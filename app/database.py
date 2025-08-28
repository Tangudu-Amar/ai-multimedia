import mysql.connector
from mysql.connector import Error, InterfaceError
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_db_connection():
    """
    Establishes and returns a connection to the MySQL database.
    Returns None if the connection fails.
    """
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", ""),
            database=os.getenv("DB_NAME", "multimedia_app")
        )
        if connection.is_connected():
            print("✅ Successfully connected to the database.")
            return connection
    except InterfaceError as ie:
        print("❌ Could not connect to MySQL server.")
        print(f"InterfaceError: {ie}")
    except Error as e:
        print("❌ MySQL error occurred.")
        print(f"MySQLError: {e}")
    return None