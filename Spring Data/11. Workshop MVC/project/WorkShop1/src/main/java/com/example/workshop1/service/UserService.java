package com.example.workshop1.service;

import com.example.workshop1.model.User;
import com.example.workshop1.model.dto.RegistrationDTO;
import com.example.workshop1.repository.UserRepository;
import org.modelmapper.ModelMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Service;

@Service
public class UserService {

    private final ModelMapper modelMapper;
    private final UserRepository userRepository;


    @Autowired
    public UserService(@Qualifier("default") ModelMapper modelMapper, UserRepository userRepository) {
        this.modelMapper = modelMapper;
        this.userRepository = userRepository;
    }

    public void register(RegistrationDTO dto) {
        User user = this.modelMapper.map(dto, User.class);

        this.userRepository.save(user);
    }
}
