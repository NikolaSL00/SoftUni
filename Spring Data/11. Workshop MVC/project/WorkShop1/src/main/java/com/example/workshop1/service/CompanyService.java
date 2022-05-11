package com.example.workshop1.service;

import com.example.workshop1.model.Company;
import com.example.workshop1.model.dto.ImportCompaniesRootDTO;
import com.example.workshop1.model.dto.ImportCompanyDTO;
import com.example.workshop1.repository.CompanyRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import javax.xml.bind.JAXBContext;
import javax.xml.bind.JAXBException;
import javax.xml.bind.Unmarshaller;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

@Service
public class CompanyService {

    private final Path XML_PATH = Path.of("src/main/resources/files/xmls/companies.xml");
    private final CompanyRepository companyRepository;

    @Autowired
    public CompanyService(CompanyRepository companyRepository) {
        this.companyRepository = companyRepository;
    }

    public boolean areImported() {
        return companyRepository.count() > 0;
    }

    public String getCompaniesText() throws IOException {
        return Files.readString(XML_PATH);
    }

    public String importCompanies() throws JAXBException, FileNotFoundException {
        JAXBContext context = JAXBContext.newInstance(ImportCompaniesRootDTO.class);
        Unmarshaller unmarshaller = context.createUnmarshaller();

        ImportCompaniesRootDTO rootDTO =
                (ImportCompaniesRootDTO) unmarshaller
                        .unmarshal(new FileReader(XML_PATH.toAbsolutePath().toString()));

        return rootDTO.getCompanies()
                .stream()
                .map(ImportCompanyDTO::getName)
                .map(Company::new)
                .map(c -> {
                    Optional<Company> optCompany =
                            this.companyRepository.findByName(c.getName());

                    if (optCompany.isPresent()) {
                        return "Invalid company.";
                    }

                    this.companyRepository.save(c);
                    return "Created company - " + c.getName();

                })
                .collect(Collectors.joining("\n"));


    }
}
