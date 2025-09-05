Python Generators – SQL Streaming Example
Project Overview

This project demonstrates how to use Python generators to stream rows from a MySQL database efficiently. It includes:

Setting up a MySQL database (ALX_prodev)

Creating a table (user_data)

Populating the table with sample data from user_data.csv

Implementing a generator to fetch rows one by one without loading all data into memory

Requirements

Python 3.x

MySQL Server

Python packages: mysql-connector-python

Sample CSV file: user_data.csv

Install required package using pip:

pip install mysql-connector-python

Files
File	Description
seed.py	Contains all functions for database connection, table creation, data insertion, and row streaming generator
0-main.py	Example usage script that sets up the database, inserts data, and tests the generator
user_data.csv	CSV file containing sample user data
README.md	Project documentation
Functions in seed.py

connect_db() – Connects to MySQL server without specifying a database.

create_database(connection) – Creates ALX_prodev database if it does not exist.

connect_to_prodev() – Connects to the ALX_prodev database.

create_table(connection) – Creates the user_data table with required fields and an indexed primary key.

insert_data(connection, csv_file) – Inserts data from user_data.csv into the table (ignores duplicates).

stream_rows(connection, limit=None) – Generator that streams rows from user_data one at a time. Optional limit parameter to restrict number of rows fetched.

Example Usage
from seed import connect_db, create_database, connect_to_prodev, create_table, insert_data, stream_rows

# Connect to MySQL
connection = connect_db()
if connection:
    create_database(connection)
    connection.close()

connection = connect_to_prodev()
if connection:
    create_table(connection)
    insert_data(connection, 'user_data.csv')

    # Stream first 5 rows
    for row in stream_rows(connection, limit=5):
        print(row)

Advantages

Memory-efficient: Only one row is loaded at a time, useful for large datasets.

Reusable: Generator can be used in loops or for processing data on the fly.

Scalable: Works well with millions of rows without exhausting memory.

Output Example
('00234e50-34eb-4ce2-94ec-26e3fa749796', 'Dan Altenwerth Jr.', 'Molly59@gmail.com', 67)
('006bfede-724d-4cdd-a2a6-59700f40d0da', 'Glenda Wisozk', 'Miriam21@gmail.com', 119)
('006e1f7f-90c2-45ad-8c1d-1275d594cc88', 'Daniel Fahey IV', 'Delia.Lesch11@hotmail.com', 49)
('00af05c9-0a86-419e-8c2d-5fb7e899ae1c', 'Ronnie Bechtelar', 'Sandra19@yahoo.com', 22)
('00cc08cc-62f4-4da1-b8e4-f5d9ef5dbbd4', 'Alma Bechtelar', 'Shelly_Balistreri22@hotmail.com', 102)

Notes

Ensure MySQL server is running and accessible.

Adjust DB_USER and DB_PASSWORD in seed.py as needed.

The generator pattern is ideal for processing or exporting large datasets row by row.
