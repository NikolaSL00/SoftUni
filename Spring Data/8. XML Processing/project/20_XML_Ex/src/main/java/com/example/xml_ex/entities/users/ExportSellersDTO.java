package com.example.xml_ex.entities.users;

import org.springframework.data.annotation.AccessType;

import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;
import java.util.List;

@XmlRootElement(name = "users")
@AccessType(AccessType.Type.FIELD)
public class ExportSellersDTO {

    @XmlElement(name = "user")
    private List<ExportUserWithSoldProductsDTO> users;

    public ExportSellersDTO() {
    }

    public ExportSellersDTO(List<ExportUserWithSoldProductsDTO> users) {
        this.users = users;
    }
    
}
