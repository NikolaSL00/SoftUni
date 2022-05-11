package com.example.json_ex.productsShop.entities.products;

import org.springframework.beans.factory.annotation.Value;

import java.math.BigDecimal;

public class ProductWithoutBuyerDTO {

    private String name;
    private BigDecimal price;
    private String seller;

    public ProductWithoutBuyerDTO(String name, BigDecimal price, String firstName, String lastName) {
        this.name = name;
        this.price = price;

        if (firstName == null) {
            this.seller = lastName;
        } else {
            this.seller = firstName + " " + lastName;
        }
    }

    public String getName() {
        return name;
    }

    public BigDecimal getPrice() {
        return price;
    }

    public String getSeller() {
        return seller;
    }

    //    String getName();
//
//    BigDecimal getPrice();
//
//    @Value("#{target.seller.firstName + ' ' + target.seller.lastName}")
//    String getSeller();
}
