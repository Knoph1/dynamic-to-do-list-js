import mysql.connector
from mysql.connector import errorcode
import config

def create_database():
    connection = None
    cursor = None
    try:
        # Establish connection to MySQL server using credentials from config.py
        connection = mysql.connector.connect(
            host=config.DB_HOST,
            user=config.DB_USER,
            password=config.DB_PASSWORD
        )
        cursor = connection.cursor()

        # Create database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(f"Error: {err}")
    finally:
        # Close cursor and connection safely
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

# Call the function to create the database
if __name__ == "__main__":
    create_database()
