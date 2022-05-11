package com.example.xml_ex.services;

import com.example.xml_ex.entities.categories.Category;
import com.example.xml_ex.entities.categories.CategoryImportDTO;
import com.example.xml_ex.entities.products.Product;
import com.example.xml_ex.entities.products.ProductImportDTO;
import com.example.xml_ex.entities.users.User;
import com.example.xml_ex.entities.users.UserImportDTO;
import com.example.xml_ex.repositories.CategoryRepository;
import com.example.xml_ex.repositories.ProductRepository;
import com.example.xml_ex.repositories.UserRepository;
import org.modelmapper.ModelMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import javax.xml.bind.JAXBContext;
import javax.xml.bind.JAXBException;
import javax.xml.bind.Unmarshaller;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.math.BigDecimal;
import java.util.*;
import java.util.stream.Collectors;

@Service
public class SeedServiceImpl implements SeedService {

    private static final String USERS_XML_PATH = "E:\\Downloads\\SoftUni\\Java\\Spring Data\\8. XML Processing\\project\\20_XML_Ex\\src\\main\\resources\\productshop\\users.xml";
    private static final String CATEGORIES_XML_PATH = "E:\\Downloads\\SoftUni\\Java\\Spring Data\\8. XML Processing\\project\\20_XML_Ex\\src\\main\\resources\\productshop\\categories.xml";
    private static final String PRODUCTS_XML_PATH = "E:\\Downloads\\SoftUni\\Java\\Spring Data\\8. XML Processing\\project\\20_XML_Ex\\src\\main\\resources\\productshop\\products.xml";
    private final UserRepository userRepository;

    private final CategoryRepository categoryRepository;

    private final ModelMapper modelMapper;
    private final ProductRepository productRepository;

    @Autowired
    public SeedServiceImpl(UserRepository userRepository, CategoryRepository categoryRepository, ProductRepository productRepository) {
        this.userRepository = userRepository;
        this.categoryRepository = categoryRepository;
        this.productRepository = productRepository;
        this.modelMapper = new ModelMapper();
    }

    @Override
    public void seedUsers() throws FileNotFoundException, JAXBException {
        JAXBContext context = JAXBContext.newInstance(UserImportDTO.class);
        Unmarshaller unmarshaller = context.createUnmarshaller();

        FileReader xmlReader = new FileReader(USERS_XML_PATH);
        UserImportDTO importDTO = (UserImportDTO) unmarshaller.unmarshal(xmlReader);

        List<User> users = importDTO
                .getUserList()
                .stream()
                .map(userInfo -> new User(userInfo.getFirstName(), userInfo.getLastName(), userInfo.getAge()))
                //.map(userInfo-> this.mapper.map(userInfo, User.clas)
                .collect(Collectors.toList());

        this.userRepository.saveAll(users);
    }

    @Override
    public void seedCategories() throws FileNotFoundException, JAXBException {
        JAXBContext context = JAXBContext.newInstance(CategoryImportDTO.class);
        Unmarshaller unmarshaller = context.createUnmarshaller();

        FileReader xlmReader = new FileReader(CATEGORIES_XML_PATH);
        CategoryImportDTO importDTO = (CategoryImportDTO) unmarshaller.unmarshal(xlmReader);

        List<Category> entities = importDTO
                .getCategories()
                .stream()
                .map(categoryName -> new Category(categoryName.getName()))
                .collect(Collectors.toList());

        this.categoryRepository.saveAll(entities);

    }

    @Override
    public void seedProducts() throws FileNotFoundException, JAXBException {
        JAXBContext context = JAXBContext.newInstance(ProductImportDTO.class);
        Unmarshaller unmarshaller = context.createUnmarshaller();

        FileReader xmlReader = new FileReader(PRODUCTS_XML_PATH);
        ProductImportDTO importDTO = (ProductImportDTO) unmarshaller.unmarshal(xmlReader);

        List<Product> products = importDTO
                .getProductList()
                .stream()
                .map(productInfo -> new Product(productInfo.getName(), productInfo.getPrice()))
                .map(this::setRandomBuyer)
                .map(this::setRandomCategories)
                .map(this::setRandomSeller)
                .collect(Collectors.toList());

        this.productRepository.saveAll(products);
    }

    private Product setRandomCategories(Product product) {

        Random random = new Random();

        long categoriesDbCount = this.categoryRepository.count();
        int count = random.nextInt((int) categoriesDbCount);
        Set<Category> categories = new HashSet<>();

        for (int i = 0; i < count; i++) {
            int randomId = random.nextInt((int) categoriesDbCount) + 1;

            Optional<Category> randomCategory = this.categoryRepository.findById(randomId);

            categories.add(randomCategory.get());
        }

        product.setCategories(categories);
        return product;
    }

    private Product setRandomBuyer(Product product) {
        if (product.getPrice().compareTo(BigDecimal.valueOf(944)) > 0) {
            return product;
        }

        Optional<User> buyer = getRandomUser();

        product.setBuyer(buyer.get());

        return product;
    }

    private Product setRandomSeller(Product product) {
        Optional<User> seller = getRandomUser();

        product.setSeller(seller.get());

        return product;
    }

    private Optional<User> getRandomUser() {
        long usersCount = this.userRepository.count();

        int randomUserId = new Random().nextInt((int) usersCount) + 1;

        Optional<User> buyer = this.userRepository.findById(randomUserId);
        return buyer;
    }
}
