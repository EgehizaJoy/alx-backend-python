import sqlite3

class ExecuteQuery:
    def __init__(self, db_name, query, params=None):
        self.db_name = db_name
        self.query = query
        self.params = params or ()
        self.connection = None
        self.cursor = None
        self.result = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute(self.query, self.params)
        self.result = self.cursor.fetchall()
        return self.result

    def __exit__(self, exc_type, exc_value, traceback):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

# Example usage
if __name__ == "__main__":
    db_name = "example.db"

    # Setup sample data (only for testing)
    with sqlite3.connect(db_name) as conn:
        c = conn.cursor()
        c.execute("DROP TABLE IF EXISTS users")
        c.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
        c.executemany("INSERT INTO users (name, age) VALUES (?, ?)", [
            ("Alice", 24), ("Bob", 30), ("Charlie", 28), ("Diana", 22)
        ])
        conn.commit()

    # Use the custom context manager to execute query
    query = "SELECT * FROM users WHERE age > ?"
    param = (25,)

    with ExecuteQuery(db_name, query, param) as results:
        for row in results:
            print(row)
