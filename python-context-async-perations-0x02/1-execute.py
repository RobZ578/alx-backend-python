#!/usr/bin/env python3
import sqlite3


class ExecuteQuery:
    """Context manager to execute a query and return results automatically."""

    def __init__(self, db_name, query, params=()):
        self.db_name = db_name
        self.query = query
        self.params = params
        self.conn = None
        self.results = None

    def __enter__(self):
        # Open database connection
        self.conn = sqlite3.connect(self.db_name)
        cursor = self.conn.cursor()
        cursor.execute(self.query, self.params)
        self.results = cursor.fetchall()
        return self.results  # return the results directly

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Commit if no error, rollback otherwise
        if exc_type:
            self.conn.rollback()
        else:
            self.conn.commit()
        self.conn.close()


if __name__ == "__main__":
    query = "SELECT * FROM users WHERE age > ?"
    params = (25,)

    with ExecuteQuery("users.db", query, params) as results:
        print("Users older than 25:")
        for row in results:
            print(row)
