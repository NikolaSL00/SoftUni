package com.example.springintro;

import com.example.springintro.model.entity.Book;
import com.example.springintro.model.entity.BookSummary;
import com.example.springintro.model.entity.EditionType;
import com.example.springintro.service.AuthorService;
import com.example.springintro.service.BookService;
import com.example.springintro.service.CategoryService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

import java.io.IOException;
import java.time.LocalDate;
import java.util.List;
import java.util.Scanner;

@Component
public class CommandLineRunnerImpl implements CommandLineRunner {

    private final CategoryService categoryService;
    private final AuthorService authorService;
    private final BookService bookService;

    @Autowired
    public CommandLineRunnerImpl(CategoryService categoryService, AuthorService authorService, BookService bookService) {
        this.categoryService = categoryService;
        this.authorService = authorService;
        this.bookService = bookService;
    }

    @Override
    public void run(String... args) throws Exception {

        //06
//        this.authorService.findFirstNamesThatEndsWith("e")
//                .forEach(e -> System.out.println(e.getFirstName() + " " + e.getLastName()));


        //07
//        this.bookService.findBookTitlesContaining("WOR")
//                .forEach(System.out::println);

        // 08
//        this.bookService.findByAuthorLastNameStartsWith("Ric")
//                .forEach(b->
//                        System.out.printf("%s (%s %s)%n",
//                        b.getTitle(),
//                        b.getAuthor().getFirstName(),
//                        b.getAuthor().getLastName()));

        // 09
//        int length = 12;
//        System.out.printf("There are %d books with title longer than %d symbols!%n", this.bookService.findBookTitleLongerThan(length), length);

        // 10
//        this.authorService.getWithTotalCopies()
//                .forEach(a -> System.out.println(a.getFirstName() + " " + a.getLastName() + " " + a.getTotalCopies()));


        // 11
//        BookSummary summary = this.bookService.getInformationForTitle("Things Fall Apart");
//
//        System.out.println(summary.getTitle()
//                + " " + summary.getEditionType()
//                + " " + summary.getAgeRestriction() +
//                " " + summary.getPrice());



            // 12
//        int booksUpdated = this.bookService.addCopiesToBooksAfter("12 Oct 2005", 100);
//
//        System.out.printf("%d books are released after %s, so total of %d book copies were added.",
//                booksUpdated, "12 Oct 2005", 100 * booksUpdated);


        //13
//        Scanner scanner = new Scanner(System.in);
//
//        int amount = Integer.parseInt(scanner.nextLine());
//        this.bookService.deleteWithCopiesLessThan(amount);

    }

    private void selectBookTitlesReleasedBefore(String date) {
//        selectBookTitlesReleasedBefore("12-04-1992");

        this.bookService.findBooksReleasedBeforeDate(date)
                .forEach(b -> System.out.printf("%s %s %.2f \n",
                        b.getTitle(),
                        b.getEditionType(),
                        b.getPrice()));
    }

    private void selectBookTitlesNotReleasedIn(int year) {
        this.bookService.selectBookTitlesNotReleasedIn(year)
                .forEach(book -> System.out.println(book.getTitle() + " - " + book.getReleaseDate()));
    }

    private void selectBooksWithPriceNotBetween(double lowerBound, double upperBound) {
        this.bookService.selectBooksWithPriceNotBetween(lowerBound, upperBound)
                .forEach(book -> System.out.println(book.getTitle() + " - " + book.getPrice()));
    }

    private void selectTitlesByEditionAndCopies(List<String> bookService) {
        bookService
                .forEach(System.out::println);
    }

    private void printALlBooksByAuthorNameOrderByReleaseDate(String firstName, String lastName) {
        bookService
                .findAllBooksByAuthorFirstAndLastNameOrderByReleaseDate(firstName, lastName)
                .forEach(System.out::println);
    }

    private void printAllAuthorsAndNumberOfTheirBooks() {
        authorService
                .getAllAuthorsOrderByCountOfTheirBooks()
                .forEach(System.out::println);
    }

    private void printAllAuthorsNamesWithBooksWithReleaseDateBeforeYear(int year) {
        bookService
                .findAllAuthorsWithBooksWithReleaseDateBeforeYear(year)
                .forEach(System.out::println);
    }

    private void printAllBooksAfterYear(int year) {
        bookService
                .findAllBooksAfterYear(year)
                .stream()
                .map(Book::getTitle)
                .forEach(System.out::println);
    }

    private void seedData() throws IOException {
        categoryService.seedCategories();
        authorService.seedAuthors();
        bookService.seedBooks();
    }

    private void selectTitlesByAgeRestrictionType() {
        Scanner scanner = new Scanner(System.in);
        String restriction = scanner.nextLine();

        this.bookService.selectBooksByAgeRestrictionEquals(restriction)
                .forEach(System.out::println);
    }
}
