package com.manoj.resumebuilder.repository;

import com.manoj.resumebuilder.entity.Resume;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;
import org.springframework.data.domain.PageRequest;
import org.springframework.test.context.DynamicPropertyRegistry;
import org.springframework.test.context.DynamicPropertySource;
import org.testcontainers.containers.MySQLContainer;
import org.testcontainers.junit.jupiter.Container;
import org.testcontainers.junit.jupiter.Testcontainers;

import static org.assertj.core.api.Assertions.assertThat;

@DataJpaTest
@Testcontainers(disabledWithoutDocker = true)
class ResumeRepositoryTest {

    @Container
    static final MySQLContainer<?> mysql = new MySQLContainer<>("mysql:8.4")
            .withDatabaseName("resume_test")
            .withUsername("test")
            .withPassword("test");

    @DynamicPropertySource
    static void databaseProperties(DynamicPropertyRegistry registry) {
        registry.add("spring.datasource.url", mysql::getJdbcUrl);
        registry.add("spring.datasource.username", mysql::getUsername);
        registry.add("spring.datasource.password", mysql::getPassword);
        registry.add("spring.jpa.hibernate.ddl-auto", () -> "create-drop");
    }

    @Autowired
    private ResumeRepository repository;

    @Test
    void searchesByNameEmailOrSkills() {
        repository.save(resume("Manoj Panda", "manoj@example.com", "Java Spring Boot"));
        repository.save(resume("Other User", "other@example.com", "React"));

        assertThat(repository.search("spring", PageRequest.of(0, 10)).getContent())
                .extracting(Resume::getEmail)
                .containsExactly("manoj@example.com");
    }

    private Resume resume(String name, String email, String skills) {
        Resume resume = new Resume();
        resume.setName(name);
        resume.setEmail(email);
        resume.setPhone("9999999999");
        resume.setEducation("B.Tech");
        resume.setSkills(skills);
        resume.setExperience("Backend engineering");
        return resume;
    }
}
