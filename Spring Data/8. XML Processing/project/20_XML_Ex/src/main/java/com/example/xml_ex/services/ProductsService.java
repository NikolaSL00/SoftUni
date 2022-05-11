package com.example.xml_ex.services;

import com.example.xml_ex.entities.products.ExportProductsInRangeDTO;

public interface ProductsService {
    ExportProductsInRangeDTO getProductsWithNoBuyerInPriceRangeBetweenDesc(float from, float to);
}
