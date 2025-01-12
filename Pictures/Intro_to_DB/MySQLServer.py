import mysql.connector # type: ignore
from mysql.connector import Error # type: ignore

def create_database():
    try:
        # Establish connection to MySQL Server
        connection = mysql.connector.connect(
            host='localhost',  # Adjust as needed for your MySQL setup
            user='root',       # Your MySQL username
            password='your_password'  # Your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Attempt to create the database
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
        else:
            print("Failed to connect to MySQL server.")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    
    finally:
        # Close the cursor and connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

# Call the function to create the database
create_database()
