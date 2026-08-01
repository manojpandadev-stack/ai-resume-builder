package com.manoj.resumebuilder.service.impl;

import com.manoj.resumebuilder.dto.request.LoginRequest;
import com.manoj.resumebuilder.dto.request.RegisterRequest;
import com.manoj.resumebuilder.dto.response.UserResponse;
import com.manoj.resumebuilder.entity.User;
import com.manoj.resumebuilder.exception.ConflictException;
import com.manoj.resumebuilder.exception.UnauthorizedException;
import com.manoj.resumebuilder.jwt.JwtUtil;
import com.manoj.resumebuilder.repository.UserRepository;
import com.manoj.resumebuilder.service.UserService;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.security.crypto.password.PasswordEncoder;

@Service
@Transactional
public class UserServiceImpl implements UserService {

    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;
    private final JwtUtil jwtUtil;

    public UserServiceImpl(UserRepository userRepository,
                           PasswordEncoder passwordEncoder,
                           JwtUtil jwtUtil) {
        this.userRepository = userRepository;
        this.passwordEncoder = passwordEncoder;
        this.jwtUtil = jwtUtil;
    }

    @Override
    public UserResponse register(RegisterRequest request) {

        if (userRepository.existsByEmail(request.getEmail())) {
            throw new ConflictException("Email already exists.");
        }

        User user = new User();
        user.setName(request.getName().trim());
        user.setEmail(request.getEmail().trim().toLowerCase());
        user.setPassword(passwordEncoder.encode(request.getPassword()));

        User savedUser = userRepository.save(user);

        return new UserResponse(
                savedUser.getId(),
                savedUser.getName(),
                savedUser.getEmail()
        );
    }

    @Override
    @Transactional(readOnly = true)
    public String login(LoginRequest request) {

        User user = userRepository.findByEmail(request.getEmail().trim().toLowerCase())
                .orElseThrow(() ->
                        new UnauthorizedException("Invalid email or password."));

        if (!passwordEncoder.matches(request.getPassword(), user.getPassword())) {
            throw new UnauthorizedException("Invalid email or password.");
        }

        return jwtUtil.generateToken(user.getEmail());
    }
}