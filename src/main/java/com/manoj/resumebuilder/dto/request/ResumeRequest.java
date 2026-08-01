package com.manoj.resumebuilder.dto.request;

import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Size;

public class ResumeRequest {

    @NotBlank
    @Size(max = 120)
    private String name;

    @NotBlank
    @Email
    @Size(max = 160)
    private String email;

    @NotBlank
    @Size(max = 30)
    private String phone;

    @NotBlank
    @Size(max = 2000)
    private String education;

    @NotBlank
    @Size(max = 2000)
    private String skills;

    @NotBlank
    @Size(max = 4000)
    private String experience;

    @Size(max = 4000)
    private String projects;

    @Size(max = 50000)
    private String generatedResume;

    public ResumeRequest() {
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }

    public String getEducation() {
        return education;
    }

    public void setEducation(String education) {
        this.education = education;
    }

    public String getSkills() {
        return skills;
    }

    public void setSkills(String skills) {
        this.skills = skills;
    }

    public String getExperience() {
        return experience;
    }

    public void setExperience(String experience) {
        this.experience = experience;
    }

    public String getProjects() {
        return projects;
    }

    public void setProjects(String projects) {
        this.projects = projects;
    }

    public String getGeneratedResume() {
        return generatedResume;
    }

    public void setGeneratedResume(String generatedResume) {
        this.generatedResume = generatedResume;
    }
}