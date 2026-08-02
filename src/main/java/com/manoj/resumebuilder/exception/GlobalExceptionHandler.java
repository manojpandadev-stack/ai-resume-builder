package com.manoj.resumebuilder.exception;

import com.manoj.resumebuilder.dto.response.ErrorResponse;
import jakarta.servlet.http.HttpServletRequest;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.AccessDeniedException;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import java.time.Instant;
import java.util.LinkedHashMap;
import java.util.Map;
import org.springframework.web.servlet.resource.NoResourceFoundException;

@RestControllerAdvice
public class GlobalExceptionHandler {

    private static final Logger log =
            LoggerFactory.getLogger(GlobalExceptionHandler.class);

    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<ErrorResponse> handleValidation(
            MethodArgumentNotValidException ex,
            HttpServletRequest request) {

        log.warn("Validation failed: {}", ex.getMessage());

        Map<String, String> validationErrors = new LinkedHashMap<>();

        ex.getBindingResult()
                .getFieldErrors()
                .forEach(error ->
                        validationErrors.put(
                                error.getField(),
                                error.getDefaultMessage()));

        return build(
                HttpStatus.BAD_REQUEST,
                "Validation failed",
                request,
                validationErrors);
    }

    @ExceptionHandler(ResourceNotFoundException.class)
    public ResponseEntity<ErrorResponse> handleNotFound(
            ResourceNotFoundException ex,
            HttpServletRequest request) {

        log.warn("Resource not found: {}", ex.getMessage());

        return build(
                HttpStatus.NOT_FOUND,
                ex.getMessage(),
                request,
                null);
    }

    @ExceptionHandler(ConflictException.class)
    public ResponseEntity<ErrorResponse> handleConflict(
            ConflictException ex,
            HttpServletRequest request) {

        log.warn("Conflict: {}", ex.getMessage());

        return build(
                HttpStatus.CONFLICT,
                ex.getMessage(),
                request,
                null);
    }

    @ExceptionHandler(UnauthorizedException.class)
    public ResponseEntity<ErrorResponse> handleUnauthorized(
            UnauthorizedException ex,
            HttpServletRequest request) {

        log.warn("Unauthorized access: {}", ex.getMessage());

        return build(
                HttpStatus.UNAUTHORIZED,
                ex.getMessage(),
                request,
                null);
    }

    @ExceptionHandler(AccessDeniedException.class)
    public ResponseEntity<ErrorResponse> handleAccessDenied(
            AccessDeniedException ex,
            HttpServletRequest request) {

        log.warn("Access denied: {}", ex.getMessage());

        return build(
                HttpStatus.FORBIDDEN,
                "Access denied",
                request,
                null);
    }

    @ExceptionHandler(AIProviderException.class)
    public ResponseEntity<ErrorResponse> handleAIProvider(
            AIProviderException ex,
            HttpServletRequest request) {

        log.warn("AI provider failure: {}", ex.getMessage());

        return build(
                HttpStatus.BAD_GATEWAY,
                ex.getMessage(),
                request,
                null);
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<ErrorResponse> handleUnexpected(
            Exception ex,
            HttpServletRequest request) {

        log.error("Unhandled request failure", ex);

        return build(
                HttpStatus.INTERNAL_SERVER_ERROR,
                "Unexpected server error",
                request,
                null);
    }


    @ExceptionHandler(NoResourceFoundException.class)
    public ResponseEntity<Void> handleNoResourceFound(NoResourceFoundException ex) {
        return ResponseEntity.notFound().build();
    }


    private ResponseEntity<ErrorResponse> build(
            HttpStatus status,
            String message,
            HttpServletRequest request,
            Map<String, String> validationErrors) {

        ErrorResponse response = new ErrorResponse(
                Instant.now(),
                status.value(),
                status.getReasonPhrase(),
                message,
                request.getRequestURI(),
                validationErrors);

        return ResponseEntity.status(status).body(response);
    }
}