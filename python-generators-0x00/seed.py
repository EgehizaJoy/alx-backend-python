import mysql.connector
import uuid
import csv

def connect_db():
    return mysql.connector.connect(
        host="localhost",
	port=3307,
        user="root",
        password=""
    )

def create_database(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    cursor.close()

def connect_to_prodev():
    return mysql.connector.connect(
        host="localhost",
	port=3307,
        user="root",
        password="",
        database="ALX_prodev"
    )

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            user_id VARCHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL NOT NULL,
            INDEX (user_id)
        )
    """)
    connection.commit()
    cursor.close()
    print("Table user_data created successfully")

def insert_data(connection, file_path):
    cursor = connection.cursor()
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cursor.execute("SELECT COUNT(*) FROM user_data WHERE email = %s", (row['email'],))
            if cursor.fetchone()[0] == 0:
                cursor.execute("""
                    INSERT INTO user_data (user_id, name, email, age)
                    VALUES (%s, %s, %s, %s)
                """, (str(uuid.uuid4()), row['name'], row['email'], row['age']))
    connection.commit()
    cursor.close()

def stream_users(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data")
    for row in cursor:
        yield row
    cursor.close()
