package com.manoj.resumebuilder.service.impl;

import com.manoj.resumebuilder.exception.AIProviderException;
import com.manoj.resumebuilder.service.AIService;
import io.github.resilience4j.circuitbreaker.CircuitBreaker;
import io.github.resilience4j.circuitbreaker.CircuitBreakerRegistry;
import io.github.resilience4j.core.functions.CheckedSupplier;
import io.github.resilience4j.retry.Retry;
import io.github.resilience4j.retry.RetryRegistry;
import io.github.resilience4j.timelimiter.TimeLimiter;
import io.github.resilience4j.timelimiter.TimeLimiterRegistry;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.stereotype.Service;

import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

@Service
public class AIServiceImpl implements AIService {

    private static final Logger log =
            LoggerFactory.getLogger(AIServiceImpl.class);

    private final ChatClient chatClient;
    private final CircuitBreaker circuitBreaker;
    private final Retry retry;
    private final TimeLimiter timeLimiter;

    private final ExecutorService executorService =
            Executors.newVirtualThreadPerTaskExecutor();

    public AIServiceImpl(ChatClient.Builder builder,
                         CircuitBreakerRegistry circuitBreakerRegistry,
                         RetryRegistry retryRegistry,
                         TimeLimiterRegistry timeLimiterRegistry) {

        this.chatClient = builder.build();
        this.circuitBreaker = circuitBreakerRegistry.circuitBreaker("groqAi");
        this.retry = retryRegistry.retry("groqAi");
        this.timeLimiter = timeLimiterRegistry.timeLimiter("groqAi");
    }

    @Override
    public String generateResume(String prompt) {
        return executePrompt(prompt);
    }
    @Override
    public String generateCoverLetter(String prompt) {
        return executePrompt(prompt);
    }

    @Override
    public String improveResume(String resumeText) {

        String prompt = """
You are a Senior Resume Writer.

Improve the following resume.

Resume:

%s
""".formatted(resumeText);

        return executePrompt(prompt);
    }

    @Override
    public String calculateATSScore(String resumeText) {

        String prompt = """
You are an ATS Resume Analyzer.

Analyze the following resume.

Return:

1. ATS Score
2. Missing Skills
3. Weak Points
4. Suggestions

Resume:

%s
""".formatted(resumeText);

        return executePrompt(prompt);
    }

    private String executePrompt(String prompt) {

        log.info("Sending AI request");

        CheckedSupplier<String> supplier =
                CircuitBreaker.decorateCheckedSupplier(
                        circuitBreaker,
                        Retry.decorateCheckedSupplier(
                                retry,
                                () -> chatClient
                                        .prompt(prompt)
                                        .call()
                                        .content()
                        )
                );

        try {

            return timeLimiter.executeFutureSupplier(() ->
                    CompletableFuture.supplyAsync(() -> {

                        try {
                            return supplier.get();
                        } catch (Throwable ex) {
                            throw new AIProviderException(
                                    "AI provider request failed",
                                    ex
                            );
                        }

                    }, executorService));

        } catch (Exception ex) {

            throw new AIProviderException(
                    "AI provider request failed",
                    ex
            );

        }
    }
}