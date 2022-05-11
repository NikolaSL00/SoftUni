package com.example.advquerying.repositories;

import com.example.advquerying.entities.Ingredient;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import java.math.BigDecimal;
import java.util.List;

public interface IngredientRepository extends JpaRepository<Ingredient, Integer> {
    List<Ingredient> findByNameStartingWith(String letter);

    List<Ingredient> findByNameInOrderByPriceAsc(List<String> list);

    int deleteByName(String name);

    @Query("UPDATE Ingredient i " +
            "SET i.price = i.price + i.price * :multiplier")
    @Modifying
    void increasePriceByPercent(@Param("multiplier") BigDecimal percentage);

    @Query("UPDATE Ingredient i "+
            "SET i.price = i.price + :value " +
            "WHERE i.name in :ingredientList")
    @Modifying
    void uptadePriceByIngredientsIn(@Param("ingredientList") List<String> ingredientsList, @Param("value") BigDecimal actualValue);
}
