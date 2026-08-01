package com.manoj.resumebuilder.service;

import com.manoj.resumebuilder.dto.request.ResumeRequest;
import com.manoj.resumebuilder.dto.response.ResumeResponse;
import com.manoj.resumebuilder.exception.ResourceNotFoundException;
import com.manoj.resumebuilder.entity.Resume;
import com.manoj.resumebuilder.repository.ResumeRepository;
import com.manoj.resumebuilder.service.impl.ResumeServiceImpl;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import java.util.Optional;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

@ExtendWith(MockitoExtension.class)
class ResumeServiceImplTest {

    @Mock
    private ResumeRepository repository;

    @InjectMocks
    private ResumeServiceImpl service;

    @Test
    void savesResumeAndReturnsDto() {
        Resume savedResume = resume();
        savedResume.setId(1L);
        when(repository.save(any(Resume.class))).thenReturn(savedResume);

        ResumeResponse response = service.saveResume(request());

        assertThat(response.getId()).isEqualTo(1L);
        assertThat(response.getEmail()).isEqualTo("manoj@example.com");
        verify(repository).save(any(Resume.class));
    }

    @Test
    void updateThrowsWhenResumeDoesNotExist() {
        when(repository.findById(99L)).thenReturn(Optional.empty());

        assertThatThrownBy(() -> service.updateResume(99L, request()))
                .isInstanceOf(ResourceNotFoundException.class)
                .hasMessageContaining("Resume not found");
    }

    private ResumeRequest request() {
        ResumeRequest request = new ResumeRequest();
        request.setName("Manoj Panda");
        request.setEmail("manoj@example.com");
        request.setPhone("9999999999");
        request.setEducation("B.Tech");
        request.setSkills("Java, Spring Boot, MySQL");
        request.setExperience("4 years backend engineering");
        request.setProjects("AI resume builder");
        return request;
    }

    private Resume resume() {
        Resume resume = new Resume();
        resume.setName("Manoj Panda");
        resume.setEmail("manoj@example.com");
        resume.setPhone("9999999999");
        resume.setEducation("B.Tech");
        resume.setSkills("Java, Spring Boot, MySQL");
        resume.setExperience("4 years backend engineering");
        return resume;
    }
}
