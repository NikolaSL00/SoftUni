package com.example.json_ex.productsShop.services;

import com.example.json_ex.productsShop.entities.products.Product;
import com.example.json_ex.productsShop.entities.categories.Category;
import com.example.json_ex.productsShop.entities.categories.CategoriesImportDTO;
import com.example.json_ex.productsShop.entities.products.ProductsImportDTO;
import com.example.json_ex.productsShop.entities.users.User;
import com.example.json_ex.productsShop.entities.users.UserImportDTO;
import com.example.json_ex.productsShop.repositories.CategoryRepository;
import com.example.json_ex.productsShop.repositories.ProductRepository;
import com.example.json_ex.productsShop.repositories.UserRepository;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import org.modelmapper.ModelMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.math.BigDecimal;
import java.util.*;
import java.util.stream.Collectors;

@Service
public class SeedServiceImpl implements SeedService {

    private static final String USERS_JSON_PATH = "E:\\Downloads\\SoftUni\\Java\\Spring Data\\7. JSON Processing\\09. DB-Advanced-JSON-Processing-Exercises-Resources\\_18_JSON_Ex\\18_JSON_Ex\\src\\main\\resources\\productShop\\users.json";
    private static final String CATEGORIES_JSON_PATH = "E:\\Downloads\\SoftUni\\Java\\Spring Data\\7. JSON Processing\\09. DB-Advanced-JSON-Processing-Exercises-Resources\\_18_JSON_Ex\\18_JSON_Ex\\src\\main\\resources\\productShop\\categories.json";
    private static final String PRODUCTS_JSON_PATH = "E:\\Downloads\\SoftUni\\Java\\Spring Data\\7. JSON Processing\\09. DB-Advanced-JSON-Processing-Exercises-Resources\\_18_JSON_Ex\\18_JSON_Ex\\src\\main\\resources\\productShop\\products.json";
    private final UserRepository userRepository;

    private final CategoryRepository categoryRepository;
    private final ModelMapper modelMapper;
    private final Gson gson;
    private final ProductRepository productRepository;

    @Autowired
    public SeedServiceImpl(UserRepository userRepository, CategoryRepository categoryRepository, ProductRepository productRepository) {
        this.userRepository = userRepository;
        this.categoryRepository = categoryRepository;
        this.productRepository = productRepository;

        this.modelMapper = new ModelMapper();

        this.gson = new GsonBuilder().setPrettyPrinting().create();
    }

    @Override
    public void seedUsers() throws FileNotFoundException {
        FileReader fileReader = new FileReader(USERS_JSON_PATH);
        UserImportDTO[] userImportDTOS = this.gson.fromJson(fileReader, UserImportDTO[].class);

        List<User> users = Arrays
                .stream(userImportDTOS)
                .map(importDTO -> this.modelMapper.map(importDTO, User.class))
                .collect(Collectors.toList());

        this.userRepository.saveAll(users);
    }

    @Override
    public void seedCategories() throws FileNotFoundException {
        FileReader fileReader = new FileReader(CATEGORIES_JSON_PATH);
        CategoriesImportDTO[] categoriesImportDTOS = this.gson.fromJson(fileReader, CategoriesImportDTO[].class);

        List<Category> categories = Arrays.stream(categoriesImportDTOS).map(importDTO -> this.modelMapper.map(importDTO, Category.class)).collect(Collectors.toList());

        this.categoryRepository.saveAll(categories);
    }

    @Override
    public void seedProducts() throws FileNotFoundException {
        FileReader fileReader = new FileReader(PRODUCTS_JSON_PATH);
        ProductsImportDTO[] productsImportDTOS = this.gson.fromJson(fileReader, ProductsImportDTO[].class);

        List<Product> products = Arrays.stream(productsImportDTOS)
                .map(importDTO -> this.modelMapper.map(importDTO, Product.class))
                .map(this::setRandomSeller)
                .map(this::setRandomBuyer)
                .map(this::setRandomCategories)
                .collect(Collectors.toList());

        this.productRepository.saveAll(products);
    }

    private Product setRandomCategories(Product product) {

        Random random = new Random();

        long categoriesDbCount = this.categoryRepository.count();
        int count = random.nextInt((int) categoriesDbCount);
        Set<Category> categories = new HashSet<>();

        for (int i = 0; i < count; i++) {
            int randomId = random.nextInt((int) categoriesDbCount) + 1;

            Optional<Category> randomCategory = this.categoryRepository.findById(randomId);

            categories.add(randomCategory.get());
        }

        product.setCategories(categories);
        return product;
    }

    private Product setRandomBuyer(Product product) {
        if (product.getPrice().compareTo(BigDecimal.valueOf(944)) > 0) {
            return product;
        }

        Optional<User> buyer = getRandomUser();

        product.setBuyer(buyer.get());

        return product;
    }

    private Product setRandomSeller(Product product) {
        Optional<User> seller = getRandomUser();

        product.setSeller(seller.get());

        return product;
    }

    private Optional<User> getRandomUser() {
        long usersCount = this.userRepository.count();

        int randomUserId = new Random().nextInt((int) usersCount) + 1;

        Optional<User> buyer = this.userRepository.findById(randomUserId);
        return buyer;
    }
}
