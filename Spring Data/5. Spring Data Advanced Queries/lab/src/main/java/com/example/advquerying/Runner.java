package com.example.advquerying;

import com.example.advquerying.services.IngredientService;
import com.example.advquerying.services.ShampooService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;
import com.example.advquerying.repositories.ShampooRepository;
import org.springframework.transaction.annotation.Transactional;

import java.math.BigDecimal;
import java.util.List;
import java.util.Scanner;
import java.util.Set;


@Component
public class Runner implements CommandLineRunner {

    private final ShampooRepository shampooRepository;

    private final ShampooService shampooService;

    private final IngredientService ingredientService;

    @Autowired
    public Runner(ShampooRepository shampooRepository, ShampooService shampooService, IngredientService ingredientService) {
        this.shampooRepository = shampooRepository;
        this.shampooService = shampooService;
        this.ingredientService = ingredientService;
    }


    public void run(String... args) {
        //_01_ShampoosByIngredients();
//        this.shampooService.selectBySize(Size.MEDIUM)
//                .forEach(System.out::println);

//        this.shampooService.selectBySizeOrLabelId(Size.MEDIUM, 10)
//                .forEach(System.out::println);

//        this.shampooService.selectByPriceHigher(BigDecimal.valueOf(9))
//                .forEach(System.out::println);

//        this.ingredientService.selectNameStartsWith("M")
//                .forEach(System.out::println);

//        this.ingredientService.selectInNames(List.of("Lavender", "Apple", "Herbs"))
//                .forEach(System.out::println);

//        int count = this.shampooService.countWithPriceLowerThan(BigDecimal.valueOf(8.50));
//        System.out.println(count);

//        this.shampooService.findByIngredientsNames(List.of("Berry", "Mineral-Collagen"))
//                .forEach(System.out::println);

//        this.shampooService.selectByIngredientsCount(2)
//                .forEach(System.out::println);

//        this.ingredientService.deleteByName("Nettle");

//        this.ingredientService.increasePriceByPercentage(0.1);

        this.ingredientService.updatePriceByIngredietntsIn(List.of("Apple", "Nettle"), -0.30);
    }
}
