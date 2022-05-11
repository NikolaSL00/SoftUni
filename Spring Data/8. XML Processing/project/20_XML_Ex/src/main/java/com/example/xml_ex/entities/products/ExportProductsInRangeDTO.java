package com.example.xml_ex.entities.products;

import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;
import java.util.List;

@XmlRootElement(name = "products")
@XmlAccessorType(XmlAccessType.FIELD)
public class ExportProductsInRangeDTO {

    @XmlElement(name = "product")
    private List<ProductsWithAttributesDTO> products;

    public ExportProductsInRangeDTO() {
    }

    public ExportProductsInRangeDTO(List<ProductsWithAttributesDTO> products) {
        this.products = products;
    }
}
