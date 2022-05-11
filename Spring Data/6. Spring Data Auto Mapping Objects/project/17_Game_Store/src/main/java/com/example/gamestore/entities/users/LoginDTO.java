package com.example.gamestore.entities.users;

import com.example.gamestore.exceptions.ValidationException;

public class LoginDTO {
    private String email;
    private String password;

    public LoginDTO(String[] commandLineParts) {
        this.email = commandLineParts[1];
        this.password = commandLineParts[2];

        this.validate();
    }

    public String getEmail() {
        return email;
    }

    public String getPassword() {
        return password;
    }

    private void validate() {
        // ..
        // throw new ValidationException();

        int indexOfAt = email.indexOf("@");
        int indexOfDot = email.lastIndexOf(".");
        if (indexOfAt < 0 || indexOfDot < 0 || indexOfAt > indexOfDot) {
            throw new ValidationException("Email must contain @ and .");
        }

        if(this.password.isEmpty()){
            throw new ValidationException("Password can not be empty!");
        }
    }

}
