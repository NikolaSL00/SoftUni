package com.example.json_ex.productsShop.entities.users;

import java.util.List;

public class UserCountAndListOfUsersDTO {
    private int usersCount;
    private List<User> users;

    public UserCountAndListOfUsersDTO(int usersCount, List<User> users) {
        this.usersCount = usersCount;
        this.users = users;
    }

    public int getUsersCount() {
        return usersCount;
    }

    public void setUsersCount(int usersCount) {
        this.usersCount = usersCount;
    }

    public List<User> getUsers() {
        return users;
    }

    public void setUsers(List<User> users) {
        this.users = users;
    }
}
