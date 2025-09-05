#!/usr/bin/python3
import mysql.connector
import csv
import uuid

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = ''  # change if you have a password
DB_NAME = 'ALX_prodev'
TABLE_NAME = 'user_data'


def connect_db():
    """Connects to the MySQL server (without specifying a database)."""
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


def create_database(connection):
    """Creates ALX_prodev database if it doesn't exist."""
    cursor = connection.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    cursor.close()
    print(f"Database {DB_NAME} checked/created successfully.")


def connect_to_prodev():
    """Connects to the ALX_prodev database."""
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


def create_table(connection):
    """Creates user_data table if it does not exist."""
    cursor = connection.cursor()
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            user_id CHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL NOT NULL,
            INDEX(user_id)
        )
    """)
    cursor.close()
    print(f"Table {TABLE_NAME} created successfully")


def insert_data(connection, csv_file):
    """Inserts data from a CSV file into the database if not exists."""
    cursor = connection.cursor()
    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            user_id = row.get('user_id') or str(uuid.uuid4())
            name = row['name']
            email = row['email']
            age = row['age']
            # Insert only if user_id doesn't exist
            cursor.execute(f"""
                INSERT IGNORE INTO {TABLE_NAME} (user_id, name, email, age)
                VALUES (%s, %s, %s, %s)
            """, (user_id, name, email, age))
    connection.commit()
    cursor.close()
    print(f"Data from {csv_file} inserted successfully")


def stream_rows(connection, limit=None):
    """Generator that yields rows from the user_data table one by one."""
    cursor = connection.cursor()
    query = f"SELECT * FROM {TABLE_NAME}"
    if limit:
        query += f" LIMIT {limit}"
    cursor.execute(query)
    for row in cursor:
        yield row
    cursor.close()
