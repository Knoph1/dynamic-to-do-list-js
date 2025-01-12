-- Use the alx_book_store database
USE alx_book_store;

-- Query to get the description of the 'Books' table 
-- without using DESCRIBE or EXPLAIN
SELECT 
  COLUMN_NAME AS 'Column Name', 
  COLUMN_TYPE AS 'Data Type', 
  IS_NULLABLE AS 'Is Nullable', 
  COLUMN_KEY AS 'Key', 
  COLUMN_DEFAULT AS 'Default Value', 
  EXTRA AS 'Extra Information'
FROM 
  INFORMATION_SCHEMA.COLUMNS
WHERE 
  TABLE_SCHEMA = 'alx_book_store'
  AND TABLE_NAME = 'Books';
