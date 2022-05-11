package com.example.workshop1.repository;

import com.example.workshop1.model.Employee;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface EmployeeRepository extends JpaRepository<Employee, Long> {

    long count();

    List<Employee> findByAgeGreaterThanOrderByProjectNameAsc(int age);
}
