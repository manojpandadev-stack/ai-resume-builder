package com.manoj.resumebuilder.controller;


import com.manoj.resumebuilder.dto.response.AuthResponse;
import com.manoj.resumebuilder.dto.request.LoginRequest;
import com.manoj.resumebuilder.dto.response.MessageResponse;
import com.manoj.resumebuilder.dto.request.RegisterRequest;
import com.manoj.resumebuilder.service.UserService;
import jakarta.validation.Valid;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/auth")
@CrossOrigin(origins = {
        "http://localhost:3000",
        "http://localhost:3001"
})
public class AuthController {

    private final UserService userService;

    public AuthController(UserService userService) {
        this.userService = userService;
    }

    @PostMapping("/register")
    public MessageResponse register(@Valid @RequestBody RegisterRequest request) {
        userService.register(request);
        return new MessageResponse("User registered successfully");
    }

    @PostMapping("/login")
    public AuthResponse login(@Valid @RequestBody LoginRequest request) {
        return new AuthResponse(userService.login(request));
    }
}
