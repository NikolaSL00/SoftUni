package com.example.gamestore.exceptions;

public class UserNotLoggedInException extends RuntimeException {
    public UserNotLoggedInException(String s) {
        super(s);
    }
}
