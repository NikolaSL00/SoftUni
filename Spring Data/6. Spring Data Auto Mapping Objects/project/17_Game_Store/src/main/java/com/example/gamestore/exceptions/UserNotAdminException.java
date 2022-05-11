package com.example.gamestore.exceptions;

public class UserNotAdminException extends RuntimeException {

    public UserNotAdminException(){
        super("Current user is not admin and can not add games!");
    }

}
