package com.example.workshop1.model.dto;

import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlAttribute;
import javax.xml.bind.annotation.XmlRootElement;
import java.io.Serializable;

@XmlRootElement(name = "company")
@XmlAccessorType(XmlAccessType.FIELD)
public class ImportCompanyDTO implements Serializable {

    @XmlAttribute
    private String name;

    public ImportCompanyDTO() {
    }

    public String getName() {
        return name;
    }
}
