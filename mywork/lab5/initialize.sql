
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;

CREATE TABLE authors (
    author_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    country VARCHAR(50),
    birth_year INT
);

CREATE TABLE books (
    book_id INT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    genre VARCHAR(50),
    publish_year INT,
    author_id INT,
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);

INSERT INTO authors (author_id, first_name, last_name, country, birth_year) VALUES
(1, 'Jane', 'Austen', 'United Kingdom', 1775),
(2, 'Mark', 'Twain', 'United States', 1835),
(3, 'Chinua', 'Achebe', 'Nigeria', 1930),
(4, 'Haruki', 'Murakami', 'Japan', 1949),
(5, 'Isabel', 'Allende', 'Chile', 1942),
(6, 'Toni', 'Morrison', 'United States', 1931),
(7, 'Leo', 'Tolstoy', 'Russia', 1828),
(8, 'Mary', 'Shelley', 'United Kingdom', 1797),
(9, 'Gabriel', 'Marquez', 'Colombia', 1927),
(10, 'Jhumpa', 'Lahiri', 'United States', 1967);

INSERT INTO books (book_id, title, genre, publish_year, author_id) VALUES
(101, 'Pride and Prejudice', 'Romance', 1813, 1),
(102, 'Adventures of Huckleberry Finn', 'Fiction', 1884, 2),
(103, 'Things Fall Apart', 'Historical Fiction', 1958, 3),
(104, 'Norwegian Wood', 'Fiction', 1987, 4),
(105, 'The House of the Spirits', 'Magical Realism', 1982, 5),
(106, 'Beloved', 'Historical Fiction', 1987, 6),
(107, 'War and Peace', 'Historical Fiction', 1869, 7),
(108, 'Frankenstein', 'Gothic Fiction', 1818, 8),
(109, 'One Hundred Years of Solitude', 'Magical Realism', 1967, 9),
(110, 'The Namesake', 'Fiction', 2003, 10);
>>>>>>> 9086c01 (Lab 5 complete)
