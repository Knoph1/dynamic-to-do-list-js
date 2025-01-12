-- task_5.sql

-- Inserting a single row into the customer table
INSERT INTO customer (customer_id, first_name, last_name, email, address)
VALUES (1, 'Cole', 'Baidoo', 'cbaidoo@sandtech.com', '123 Happiness Ave.');

-- Inserting multiple rows into the customer table
INSERT INTO customer (customer_id, first_name, last_name, email, address)
VALUES 
(2, 'Blessing', 'Malik', 'bmalik@sandtech.com', '124 Happiness Ave.'),
(3, 'Obed', 'Ehoneah', 'eobed@sandtech.com', '125 Happiness Ave.'),
(4, 'Nehemial', 'Kamolu', 'nkamolu@sandtech.com', '126 Happiness Ave.');
