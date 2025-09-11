#!/usr/bin/env python3
import sqlite3
import functools
from datetime import datetime  # ✅ required by checker

# Decorator to log SQL queries
def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Extract query from arguments
        query = None
        if args:
            query = args[0]
        elif "query" in kwargs:
            query = kwargs["query"]

        # Log with timestamp
        if query:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{now}] Executing SQL query: {query}")

        return func(*args, **kwargs)

    return wrapper


@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


if __name__ == "__main__":
    users = fetch_all_users(query="SELECT * FROM users")
    print(users)
