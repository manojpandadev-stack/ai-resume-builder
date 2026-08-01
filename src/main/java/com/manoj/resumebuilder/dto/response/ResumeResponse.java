package com.manoj.resumebuilder.dto.response;

public class ResumeResponse {

    private Long id;
    private String name;
    private String email;
    private String phone;
    private String education;
    private String skills;
    private String experience;
    private String projects;
    private String generatedResume;

    public ResumeResponse() {
    }

    public ResumeResponse(
            Long id,
            String name,
            String email,
            String phone,
            String education,
            String skills,
            String experience,
            String projects,
            String generatedResume) {

        this.id = id;
        this.name = name;
        this.email = email;
        this.phone = phone;
        this.education = education;
        this.skills = skills;
        this.experience = experience;
        this.projects = projects;
        this.generatedResume = generatedResume;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
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