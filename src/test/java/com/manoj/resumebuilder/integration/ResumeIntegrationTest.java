package com.manoj.resumebuilder.integration;


import com.fasterxml.jackson.databind.ObjectMapper;
import com.manoj.resumebuilder.dto.request.ResumeRequest;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.web.client.TestRestTemplate;
import org.springframework.boot.test.web.server.LocalServerPort;
import org.springframework.http.*;

import static org.junit.jupiter.api.Assertions.*;

@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
class ResumeIntegrationTest {

    @LocalServerPort
    private int port;

    @Autowired
    private TestRestTemplate restTemplate;

    @Autowired
    private ObjectMapper objectMapper;

    @Test
    void shouldCreateResume() {

        ResumeRequest request = new ResumeRequest();
        request.setName("Manoj Panda");
        request.setEmail("manoj@example.com");
        request.setPhone("9876543210");
        request.setEducation("B.Tech");
        request.setSkills("Java, Spring Boot");
        request.setExperience("4 Years");

        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);

        HttpEntity<ResumeRequest> entity =
                new HttpEntity<>(request, headers);

        ResponseEntity<String> response =
                restTemplate.postForEntity(
                        "http://localhost:" + port + "/resume",
                        entity,
                        String.class);

        assertTrue(response.getStatusCode().is2xxSuccessful());
    }
}