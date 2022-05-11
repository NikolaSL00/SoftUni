package com.example.gamestore.entities.users;


import com.example.gamestore.exceptions.ValidationException;

/**
 * Validate the data for registering a user
 * <p>
 * Email must be ...
 * Password must be ...
 * <p>
 * commandParts[0] is skipped because it contains the command name
 * which is not needed in the user object
 *
 * @param commandParts all data read from the console
 */

public class RegisterDTO {
    private String email;

    private String password;

    private String confirmPassword;

    private String fullName;

    public RegisterDTO(String[] commandParts) {
        this.email = commandParts[1];
        this.password = commandParts[2];
        this.confirmPassword = commandParts[3];
        this.fullName = commandParts[4];

        this.validate();
    }

    private void validate() {
        // ..
        // throw new ValidationException();

        int indexOfAt = email.indexOf("@");
        int indexOfDot = email.lastIndexOf(".");
        if (indexOfAt < 0 || indexOfDot < 0 || indexOfAt > indexOfDot) {
            throw new ValidationException("Email must contain @ and .");
        }


        // TODO: Validate password
        if (!password.equals(confirmPassword)) {
            throw new ValidationException("Passwords do not match.");
        }

    }

    public String getEmail() {
        return email;
    }

    public String getPassword() {
        return password;
    }

    public String getConfirmPassword() {
        return confirmPassword;
    }

    public String getFullName() {
        return fullName;
    }

}
