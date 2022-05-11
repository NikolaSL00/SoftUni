package com.example.advquerying.services;

import com.example.advquerying.entities.Ingredient;

import java.util.List;

public interface IngredientService {
    List<Ingredient> selectNameStartsWith(String letter);

    List<Ingredient> selectInNames(List<String> list);

    int deleteByName(String name);

    void increasePriceByPercentage(double percentage);

    void updatePriceByIngredietntsIn(List<String> apple, double v);
}
