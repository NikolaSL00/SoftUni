package com.example.workshop1.service;

import com.example.workshop1.model.Company;
import com.example.workshop1.model.Project;
import com.example.workshop1.model.dto.ImportProjectDTO;
import com.example.workshop1.model.dto.ImportProjectsRootDTO;
import com.example.workshop1.repository.CompanyRepository;
import com.example.workshop1.repository.ProjectRepository;
import com.example.workshop1.util.MyValidator;
import org.modelmapper.ModelMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Service;

import javax.xml.bind.JAXBContext;
import javax.xml.bind.JAXBException;
import javax.xml.bind.Unmarshaller;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

@Service
public class ProjectService {
    private final MyValidator validator;

    private final ModelMapper modelMapper;

    private final Path XML_PATH = Path.of("src/main/resources/files/xmls/projects.xml");

    private final ProjectRepository projectRepository;

    private final CompanyRepository companyRepository;

    @Autowired
    public ProjectService(MyValidator validator, @Qualifier("withLocalDate") ModelMapper modelMapper, ProjectRepository projectRepository, CompanyRepository companyRepository) {
        this.validator = validator;
        this.modelMapper = modelMapper;
        this.projectRepository = projectRepository;
        this.companyRepository = companyRepository;
    }

    public boolean areImported() {
        return projectRepository.count() > 0;
    }

    public String getProjectsText() throws IOException {
        return Files.readString(XML_PATH);
    }

    public String importProjects() throws JAXBException, FileNotFoundException {
        JAXBContext context = JAXBContext.newInstance(ImportProjectsRootDTO.class);
        Unmarshaller unmarshaller = context.createUnmarshaller();

        ImportProjectsRootDTO rootDTO = (ImportProjectsRootDTO) unmarshaller
                .unmarshal(new FileReader(XML_PATH.toAbsolutePath().toString()));

        StringBuilder sb = new StringBuilder();
        List<ImportProjectDTO> projects = rootDTO.getProjects();
        for (ImportProjectDTO dto : projects) {

            if (!validator.isValid(dto)) {
                sb.append("Invalid Project\n");
                continue;
            }

            Project project =
                    this.modelMapper.map(dto, Project.class);

            Optional<Company> companyName = this.companyRepository.findByName(dto.getCompany().getName());
            project.setCompany(companyName.get());
            this.projectRepository.save(project);

            sb
                    .append("Created project - ")
                    .append(project.getName())
                    .append("for company ")
                    .append(project.getCompany().getName())
                    .append("\n");
        }
        return sb.toString();
    }

    public String getFinishedProjects() {
        List<Project> projects = this.projectRepository.findByIsFinishedTrueOrderByPaymentDesc();

        return projects
                .stream()
                .map(Project::toString)
                .collect(Collectors.joining("\n"));
    }
}
