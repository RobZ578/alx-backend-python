#!/usr/bin/env python3
import sqlite3
import functools

# Global cache dictionary
query_cache = {}


def with_db_connection(func):
    """Decorator that opens and closes a database connection automatically"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect("users.db")
        try:
            result = func(conn, *args, **kwargs)
        finally:
            conn.close()
        return result
    return wrapper


def cache_query(func):
    """Decorator to cache query results based on the SQL query string"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get("query")
        if query in query_cache:
            print(f"Cache hit for query: {query}")
            return query_cache[query]

        print(f"Cache miss for query: {query}. Executing database query...")
        result = func(*args, **kwargs)
        query_cache[query] = result  # store in cache
        return result
    return wrapper


@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


if __name__ == "__main__":
    # First call: executes query and stores in cache
    users = fetch_users_with_cache(query="SELECT * FROM users")
    print(users)

    # Second call: retrieves result from cache (no database hit)
    users_again = fetch_users_with_cache(query="SELECT * FROM users")
    print(users_again)
