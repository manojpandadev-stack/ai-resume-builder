package com.manoj.resumebuilder.service;

import com.manoj.resumebuilder.dto.request.LoginRequest;
import com.manoj.resumebuilder.dto.request.RegisterRequest;
import com.manoj.resumebuilder.dto.response.UserResponse;

public interface UserService {

    UserResponse register(RegisterRequest request);

    String login(LoginRequest request);
}