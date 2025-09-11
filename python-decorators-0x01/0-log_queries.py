#!/usr/bin/env python3
import sqlite3
import functools

# Decorator to log SQL queries
def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Extract the SQL query from arguments if present
        query = None
        if args:
            query = args[0]
        elif "query" in kwargs:
            query = kwargs["query"]

        # Log the query
        if query:
            print(f"[LOG] Executing SQL query: {query}")

        # Call the original function
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


# Example usage
if __name__ == "__main__":
    users = fetch_all_users(query="SELECT * FROM users")
    print(users)
