package com.example.xml_ex.entities.products;

import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;
import java.util.List;

@XmlRootElement(name = "products")
public class ProductImportDTO {

    @XmlElement(name = "product")
    private List<ProductInfoDTO> productList;

    public ProductImportDTO() {
    }

    public List<ProductInfoDTO> getProductList() {
        return productList;
    }
}
