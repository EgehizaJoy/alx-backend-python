import mysql.connector
from decimal import Decimal

def stream_users_in_batches(batch_size):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ALX_prodev",
        port=3307
    )
    cursor = connection.cursor(dictionary=True)
    users = []
    try:
        cursor.execute("SELECT * FROM user_data")
        batch = []
        for row in cursor:
            if isinstance(row["age"], Decimal):
                row["age"] = int(row["age"])
            batch.append(row)
            if len(batch) == batch_size:
                users.append(batch)
                batch = []
        if batch:
            users.append(batch)
        return users
    finally:
        cursor.close()
        connection.close()

def batch_processing(batch_size):
    all_batches = stream_users_in_batches(batch_size)
    for batch in all_batches:
        for user in batch:
            if user["age"] > 25:
                print(user)

