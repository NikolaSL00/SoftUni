package com.example.xml_ex;

import com.example.xml_ex.entities.products.ExportProductsInRangeDTO;
import com.example.xml_ex.entities.users.ExportSellersDTO;
import com.example.xml_ex.entities.users.ExportSellersWithCountsDTO;
import com.example.xml_ex.services.ProductsService;
import com.example.xml_ex.services.SeedService;
import com.example.xml_ex.services.UserService;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

import javax.xml.bind.JAXBContext;
import javax.xml.bind.Marshaller;

@Component
public class ProductShopRunner implements CommandLineRunner {

    private final SeedService seedService;
    private final ProductsService productsService;
    private final UserService userService;

    @Autowired
    public ProductShopRunner(SeedService seedService, ProductsService productsService, UserService userService) {
        this.seedService = seedService;
        this.productsService = productsService;
        this.userService = userService;
    }

    @Override
    public void run(String... args) throws Exception {
//        this.seedService.seedAll();

        // 01
//        ExportProductsInRangeDTO productsInRange = this.productsService.getProductsWithNoBuyerInPriceRangeBetweenDesc(500, 1000);
//        JAXBContext context = JAXBContext.newInstance(ExportProductsInRangeDTO.class);
//        Marshaller marshaller = context.createMarshaller();
//        marshaller.setProperty(Marshaller.JAXB_FORMATTED_OUTPUT, true);
//
//        marshaller.marshal(productsInRange, System.out);


        // 02
//        ExportSellersDTO result = this.userService.findAllWithSoldProducts();
//        JAXBContext context = JAXBContext.newInstance(ExportSellersDTO.class);
//
//        Marshaller marshaller = context.createMarshaller();
//        marshaller.setProperty(Marshaller.JAXB_FORMATTED_OUTPUT, true);
//
//        marshaller.marshal(result, System.out);

        // 04
//        ExportSellersWithCountsDTO dto = this.userService.findAllWithSoldProductsAndCounts();
//
//        Gson gson = new GsonBuilder()
//                .setPrettyPrinting()
//                .serializeNulls()
//                .create();
//
//        String result = gson.toJson(dto);
//
//        System.out.println(result);
    }

}
