package com.manoj.resumebuilder.controller;

import com.manoj.resumebuilder.dto.request.ResumeRequest;
import com.manoj.resumebuilder.dto.response.MessageResponse;
import com.manoj.resumebuilder.dto.response.ResumeResponse;
import com.manoj.resumebuilder.service.ResumeService;
import jakarta.validation.Valid;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/resumes")
public class ResumeController {

    private final ResumeService service;

    public ResumeController(ResumeService service) {
        this.service = service;
    }

    @PostMapping
    public ResponseEntity<ResumeResponse> saveResume(
            @Valid @RequestBody ResumeRequest request) {
        System.out.println("========== SAVE RESUME ==========");
        System.out.println("Projects: " + request.getProjects());
        System.out.println("Generated Resume: " + request.getGeneratedResume());
        ResumeResponse response = service.saveResume(request);

        return ResponseEntity
                .status(HttpStatus.CREATED)
                .body(response);
    }

    @GetMapping("/{id}")
    public ResponseEntity<ResumeResponse> getResumeById(
            @PathVariable Long id) {

        return ResponseEntity.ok(service.getResumeById(id));
    }

    @GetMapping
    public ResponseEntity<Page<ResumeResponse>> getAllResumes(
            @RequestParam(required = false) String search,
            Pageable pageable) {

        return ResponseEntity.ok(service.getResumes(search, pageable));
    }

    @PutMapping("/{id}")
    public ResponseEntity<ResumeResponse> updateResume(
            @PathVariable Long id,
            @Valid @RequestBody ResumeRequest request) {

        return ResponseEntity.ok(service.updateResume(id, request));
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<MessageResponse> deleteResume(
            @PathVariable Long id) {

        service.deleteResume(id);

        return ResponseEntity.ok(
                new MessageResponse("Resume deleted successfully")
        );
    }

}