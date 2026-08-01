package com.manoj.resumebuilder.dto.request;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Size;

public class AiTextRequest {

    @NotBlank
    @Size(max = 12000)
    private String content;

    public AiTextRequest() {
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }
}
