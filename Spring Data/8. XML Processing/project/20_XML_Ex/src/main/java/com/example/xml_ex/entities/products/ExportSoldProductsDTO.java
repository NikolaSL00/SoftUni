package com.example.xml_ex.entities.products;

import java.util.List;

public class ExportSoldProductsDTO {

    private int count;

    private List<ExportNamePriceProductDTO> products;

    public ExportSoldProductsDTO(List<ExportNamePriceProductDTO> products) {
        this.products = products;

        this.count = this.products.size();
    }

    public int getCount() {
        return count;
    }

    public List<ExportNamePriceProductDTO> getProducts() {
        return products;
    }
}
