package com.example.json_ex.productsShop.entities.categories;

import java.math.BigDecimal;

public class CategoryStatsDTO {
    private String category;
    private long productCount;
    private double averagePrice;
    private BigDecimal totalRevenue;

    public CategoryStatsDTO(String category, long count, double averagePrice, BigDecimal totalRevenue) {
        this.category = category;
        this.productCount = count;
        this.averagePrice = averagePrice;
        this.totalRevenue = totalRevenue;
    }

    public String getCategory() {
        return category;
    }

    public long getCount() {
        return productCount;
    }

    public double getAveragePrice() {
        return averagePrice;
    }

    public BigDecimal getTotalRevenue() {
        return totalRevenue;
    }
}
