package com.example.json_ex.productsShop.entities.users;

import com.example.json_ex.productsShop.entities.products.Product;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

@Entity
@Table(name = "users")
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;

    @Column(name = "first_name")
    private String firstName;

    @Column(name = "last_name", nullable = false)
    private String lastName;

    private Integer age;

    @OneToMany(targetEntity = Product.class, mappedBy = "seller")
    private List<Product> itemsSold;

    @OneToMany(targetEntity = Product.class, mappedBy = "buyer")
    private List<Product> itemsBought;

    @ManyToMany
    private Set<User> friends;

    public User(String firstName, String lastName, Integer age) {
        this();
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age;
    }
    public User() {
        this.itemsSold = new ArrayList<>();
        this.itemsBought = new ArrayList<>();
        this.friends = new HashSet<>();
    }

    public Set<User> getFriends() {
        return friends;
    }

    public void setFriends(Set<User> friends) {
        this.friends = friends;
    }

    public List<Product> getItemsSold() {
        return itemsSold;
    }

    public void setItemsSold(List<Product> itemsSold) {
        this.itemsSold = itemsSold;
    }

    public List<Product> getItemsBought() {
        return itemsBought;
    }

    public void setItemsBought(List<Product> itemsBought) {
        this.itemsBought = itemsBought;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public Integer getAge() {
        return age;
    }

    public void setAge(Integer age) {
        this.age = age;
    }
}
