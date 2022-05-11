package com.example.springintro.repository;

import com.example.springintro.model.entity.AgeRestriction;
import com.example.springintro.model.entity.Book;
import com.example.springintro.model.entity.BookSummary;
import com.example.springintro.model.entity.EditionType;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;
import org.springframework.transaction.annotation.Transactional;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.util.List;

@Repository
public interface BookRepository extends JpaRepository<Book, Long> {

    List<Book> findAllByReleaseDateAfter(LocalDate releaseDateAfter);

    List<Book> findAllByReleaseDateBefore(LocalDate releaseDateBefore);

    List<Book> findAllByAuthor_FirstNameAndAuthor_LastNameOrderByReleaseDateDescTitle(String author_firstName, String author_lastName);

    @Query("SELECT book.title FROM Book book " +
            "WHERE book.ageRestriction = :realAgeRestriction")
    List<String> findTitleByAgeRestrictionEquals(AgeRestriction realAgeRestriction);

    @Query("SELECT b.title FROM Book b " +
            "WHERE b.editionType = :edition " +
            "AND b.copies < :copies")
    List<String> findTitlesByEditionAndCopies(EditionType edition, int copies);

    List<Book> findAllBooksByPriceLessThanOrPriceGreaterThan(BigDecimal lowerBound, BigDecimal upperBound);


    List<Book> findAllBooksByReleaseDateBeforeOrReleaseDateAfter(LocalDate lowerBound, LocalDate upperBound);

    List<Book> findByTitleContaining(String search);

    List<Book> findByAuthorLastNameStartingWith(String namePart);

    @Query("SELECT count(b) FROM Book b " +
            "WHERE length(b.title) > :length")
    int countBooksWithTitleLongerThan(int length);

    @Query("SELECT b.title AS title, b.editionType AS editionType, b.ageRestriction AS ageRestriction, b.price AS price " +
            "FROM Book b " +
            "WHERE b.title = :title")
    BookSummary findSummaryForTitle(String title);

    @Query("UPDATE Book b SET b.copies = b.copies + :amount WHERE b.releaseDate > :after")
    @Modifying
    @Transactional
    int addCopiesToBooksAfter(LocalDate after, int amount);

    @Transactional
    int deleteByCopiesLessThan(int amount);
}
