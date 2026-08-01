package com.manoj.resumebuilder.service;

import com.manoj.resumebuilder.dto.request.ResumeRequest;
import com.manoj.resumebuilder.dto.response.ResumeResponse;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;

public interface ResumeService {


    ResumeResponse saveResume(ResumeRequest request);


    ResumeResponse getResumeById(Long id);

    Page<ResumeResponse> getResumes(String keyword, Pageable pageable);

    ResumeResponse updateResume(Long id, ResumeRequest request);

    void deleteResume(Long id);

}