package exam.model;

import org.springframework.data.annotation.AccessType;

import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;

@XmlRootElement(name = "")
@AccessType(AccessType.Type.FIELD)
public class ImportTownDTO {
    @XmlElement
    private String name;

    @XmlElement
    private int population;

    @XmlElement(name = "travel-guide")
    private String travelGuide;

    public ImportTownDTO() {
    }

    public String getName() {
        return name;
    }

    public int getPopulation() {
        return population;
    }

    public String getTravelGuide() {
        return travelGuide;
    }

    public boolean isValid() {
        if(this.name.length() < 2){
            return false;
        }

        if(this.population < 1){
            return false;
        }

        if(this.travelGuide.length() < 10){
            return false;
        }

        return true;
    }
}
