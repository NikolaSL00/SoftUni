package exam.service.impl;

import exam.model.ImportTownsDTO;
import exam.model.Town;
import exam.repository.TownRepository;
import exam.service.TownService;
import org.modelmapper.ModelMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import javax.xml.bind.JAXBContext;
import javax.xml.bind.JAXBException;
import javax.xml.bind.Unmarshaller;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@Service
public class TownServiceImpl implements TownService {

    public static final Path XML_PATH = Path.of("src", "main", "resources", "files", "xml", "towns.xml");
    private final TownRepository townRepository;

    private final ModelMapper modelMapper;

    @Autowired
    public TownServiceImpl(TownRepository townRepository) {
        this.townRepository = townRepository;
        modelMapper = new ModelMapper();
    }

    @Override
    public boolean areImported() {
        return townRepository.count() > 0;
    }

    @Override
    public String readTownsFileContent() throws IOException {
        return String.join("\n", Files.readAllLines(XML_PATH));
    }

    @Override
    public String importTowns() throws JAXBException, IOException {
        List<String> result = new ArrayList<>();

        JAXBContext context = JAXBContext.newInstance(ImportTownsDTO.class);

        Unmarshaller unmarshaller = context.createUnmarshaller();

        ImportTownsDTO towns = (ImportTownsDTO) unmarshaller.
                unmarshal(new FileReader(XML_PATH.toAbsolutePath().toString()));

        towns.getTowns()
                .forEach(town -> {
                    if (town.isValid()) {

                        Optional<Town> optTown = this.townRepository.findByName(town.getName());

                        if (optTown.isPresent()) {
                            result.add("Town already exists");
                        } else {
                            Town toPersist = this.modelMapper.map(town, Town.class);
                            this.townRepository.save(toPersist);

                            result.add("Saved Town " + town.getName());

                        }

                    } else {
                        result.add("Invalid Town");
                    }
                });


        return String.join("\n", result);
    }
}
