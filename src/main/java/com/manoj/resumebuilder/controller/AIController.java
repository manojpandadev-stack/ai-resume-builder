package com.manoj.resumebuilder.controller;

import com.manoj.resumebuilder.dto.request.AiTextRequest;
import com.manoj.resumebuilder.dto.request.ResumeRequest;
import com.manoj.resumebuilder.dto.response.AiResponse;
import com.manoj.resumebuilder.service.AIService;
import io.github.resilience4j.ratelimiter.annotation.RateLimiter;
import jakarta.validation.Valid;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/ai")
@CrossOrigin(origins = {
        "http://localhost:3000",
        "http://localhost:3001"
})
@RateLimiter(name = "ai")
public class AIController {

    private final AIService aiService;

    public AIController(AIService aiService) {
        this.aiService = aiService;
    }

    @PostMapping("/generate")
    public ResponseEntity<AiResponse> generateResume(
            @Valid @RequestBody ResumeRequest request) {

        String prompt = """
Generate a professional ATS-friendly resume.

Name: %s
Email: %s
Phone: %s
Education: %s
Skills: %s
Experience: %s
Projects: %s
"""
                .formatted(
                        request.getName(),
                        request.getEmail(),
                        request.getPhone(),
                        request.getEducation(),
                        request.getSkills(),
                        request.getExperience(),
                        request.getProjects()
                );

        return ResponseEntity.ok(
                new AiResponse(
                        aiService.generateResume(prompt)
                )
        );
    }

    @PostMapping("/cover-letter")
    public ResponseEntity<AiResponse> generateCoverLetter(
            @Valid @RequestBody ResumeRequest request) {

        String prompt = """
Write a professional cover letter.

Candidate Name: %s
Email: %s
Phone: %s
Education: %s
Skills: %s
Experience: %s
Projects: %s

Create a professional one-page cover letter.
"""
                .formatted(
                        request.getName(),
                        request.getEmail(),
                        request.getPhone(),
                        request.getEducation(),
                        request.getSkills(),
                        request.getExperience(),
                        request.getProjects()
                );

        return ResponseEntity.ok(
                new AiResponse(
                        aiService.generateCoverLetter(prompt)
                )
        );
    }

    @PostMapping("/analyze")
    public ResponseEntity<AiResponse> analyzeResume(
            @Valid @RequestBody AiTextRequest request) {

        return ResponseEntity.ok(
                new AiResponse(
                        aiService.calculateATSScore(request.getContent())
                )
        );
    }

    @PostMapping("/improve")
    public ResponseEntity<AiResponse> improveResume(
            @Valid @RequestBody AiTextRequest request) {

        return ResponseEntity.ok(
                new AiResponse(
                        aiService.improveResume(request.getContent())
                )
        );
    }
}