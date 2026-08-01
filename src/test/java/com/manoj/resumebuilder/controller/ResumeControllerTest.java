package com.manoj.resumebuilder.controller;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.manoj.resumebuilder.dto.request.ResumeRequest;
import com.manoj.resumebuilder.dto.response.ResumeResponse;
import com.manoj.resumebuilder.service.ResumeService;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.test.context.bean.override.mockito.MockitoBean;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.when;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

@WebMvcTest(ResumeController.class)
class ResumeControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @MockitoBean
    private ResumeService resumeService;

    @Autowired
    private ObjectMapper objectMapper;

    @Test
    void shouldCreateResume() throws Exception {

        ResumeRequest request = new ResumeRequest();
        request.setName("Manoj Panda");
        request.setEmail("manoj@example.com");
        request.setPhone("9876543210");
        request.setEducation("B.Tech");
        request.setSkills("Java, Spring Boot");
        request.setExperience("4 Years");

        ResumeResponse response = new ResumeResponse(


        when(resumeService.saveResume(any())).thenReturn(response);

        mockMvc.perform(post("/resume")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(request)))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.name").value("Manoj Panda"))
                .andExpect(jsonPath("$.email").value("manoj@example.com"));
    }
}