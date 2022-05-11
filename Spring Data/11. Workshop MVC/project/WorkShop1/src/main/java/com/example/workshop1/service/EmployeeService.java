package com.example.workshop1.service;

import com.example.workshop1.model.Employee;
import com.example.workshop1.model.Project;
import com.example.workshop1.model.dto.ExportEmployeeDTO;
import com.example.workshop1.model.dto.ImportEmployeeDTO;
import com.example.workshop1.model.dto.ImportEmployeesRootDTO;
import com.example.workshop1.repository.EmployeeRepository;
import com.example.workshop1.repository.ProjectRepository;
import com.example.workshop1.util.MyValidator;
import org.modelmapper.ModelMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Service;

import javax.xml.bind.JAXBContext;
import javax.xml.bind.JAXBException;
import javax.xml.bind.Unmarshaller;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

@Service
public class EmployeeService {
    private final MyValidator validator;

    private final Path XML_PATH = Path.of("src/main/resources/files/xmls/employees.xml");
    private final EmployeeRepository employeeRepository;
    private final ModelMapper modelMapper;
    private final ProjectRepository projectRepository;

    @Autowired
    public EmployeeService(MyValidator validator,
                           EmployeeRepository employeeRepository,
                           @Qualifier("withLocalDate") ModelMapper modelMapper,
                           ProjectRepository projectRepository) {

        this.validator = validator;
        this.employeeRepository = employeeRepository;
        this.modelMapper = modelMapper;
        this.projectRepository = projectRepository;
    }

    public boolean areImported() {
        return employeeRepository.count() > 0;
    }

    public String getEmployeesText() throws IOException {
        return Files.readString(Path.of(XML_PATH.toAbsolutePath().toString()));
    }

    public String importEmployees() throws JAXBException {
        JAXBContext context = JAXBContext.newInstance(ImportEmployeesRootDTO.class);
        Unmarshaller unmarshaller = context.createUnmarshaller();

        ImportEmployeesRootDTO rootDTO = (ImportEmployeesRootDTO) unmarshaller
                .unmarshal(new File(XML_PATH.toAbsolutePath().toString()));

        return rootDTO
                .getEmployees()
                .stream()
                .map(this::importEmployee)
                .collect(Collectors.joining("\n"));
    }

    private String importEmployee(ImportEmployeeDTO dto) {
        if (!validator.isValid(dto)) {
            return "Invalid Employee or Project";
        }
        Employee employee = this.modelMapper.map(dto, Employee.class);

        Optional<Project> optionalProject = this.projectRepository.
                findByName(dto.getProject().getName());

        if (optionalProject.isEmpty()) {
            return "Invalid Project Name";
        }

        employee.setProject(optionalProject.get());
        this.employeeRepository.save(employee);

        return "Successfully imported Employee - "
                + employee.getFirstName()
                + " "
                + employee.getLastName();
    }

    public List<ExportEmployeeDTO> getEmployeesAbove() {
        List<Employee> employees = this.employeeRepository.findByAgeGreaterThanOrderByProjectNameAsc(25);

        return employees
                .stream()
                .map(ExportEmployeeDTO::new)
                .collect(Collectors.toList());
    }
}
