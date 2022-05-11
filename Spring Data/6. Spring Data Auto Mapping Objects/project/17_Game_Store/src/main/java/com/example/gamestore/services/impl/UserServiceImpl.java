package com.example.gamestore.services.impl;

import com.example.gamestore.entities.users.LoginDTO;
import com.example.gamestore.entities.users.RegisterDTO;
import com.example.gamestore.entities.users.User;
import com.example.gamestore.exceptions.UserNotLoggedInException;
import com.example.gamestore.repositories.UserRepository;
import com.example.gamestore.services.UserService;
import org.modelmapper.ModelMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.util.Optional;

@Component
public class UserServiceImpl implements UserService {

    private User currentUser;
    private final UserRepository userRepository;

    @Autowired
    public UserServiceImpl(UserRepository userRepository) {
        this.currentUser = null;
        this.userRepository = userRepository;
    }

    @Override
    public User register(RegisterDTO registerDTO) {

        if (this.currentUser != null) {
            // throw exception / return
        }

        ModelMapper mapper = new ModelMapper();
        User toRegister = mapper.map(registerDTO, User.class);

        long userCount = this.userRepository.count();
        if (userCount == 0) {
            toRegister.setAdmin(true);
        }

        return this.userRepository.save(toRegister);
    }


    @Override
    public Optional<User> login(LoginDTO loginData) {
        if (this.currentUser != null) {
            // throw exception / return
        }

        Optional<User> user = this.userRepository
                .findByEmailAndPassword(loginData.getEmail(), loginData.getPassword());

        user.ifPresent(value -> this.currentUser = value);

        return user;
    }

    @Override
    public User getLoggedUser() {
        return this.getCurrentUser();
    }

    public User getCurrentUser() {
        if(this.currentUser == null){
            throw new UserNotLoggedInException("Execute Login command first!");
        }
        return this.currentUser;
    }


    @Override
    public void logout() {
        if (this.currentUser != null) {
            this.currentUser = null;
        } else {
            throw new UserNotLoggedInException("Can not log out. No user was logged in");
        }
    }
}
