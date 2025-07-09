#!/usr/bin/python3

seed = __import__('seed')

connection = seed.connect_db()
if connection:
    seed.create_database(connection)
    connection.close()
    print("connection successful")

    connection = seed.connect_to_prodev()
    if connection:
        seed.create_table(connection)
        seed.insert_data(connection, 'user_data.csv')

        print("Database ALX_prodev is present")

        gen = seed.stream_users(connection)
        for i in range(5):
            print(next(gen))

        connection.close()
