package com.manoj.resumebuilder.service;

import com.manoj.resumebuilder.dto.request.ResumeRequest;
import com.manoj.resumebuilder.dto.response.ResumeResponse;
import com.manoj.resumebuilder.entity.Resume;
import com.manoj.resumebuilder.repository.ResumeRepository;
import com.manoj.resumebuilder.service.impl.ResumeServiceImpl;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import static org.junit.jupiter.api.Assertions.*;
        import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.*;

@ExtendWith(MockitoExtension.class)
class ResumeServiceTest {

    @Mock
    private ResumeRepository resumeRepository;

    @InjectMocks
    private ResumeServiceImpl resumeService;

    private ResumeRequest request;
    private Resume resume;

    @BeforeEach
    void setUp() {
        request = new ResumeRequest();
        request.setName("Manoj Panda");
        request.setEmail("manoj@example.com");
        request.setPhone("9876543210");
        request.setSkills("Java, Spring Boot");
        request.setEducation("B.Tech");
        request.setExperience("4 Years");

        resume = new Resume();
        resume.setId(1L);
        resume.setName(request.getName());
        resume.setEmail(request.getEmail());
        resume.setPhone(request.getPhone());
        resume.setSkills(request.getSkills());
        resume.setEducation(request.getEducation());
        resume.setExperience(request.getExperience());
    }

    @Test
    void shouldSaveResumeSuccessfully() {

        when(resumeRepository.save(any(Resume.class))).thenReturn(resume);

        ResumeResponse response = resumeService.saveResume(request);

        assertNotNull(response);
        assertEquals("Manoj Panda", response.getName());
        assertEquals("manoj@example.com", response.getEmail());

        verify(resumeRepository, times(1)).save(any(Resume.class));
    }
}
