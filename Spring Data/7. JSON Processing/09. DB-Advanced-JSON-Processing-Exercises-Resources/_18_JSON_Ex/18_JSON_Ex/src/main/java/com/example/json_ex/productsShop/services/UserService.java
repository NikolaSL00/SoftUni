package com.example.json_ex.productsShop.services;

import com.example.json_ex.productsShop.entities.users.User;
import com.example.json_ex.productsShop.entities.users.UsersWithSoldProductsDTO;

import java.util.List;

public interface UserService {
    List<UsersWithSoldProductsDTO> getAllWithSoldProducts();

    List<User> getAllWithSoldProductsOrderByCount();
}
