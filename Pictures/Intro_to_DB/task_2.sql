-- Use the alx_book_store database
USE alx_book_store;

-- Create the Authors table
CREATE TABLE IF NOT EXISTS AUTHORS (
    author_id INT PRIMARY KEY AUTO_INCREMENT,
    author_name VARCHAR(215) NOT NULL
);

-- Create the Books table
CREATE TABLE IF NOT EXISTS BOOKS (
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(130) NOT NULL,
    author_id INT,
    price DOUBLE NOT NULL,
    publication_date DATE,
    FOREIGN KEY (author_id) REFERENCES AUTHORS(author_id)
);

-- Create the Customers table
CREATE TABLE IF NOT EXISTS CUSTOMERS (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_name VARCHAR(215) NOT NULL,
    email VARCHAR(215) NOT NULL,
    address TEXT NOT NULL
);

-- Create the Orders table
CREATE TABLE IF NOT EXISTS ORDERS (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    order_date DATE NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES CUSTOMERS(customer_id)
);

-- Create the Order_Details table
CREATE TABLE IF NOT EXISTS ORDER_DETAILS (
    orderdetailid INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT,
    book_id INT,
    quantity DOUBLE NOT NULL,
    FOREIGN KEY (order_id) REFERENCES ORDERS(order_id),
    FOREIGN KEY (book_id) REFERENCES BOOKS(book_id)
);
