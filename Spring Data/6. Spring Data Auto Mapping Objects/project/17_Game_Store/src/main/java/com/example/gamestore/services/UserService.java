package com.example.gamestore.services;

import com.example.gamestore.entities.users.LoginDTO;
import com.example.gamestore.entities.users.RegisterDTO;
import com.example.gamestore.entities.users.User;

import java.util.Optional;

public interface UserService {
    User register(RegisterDTO registerDTO);
    void logout();
    Optional<User> login(LoginDTO loginData);

    User getLoggedUser();
}
