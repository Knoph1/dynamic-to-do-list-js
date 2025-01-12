-- Check if database exists and drop if necessary
DROP DATABASE IF EXISTS alx_book_store;

-- Create the database
CREATE DATABASE alx_book_store;
USE alx_book_store;

-- Check if Authors table exists, if not, create it
CREATE TABLE IF NOT EXISTS Authors (
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    author_name VARCHAR(215) NOT NULL
);

-- Check if Books table exists, if not, create it
CREATE TABLE IF NOT EXISTS Books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(130) NOT NULL,
    author_id INT,
    price DOUBLE,
    publication_date DATE,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id) ON DELETE CASCADE
);

-- Check if Customers table exists, if not, create it
CREATE TABLE IF NOT EXISTS Customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(215) NOT NULL,
    email VARCHAR(215) NOT NULL,
    address TEXT
);

-- Check if Orders table exists, if not, create it
CREATE TABLE IF NOT EXISTS Orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE
);

-- Check if Order_Details table exists, if not, create it
CREATE TABLE IF NOT EXISTS Order_Details (
    orderdetailid INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    book_id INT,
    quantity DOUBLE,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (book_id) REFERENCES Books(book_id) ON DELETE CASCADE
);

-- Check if there are any records in Authors table, if not, add some default data
INSERT INTO Authors (author_name)
SELECT 'John Doe' WHERE NOT EXISTS (SELECT 1 FROM Authors WHERE author_name = 'John Doe');

-- Check if there are any records in Books table, if not, add some default data
INSERT INTO Books (title, author_id, price, publication_date)
SELECT 'Learn SQL', 1, 29.99, '2025-01-10'
WHERE NOT EXISTS (SELECT 1 FROM Books WHERE title = 'Learn SQL');

-- Check if there are any records in Customers table, if not, add some default data
INSERT INTO Customers (customer_name, email, address)
SELECT 'Alice Smith', 'alice@example.com', '123 Main St'
WHERE NOT EXISTS (SELECT 1 FROM Customers WHERE email = 'alice@example.com');

-- Check if there are any records in Orders table, if not, add some default data
INSERT INTO Orders (customer_id, order_date)
SELECT 1, '2025-01-12'
WHERE NOT EXISTS (SELECT 1 FROM Orders WHERE customer_id = 1);

-- Check if there are any records in Order_Details table, if not, add some default data
INSERT INTO Order_Details (order_id, book_id, quantity)
SELECT 1, 1, 2
WHERE NOT EXISTS (SELECT 1 FROM Order_Details WHERE order_id = 1 AND book_id = 1);

-- Read data (select all books)
SELECT * FROM Books;

-- Update a book's price
UPDATE Books
SET price = 24.99
WHERE book_id = 1;

-- Delete a book
DELETE FROM Books
WHERE book_id = 1;

-- Example subquery: Select books by a specific author
SELECT book_id, title
FROM Books
WHERE author_id IN (SELECT author_id FROM Authors WHERE author_name = 'John Doe');

-- Using a MySQL function: Format publication date
SELECT title, DATE_FORMAT(publication_date, '%M %d, %Y') AS formatted_date
FROM Books;
