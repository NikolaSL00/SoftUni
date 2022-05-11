package com.example.advquerying.services;

import com.example.advquerying.entities.Shampoo;
import com.example.advquerying.entities.Size;

import java.math.BigDecimal;
import java.util.List;


public interface ShampooService {
    List<Shampoo> selectBySize(Size size);

    List<Shampoo> selectBySizeOrLabelId(Size size, long labelId);

    List<Shampoo> selectByPriceHigher(BigDecimal price);

   int countWithPriceLowerThan(BigDecimal price);

    List<Shampoo> findByIngredientsNames(List<String> ingredients);

    List<Shampoo> selectByIngredientsCount(int ingredientsCount);
}
