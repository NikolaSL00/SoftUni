package com.example.xml_ex.services;

import com.example.xml_ex.entities.products.ProductsWithAttributesDTO;
import com.example.xml_ex.entities.products.Product;
import com.example.xml_ex.entities.products.ExportProductsInRangeDTO;
import com.example.xml_ex.entities.users.User;
import com.example.xml_ex.repositories.ProductRepository;
import org.modelmapper.Converter;
import org.modelmapper.ModelMapper;
import org.modelmapper.TypeMap;
import org.modelmapper.spi.MappingContext;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.math.BigDecimal;
import java.util.List;
import java.util.stream.Collectors;


@Service
public class ProductsServiceImpl implements ProductsService {

    private final ModelMapper mapper;
    private final ProductRepository productRepository;
    private final TypeMap<Product, ProductsWithAttributesDTO> productToDtoMapping;

    @Autowired
    public ProductsServiceImpl(ProductRepository productRepository) {
        this.productRepository = productRepository;
        this.mapper = new ModelMapper();

        // Seller -> firstName + lastName
        // source is User, destination is String
        Converter<User, String> userToFullNameConverter =
                context ->
                        context.getSource() == null
                                ? null
                                : context.getSource().getFullName();

        TypeMap<Product, ProductsWithAttributesDTO> typeMap =
                this.mapper.createTypeMap(Product.class, ProductsWithAttributesDTO.class);

        this.productToDtoMapping = typeMap.addMappings(map ->
                map.using(userToFullNameConverter)
                        .map(Product::getSeller, ProductsWithAttributesDTO::setSeller));

    }

    @Override
    public ExportProductsInRangeDTO getProductsWithNoBuyerInPriceRangeBetweenDesc(float from, float to) {
        BigDecimal lowerBound = BigDecimal.valueOf(from);
        BigDecimal upperBound = BigDecimal.valueOf(to);

        List<Product> products = this.productRepository
                .findAllByPriceBetweenAndBuyerIsNullOrderByPriceDesc(lowerBound, upperBound);

        List<ProductsWithAttributesDTO> dtos = products
                .stream()
//                .map(product -> this.mapper.map(product, ProductsWithAttributesDTO.class))
                .map(this.productToDtoMapping::map)
                .collect(Collectors.toList());

        return new ExportProductsInRangeDTO(dtos);
    }
}
