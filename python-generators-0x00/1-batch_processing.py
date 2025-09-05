#!/usr/bin/python3
import mysql.connector

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = ''
DB_NAME = 'ALX_prodev'


def stream_users_in_batches(batch_size):
    """
    Generator that fetches rows from the user_data table in batches using yield.
    """
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = connection.cursor(dictionary=True)
        offset = 0

        while True:
            # Explicitly using FROM user_data
            cursor.execute(
                f"SELECT * FROM user_data LIMIT {batch_size} OFFSET {offset}"
            )
            batch = cursor.fetchall()
            if not batch:
                break
            yield batch  # use yield, not return
            offset += batch_size

    except mysql.connector.Error as err:
        print(f"Database error: {err}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def batch_processing(batch_size):
    """
    Processes each batch and prints users over age 25.
    """
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                print(user)
