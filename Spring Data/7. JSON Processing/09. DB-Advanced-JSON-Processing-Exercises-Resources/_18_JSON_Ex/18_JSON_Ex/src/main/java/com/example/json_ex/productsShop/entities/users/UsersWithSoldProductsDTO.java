package com.example.json_ex.productsShop.entities.users;


import com.example.json_ex.productsShop.entities.products.SoldProductDTO;

import java.util.List;

public class UsersWithSoldProductsDTO {

    private String fistName;
    private String lastName;

    private List<SoldProductDTO> itemsBought;

    public List<SoldProductDTO> getItemsBought() {
        return itemsBought;
    }

    public void setItemsBought(List<SoldProductDTO> itemsBought) {
        this.itemsBought = itemsBought;
    }

    public String getFistName() {
        return fistName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setFistName(String fistName) {
        this.fistName = fistName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }


}
