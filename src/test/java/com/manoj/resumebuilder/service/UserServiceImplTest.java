package com.manoj.resumebuilder.service;

import com.manoj.resumebuilder.dto.request.LoginRequest;
import com.manoj.resumebuilder.dto.request.RegisterRequest;
import com.manoj.resumebuilder.dto.response.UserResponse;
import com.manoj.resumebuilder.entity.User;
import com.manoj.resumebuilder.jwt.JwtUtil;
import com.manoj.resumebuilder.repository.UserRepository;
import com.manoj.resumebuilder.service.impl.UserServiceImpl;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import org.springframework.security.crypto.password.PasswordEncoder;

import java.util.Optional;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

@ExtendWith(MockitoExtension.class)
class UserServiceTest {

    @Mock
    private UserRepository userRepository;

    @Mock
    private PasswordEncoder passwordEncoder;

    @Mock
    private JwtUtil jwtUtil;

    @InjectMocks
    private UserServiceImpl userService;

    private RegisterRequest registerRequest;
    private LoginRequest loginRequest;
    private User user;

    @BeforeEach
    void setUp() {

        registerRequest = new RegisterRequest();
        registerRequest.setName("Manoj Panda");
        registerRequest.setEmail("manoj@example.com");
        registerRequest.setPassword("password123");

        loginRequest = new LoginRequest();
        loginRequest.setEmail("manoj@example.com");
        loginRequest.setPassword("password123");

        user = new User();
        user.setId(1L);
        user.setName("Manoj Panda");
        user.setEmail("manoj@example.com");
        user.setPassword("encodedPassword");
    }

    @Test
    void shouldRegisterUserSuccessfully() {

        when(userRepository.existsByEmail(anyString())).thenReturn(false);
        when(passwordEncoder.encode(anyString())).thenReturn("encodedPassword");
        when(userRepository.save(any(User.class))).thenReturn(user);

        UserResponse response = userService.register(registerRequest);

        assertNotNull(response);
        assertEquals("Manoj Panda", response.getName());
        assertEquals("manoj@example.com", response.getEmail());

        verify(userRepository).save(any(User.class));
    }

    @Test
    void shouldLoginSuccessfully() {

        when(userRepository.findByEmail(anyString())).thenReturn(Optional.of(user));
        when(passwordEncoder.matches(anyString(), anyString())).thenReturn(true);
        when(jwtUtil.generateToken(anyString())).thenReturn("jwt-token");

        String token = userService.login(loginRequest);

        assertEquals("jwt-token", token);
    }
}