package com.example.xml_ex.services;


import com.example.xml_ex.entities.users.ExportSellersDTO;
import com.example.xml_ex.entities.users.ExportSellersWithCountsDTO;

public interface UserService {
   ExportSellersDTO findAllWithSoldProducts();

   ExportSellersWithCountsDTO findAllWithSoldProductsAndCounts();
}
