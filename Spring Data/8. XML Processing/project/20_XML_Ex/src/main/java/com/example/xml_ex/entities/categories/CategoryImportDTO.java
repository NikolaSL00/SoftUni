package com.example.xml_ex.entities.categories;

import javax.xml.bind.annotation.*;
import java.util.List;

@XmlRootElement(name = "categories")
@XmlAccessorType(XmlAccessType.FIELD)
public class CategoryImportDTO {

    @XmlElement(name = "category")
    List<CategoryNameDTO> categories;

    public CategoryImportDTO() {
    }

    public List<CategoryNameDTO> getCategories() {
        return categories;
    }
}
