package com.example.advquerying.repositories;

import com.example.advquerying.entities.Ingredient;
import com.example.advquerying.entities.Shampoo;
import com.example.advquerying.entities.Size;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.math.BigDecimal;
import java.util.List;
import java.util.Set;

@Repository
public interface ShampooRepository extends JpaRepository<Shampoo, Long> {

    List<Shampoo> findAllByBrand(String brand);

    List<Shampoo> findAllByBrandAndSize(String brand, Size size);

    List<Shampoo> findBySizeOrderById(Size size);

    @Query("SELECT s FROM Shampoo s " +
            "JOIN s.ingredients AS ingr " +
            "WHERE ingr.name IN :ingredients")
    List<Shampoo> findByIngredientsNames(
            @Param("ingredients") List<String> ingredientNames);

    List<Shampoo> findBySize(Size size);

    List<Shampoo> findBySizeOrLabelIdOrderByPriceAsc(Size size, long labelId);

    List<Shampoo> findByPriceGreaterThanOrderByPriceDesc(BigDecimal price);

    int countByPriceLessThan(BigDecimal price);

    @Query("SELECT s FROM Shampoo s " +
            "WHERE s.ingredients.size < :ingrCount")
    List<Shampoo> findByIngredientCountLessThan(@Param("ingrCount") int ingredientsCount);
}
