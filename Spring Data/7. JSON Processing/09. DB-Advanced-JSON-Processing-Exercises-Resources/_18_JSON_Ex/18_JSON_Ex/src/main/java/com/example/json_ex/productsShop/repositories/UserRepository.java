package com.example.json_ex.productsShop.repositories;

import com.example.json_ex.productsShop.entities.users.User;
import com.example.json_ex.productsShop.entities.users.UserCountAndListOfUsersDTO;
import com.example.json_ex.productsShop.entities.users.UsersWithSoldProductsDTO;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface UserRepository extends JpaRepository<User, Integer> {
    @Query("SELECT user FROM User user " +
            "JOIN user.itemsSold product " +
            "WHERE product.buyer IS NOT NULL")
    List<User> findAllWithSoldProducts();



//    @Query("SELECT new com.example.json_ex.productsShop.entities.users.UserCountAndListOfUsersDTO(" +
//            " COUNT(u),  ) " +
//            "FROM User u " +
//            "JOIN u.itemsSold product " +
//            "WHERE product.buyer IS NOT NULL " +
//            "ORDER BY size(u.itemsSold) DESC, u.lastName ASC")
//    List<User> findAllWithSoldProductsOrderByCount();


}
