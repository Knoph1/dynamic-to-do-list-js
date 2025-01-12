import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establish the connection to the MySQL server
        connection = mysql.connector.connect(
            host='localhost',  # or the IP address of your MySQL server
            user='root',  # or your MySQL username
            password='your_password'  # replace with your MySQL root password
        )

        if connection.is_connected():
            # Create a cursor to execute the SQL query
            cursor = connection.cursor()

            # Check if the database exists, and if not, create it
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            # Commit changes
            connection.commit()

            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        # Handle any errors during connection or execution
        print(f"Error: {e}")

    finally:
        # Ensure the connection is closed
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

# Run the function to create the database
if __name__ == "__main__":
    create_database()
