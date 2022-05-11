package com.example.workshop1.repository;

import com.example.workshop1.model.Company;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface CompanyRepository extends JpaRepository<Company, Long> {
    long count();
    Optional<Company> findByName(String name);
}
