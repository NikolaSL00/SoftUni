package com.example.json_ex.productsShop;

import com.example.json_ex.productsShop.entities.categories.CategoryStatsDTO;
import com.example.json_ex.productsShop.entities.products.ProductWithoutBuyerDTO;
import com.example.json_ex.productsShop.entities.users.UsersWithSoldProductsDTO;
import com.example.json_ex.productsShop.services.ProductsService;
import com.example.json_ex.productsShop.services.SeedService;
import com.example.json_ex.productsShop.services.UserService;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
public class ProductShopRunner implements CommandLineRunner {

    private final SeedService seedService;
    private final ProductsService productsService;
    private final UserService userService;

    private final Gson gson;

    @Autowired
    public ProductShopRunner(SeedService seedService, ProductsService productsService, UserService userService) {
        this.seedService = seedService;
        this.productsService = productsService;
        this.userService = userService;

        this.gson = new GsonBuilder()
                .setPrettyPrinting()
                .create();
    }

    @Override
    public void run(String... args) throws Exception {
//        this.seedService.seedAll();


        // 01
//        List<ProductWithoutBuyerDTO> productsForSell = this.productsService.getProductsInPriceRangeForSell(500, 1000);
//        String json = this.gson.toJson(productsForSell);
//
//        System.out.println(json);


        // 02
//        List<UsersWithSoldProductsDTO> usersWithSoldProducts = this.userService.getAllWithSoldProducts();
//        String json = this.gson.toJson(usersWithSoldProducts);
//        System.out.println(json);


//         03
//        List<CategoryStatsDTO> allCategoriesOrderedByNumberOfProducts =
//                this.productsService.getAllCategoriesOrderedByNumberOfProducts();
//
//        String json = this.gson.toJson(allCategoriesOrderedByNumberOfProducts);
//        System.out.println(json);


        // 04
//        this.userService.getAllWithSoldProductsOrderByCount();
    //    not working
    }
}
