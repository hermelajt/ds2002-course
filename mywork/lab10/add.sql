USE sgm3pm_db;

INSERT INTO authors (author_id, first_name, last_name, country, birth_year) VALUES
(11, 'George', 'Orwell', 'United Kingdom', 1903),
(12, 'F. Scott', 'Fitzgerald', 'United States', 1896);

INSERT INTO books (book_id, title, genre, publish_year, author_id) VALUES
(111, '1984', 'Dystopian', 1949, 11),
(112, 'Animal Farm', 'Political Satire', 1945, 11),
(113, 'The Great Gatsby', 'Fiction', 1925, 12);
