package com.manoj.resumebuilder.repository;

import com.manoj.resumebuilder.entity.Resume;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface ResumeRepository extends JpaRepository<Resume, Long> {

    @Query("""
            SELECT r
            FROM Resume r
            WHERE LOWER(r.name) LIKE LOWER(CONCAT('%', :keyword, '%'))
               OR LOWER(r.email) LIKE LOWER(CONCAT('%', :keyword, '%'))
               OR LOWER(r.skills) LIKE LOWER(CONCAT('%', :keyword, '%'))
            """)
    Page<Resume> search(
            @Param("keyword") String keyword,
            Pageable pageable
    );

    Optional<Resume> findByEmail(String email);

    boolean existsByEmail(String email);
}