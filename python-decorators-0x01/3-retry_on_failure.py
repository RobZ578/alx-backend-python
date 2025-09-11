#!/usr/bin/env python3
import time
import sqlite3
import functools


def with_db_connection(func):
    """Decorator that opens and closes a database connection automatically"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')  # open connection
        try:
            result = func(conn, *args, **kwargs)
        finally:
            conn.close()  # always close connection
        return result
    return wrapper


def retry_on_failure(retries=3, delay=2):
    """Decorator that retries a function if it raises an exception"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempt += 1
                    if attempt == retries:
                        print(f"Failed after {retries} retries: {e}")
                        raise
                    print(f"Attempt {attempt} failed: {e}. Retrying in {delay} seconds...")
                    time.sleep(delay)
        return wrapper
    return decorator


@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()


if __name__ == "__main__":
    users = fetch_users_with_retry()
    print(users)
