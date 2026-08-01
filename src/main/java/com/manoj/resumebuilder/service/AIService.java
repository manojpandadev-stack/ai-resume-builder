package com.manoj.resumebuilder.service;

public interface AIService {

    String generateResume(String prompt);

    String generateCoverLetter(String prompt);

    String improveResume(String resumeText);

    String calculateATSScore(String resumeText);
}