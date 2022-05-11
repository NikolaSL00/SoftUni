package com.example.advquerying.services;

import com.example.advquerying.entities.Label;
import com.example.advquerying.entities.Shampoo;
import com.example.advquerying.entities.Size;
import com.example.advquerying.repositories.ShampooRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.math.BigDecimal;
import java.util.List;
@Service
public class ShampooServiceImpl implements ShampooService {

    @Autowired
    private ShampooRepository shampooRepository;

    @Override
    public List<Shampoo> selectBySize(Size size) {
        return this.shampooRepository.findBySize(size);
    }

    @Override
    public List<Shampoo> selectBySizeOrLabelId(Size size, long labelId) {
        return this.shampooRepository.findBySizeOrLabelIdOrderByPriceAsc(size, labelId);
    }

    @Override
    public List<Shampoo> selectByPriceHigher(BigDecimal price) {
        return this.shampooRepository.findByPriceGreaterThanOrderByPriceDesc(price);
    }

    @Override
    public int countWithPriceLowerThan(BigDecimal price) {
        return this.shampooRepository.countByPriceLessThan(price);
    }

    @Override
    public List<Shampoo> findByIngredientsNames(List<String> ingredients) {
        return this.shampooRepository.findByIngredientsNames(ingredients);
    }

    @Override
    public List<Shampoo> selectByIngredientsCount(int ingredientsCount) {
        return this.shampooRepository.findByIngredientCountLessThan(ingredientsCount);
    }
}
