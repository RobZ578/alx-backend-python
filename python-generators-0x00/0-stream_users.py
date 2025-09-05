#!/usr/bin/python3
import mysql.connector

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = ''
DB_NAME = 'ALX_prodev'
TABLE_NAME = 'user_data'


def stream_users():
    """
    Generator function that yields one user row at a time from user_data table.
    """
    try:
        # Connect to the database
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM {TABLE_NAME}")

        # Yield each row one by one
        for row in cursor:
            yield row

    except mysql.connector.Error as err:
        print(f"Database error: {err}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
