USE sgm3pm_db;

SELECT 
    books.title,
    books.genre,
    books.publish_year,
    authors.first_name,
    authors.last_name
FROM books
JOIN authors ON books.author_id = authors.author_id
WHERE books.genre = 'Fiction';
