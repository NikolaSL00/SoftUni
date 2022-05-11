package com.example.workshop1.repository;

import com.example.workshop1.model.Project;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public interface ProjectRepository extends JpaRepository<Project, Long> {
    long count();

    Optional<Project> findByName(String name);

    List<Project> findByIsFinishedTrueOrderByPaymentDesc();
}
