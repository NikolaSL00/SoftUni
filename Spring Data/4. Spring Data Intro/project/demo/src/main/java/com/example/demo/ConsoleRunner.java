package com.example.demo;

import com.example.demo.entities.Author;
import com.example.demo.entities.Book;
import com.example.demo.repositories.AuthorRepository;
import com.example.demo.repositories.BooksRepository;
import com.example.demo.services.SeedService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

import java.time.LocalDate;
import java.util.Comparator;
import java.util.List;

@Component
public class ConsoleRunner implements CommandLineRunner {

    private final SeedService seedService;
    private final BooksRepository bookRepository;
    private final AuthorRepository authorRepository;

    @Autowired
    public ConsoleRunner(SeedService seedService,
                         BooksRepository bookRepository,
                         AuthorRepository authorRepository) {
        this.seedService = seedService;
        this.bookRepository = bookRepository;
        this.authorRepository = authorRepository;
    }

    private void _01_booksAfter2000() {
        LocalDate year2000 = LocalDate.of(2000, 1, 1);

        List<Book> books = this.bookRepository.findByReleaseDateAfter(year2000);

        books.forEach(e -> System.out.println(e.getTitle()));
    }

    private void _02_authorsWithAtLeastOneBookBefore1990() {
        LocalDate year1990 = LocalDate.of(1990, 1, 1);

        List<Author> authors = this.authorRepository.findDistinctByBooksReleaseDateBefore(year1990);

        authors.forEach(e -> System.out.println(e.getFirstName() + " " + e.getLastName()));
    }

    private void _03_allAuthorsOrderedByBookCount() {
        List<Author> authors = this.authorRepository.findAll();

        authors
                .stream()
                .sorted((l , r) -> r.getBooks().size() - l.getBooks().size())
                .forEach(e -> System.out.println(e.getFirstName() + " " + e.getLastName()  + " -> " + e.getBooks().size()));
    }

    @Override
    public void run(String... args) throws Exception {
        // this.seedService.seedAll();
        // this._01_booksAfter2000();
        // this._02_authorsWithAtLeastOneBookBefore1990();
        // this._03_allAuthorsOrderedByBookCount();
    }




}
