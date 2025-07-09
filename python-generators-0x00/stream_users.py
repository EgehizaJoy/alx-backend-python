import mysql.connector
from decimal import Decimal

def stream_users():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ALX_prodev",
        port=3307
    )
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM user_data")
        for row in cursor:
            # Convert Decimal to int for printing (optional)
            if isinstance(row.get("age"), Decimal):
                row["age"] = int(row["age"])
            yield row
    finally:
        cursor.close()
        connection.close()

