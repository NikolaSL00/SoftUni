package com.example.advquerying.services;

import com.example.advquerying.entities.Ingredient;
import com.example.advquerying.repositories.IngredientRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.math.BigDecimal;
import java.util.List;

@Service
public class IngredientServiceImpl implements IngredientService {

    private final IngredientRepository ingredientRepository;

    @Autowired
    public IngredientServiceImpl(IngredientRepository ingredientRepository) {
        this.ingredientRepository = ingredientRepository;
    }


    @Override
    public List<Ingredient> selectNameStartsWith(String letter) {
        return this.ingredientRepository.findByNameStartingWith(letter);
    }

    @Override
    public List<Ingredient> selectInNames(List<String> list) {
        return this.ingredientRepository.findByNameInOrderByPriceAsc(list);
    }

    @Override
    @Transactional
    public int deleteByName(String name) {
        return this.ingredientRepository.deleteByName(name);
    }

    @Transactional
    @Override
    public void increasePriceByPercentage(double percentage) {
        BigDecimal actualPercent = BigDecimal.valueOf(percentage);
        this.ingredientRepository.increasePriceByPercent(actualPercent);
    }

    @Override
    @Transactional
    public void updatePriceByIngredietntsIn(List<String> apple, double v) {
        BigDecimal actualValue = BigDecimal.valueOf(v);
        this.ingredientRepository.uptadePriceByIngredientsIn(apple,actualValue);
    }
}
