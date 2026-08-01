package com.manoj.resumebuilder.service.impl;

import com.manoj.resumebuilder.dto.request.ResumeRequest;
import com.manoj.resumebuilder.dto.response.ResumeResponse;
import com.manoj.resumebuilder.entity.Resume;
import com.manoj.resumebuilder.exception.ResourceNotFoundException;
import com.manoj.resumebuilder.repository.ResumeRepository;
import com.manoj.resumebuilder.service.ResumeService;
import jakarta.transaction.Transactional;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;
import org.springframework.util.StringUtils;

@Service
@Transactional
public class ResumeServiceImpl implements ResumeService {

    private final ResumeRepository repository;

    public ResumeServiceImpl(ResumeRepository repository) {
        this.repository = repository;
    }

    @Override
    public ResumeResponse saveResume(ResumeRequest request) {
        return toResponse(repository.save(toEntity(new Resume(), request)));
    }

    @Override
    @Transactional
    public ResumeResponse getResumeById(Long id) {

        Resume resume = repository.findById(id)
                .orElseThrow(() ->
                        new ResourceNotFoundException("Resume not found with id " + id));

        return toResponse(resume);
    }

    @Override
    public Page<ResumeResponse> getResumes(String keyword, Pageable pageable) {

        Page<Resume> resumes = StringUtils.hasText(keyword)
                ? repository.search(keyword.trim(), pageable)
                : repository.findAll(pageable);

        return resumes.map(this::toResponse);
    }

    @Override
    public ResumeResponse updateResume(Long id, ResumeRequest request) {

        Resume resume = repository.findById(id)
                .orElseThrow(() ->
                        new ResourceNotFoundException("Resume not found with id " + id));

        return toResponse(repository.save(toEntity(resume, request)));
    }

    @Override
    public void deleteResume(Long id) {

        if (!repository.existsById(id)) {
            throw new ResourceNotFoundException("Resume not found with id " + id);
        }

        repository.deleteById(id);
    }

    private Resume toEntity(Resume resume, ResumeRequest request) {

        resume.setName(request.getName());
        resume.setEmail(request.getEmail());
        resume.setPhone(request.getPhone());
        resume.setSkills(request.getSkills());
        resume.setEducation(request.getEducation());
        resume.setExperience(request.getExperience());
        resume.setProjects(request.getProjects());
        resume.setGeneratedResume(request.getGeneratedResume());

        return resume;
    }

    private ResumeResponse toResponse(Resume resume) {

        return new ResumeResponse(
                resume.getId(),
                resume.getName(),
                resume.getEmail(),
                resume.getPhone(),
                resume.getEducation(),
                resume.getSkills(),
                resume.getExperience(),
                resume.getProjects(),
                resume.getGeneratedResume()
        );
    }
}