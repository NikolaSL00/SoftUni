package com.example.xml_ex.services;

import com.example.xml_ex.entities.products.ExportNamePriceProductDTO;
import com.example.xml_ex.entities.products.ExportSoldProductsDTO;
import com.example.xml_ex.entities.users.*;
import com.example.xml_ex.repositories.UserRepository;
import net.bytebuddy.jar.asm.commons.Remapper;
import org.modelmapper.ModelMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.stream.Collectors;

@Service
public class UserServiceImpl implements UserService {

    private final UserRepository userRepository;
    private final ModelMapper mapper;

    @Autowired
    public UserServiceImpl(UserRepository userRepository) {
        this.mapper = new ModelMapper();
        this.userRepository = userRepository;
    }


    @Override
    @Transactional
    public ExportSellersDTO findAllWithSoldProducts() {

        List<User> users =
                this.userRepository.findAllWithSoldProducts();

        List<ExportUserWithSoldProductsDTO> dtos = users
                .stream()
                .map(u -> this.mapper.map(u, ExportUserWithSoldProductsDTO.class))
                .collect(Collectors.toList());

        // razchitame che zaradi dobroto naimenovane na poletata na DTO modelMapper shte gi vloji dobre


        return new ExportSellersDTO(dtos);
    }

    @Override
    @Transactional
    public ExportSellersWithCountsDTO findAllWithSoldProductsAndCounts() {
        List<User> users = this.userRepository.findAllWithSoldProductsOrderByCount();

        List<ExportUserWithSoldCountDTO> dtos = users
                .stream()
                .map(this::createExportUserWithSoldCountDTO)
                .collect(Collectors.toList());

        return new ExportSellersWithCountsDTO(dtos);
    }

    private ExportUserWithSoldCountDTO createExportUserWithSoldCountDTO(User u) {
        ExportUserWithSoldCountDTO userDTO = this.mapper.map(u, ExportUserWithSoldCountDTO.class);

        List<ExportNamePriceProductDTO> namePriceProductDTOS = u.getItemsSold()
                .stream()
                .map(p -> this.mapper.map(p, ExportNamePriceProductDTO.class))
                .collect(Collectors.toList());

        ExportSoldProductsDTO soldProductsDTO = new ExportSoldProductsDTO(namePriceProductDTOS);

        userDTO.setSoldProducts(soldProductsDTO);

        return userDTO;
    }
}
