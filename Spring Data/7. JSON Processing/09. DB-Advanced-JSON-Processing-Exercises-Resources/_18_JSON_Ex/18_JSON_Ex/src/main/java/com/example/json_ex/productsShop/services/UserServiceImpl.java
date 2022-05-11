package com.example.json_ex.productsShop.services;

import com.example.json_ex.productsShop.entities.users.User;
import com.example.json_ex.productsShop.entities.users.UserCountAndListOfUsersDTO;
import com.example.json_ex.productsShop.entities.users.UsersWithSoldProductsDTO;
import com.example.json_ex.productsShop.repositories.UserRepository;
import org.modelmapper.Converter;
import org.modelmapper.ModelMapper;
import org.modelmapper.TypeMap;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.Collection;
import java.util.List;
import java.util.stream.Collectors;

@Service
public class UserServiceImpl implements UserService {

    private final UserRepository userRepository;
    private final ModelMapper mapper;


    @Autowired
    public UserServiceImpl(UserRepository userRepository) {
        this.userRepository = userRepository;
        this.mapper = new ModelMapper();
    }

    @Override
    @Transactional
    public List<UsersWithSoldProductsDTO> getAllWithSoldProducts() {
        List<User> allWithSoldProducts = this.userRepository.findAllWithSoldProducts();

        return allWithSoldProducts
                .stream()
                .map(user -> this.mapper.map(user, UsersWithSoldProductsDTO.class))
                .collect(Collectors.toList());

    }

    @Override
    @Transactional
    public List<User> getAllWithSoldProductsOrderByCount() {

        List<User> all = this.userRepository.findAllWithSoldProductsOrderByCount();

        return null;
    }
}
