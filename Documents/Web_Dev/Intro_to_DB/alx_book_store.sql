-- Create the database
CREATE DATABASE alx_book_store;
USE alx_book_store;

-- Create Authors table
CREATE TABLE Authors (
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    author_name VARCHAR(215) NOT NULL
);

-- Create Books table
CREATE TABLE Books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(130) NOT NULL,
    author_id INT,
    price DOUBLE,
    publication_date DATE,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id)
);

-- Create Customers table
CREATE TABLE Customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(215) NOT NULL,
    email VARCHAR(215) NOT NULL,
    address TEXT
);

-- Create Orders table
CREATE TABLE Orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

-- Create Order_Details table
CREATE TABLE Order_Details (
    orderdetailid INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    book_id INT,
    quantity DOUBLE,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
);

-- Example data insertions (optional)
INSERT INTO Authors (author_name) VALUES ('John Doe');
INSERT INTO Books (title, author_id, price, publication_date) 
VALUES ('Learn SQL', 1, 29.99, '2025-01-10');

-- CRUD operations examples:

-- Insert a new customer
INSERT INTO Customers (customer_name, email, address) 
VALUES ('Alice Smith', 'alice@example.com', '123 Main St');

-- Create a new order
INSERT INTO Orders (customer_id, order_date) 
VALUES (1, '2025-01-12');

-- Insert order details for the order
INSERT INTO Order_Details (order_id, book_id, quantity) 
VALUES (1, 1, 2);

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
