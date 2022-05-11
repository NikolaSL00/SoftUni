package com.example.springintro.service;

import com.example.springintro.model.entity.Book;
import com.example.springintro.model.entity.BookSummary;
import com.example.springintro.model.entity.EditionType;

import java.io.IOException;
import java.time.LocalDate;
import java.util.List;

public interface BookService {
    void seedBooks() throws IOException;

    List<Book> findAllBooksAfterYear(int year);

    List<String> findAllAuthorsWithBooksWithReleaseDateBeforeYear(int year);

    List<String> findAllBooksByAuthorFirstAndLastNameOrderByReleaseDate(String firstName, String lastName);

    List<String> selectBooksByAgeRestrictionEquals(String ageRestriction);

    List<String> selectTitlesByEditionAndCopies(EditionType edition, int copies);

    List<Book> selectBooksWithPriceNotBetween(double lowerBound, double upperBound);

    List<Book> selectBookTitlesNotReleasedIn(int year);

    List<Book> findBooksReleasedBeforeDate(String date);

    List<String> findBookTitlesContaining(String search);

    List<Book> findByAuthorLastNameStartsWith(String namePart);

    int findBookTitleLongerThan(int length);

    BookSummary getInformationForTitle(String title);

    int addCopiesToBooksAfter(String date, int amount);

    int deleteWithCopiesLessThan(int amount);
}
