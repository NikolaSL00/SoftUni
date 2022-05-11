package com.example.json_ex.productsShop.services;

import com.example.json_ex.productsShop.entities.categories.CategoryStatsDTO;
import com.example.json_ex.productsShop.entities.products.ProductWithoutBuyerDTO;
import org.springframework.stereotype.Service;

import java.math.BigDecimal;
import java.util.List;

public interface ProductsService {
    List<ProductWithoutBuyerDTO> getProductsInPriceRangeForSell(
            float from, float to);

    List<CategoryStatsDTO> getAllCategoriesOrderedByNumberOfProducts();

}
