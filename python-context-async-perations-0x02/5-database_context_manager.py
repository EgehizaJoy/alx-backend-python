#!/usr/bin/env python3
import sqlite3

class DatabaseConnection:
    def __enter__(self):
        self.conn = sqlite3.connect('users.db')
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

# Using the custom context manager to fetch users
with DatabaseConnection() as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

print(users)
