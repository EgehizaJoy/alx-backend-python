# Python Generators – ALX Project

This project focuses on using Python to interact with a MySQL database and stream rows using generators.

## Features

- Connects to MySQL server (localhost:3307 via XAMPP)
- Creates a database (`ALX_prodev`) and table (`user_data`)
- Inserts data from a CSV file
- Streams data row by row using generators (to be implemented)

## Files

- `seed.py` – Contains database setup and data insertion logic
- `0-main.py` – Main script to test the setup
- `user_data.csv` – Sample data to populate the database

## How to Run

Make sure MySQL (via XAMPP) is running on port `3307`, then run:

```bash
py 0-main.py
