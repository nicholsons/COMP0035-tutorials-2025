import sqlite3
import os

def create_db(sql_script_path, db_path):
    # If a database file already exists, delete it first
    if os.path.exists(db_path):
        os.remove(db_path)
        print(f"Deleted existing database: {db_path}")

    with open(sql_script_path, 'r') as file:
        sql_script = file.read()

    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.executescript(sql_script)

    connection.commit()
    connection.close()
    print(f"Database created successfully at {db_path}")

if __name__ == "__main__":
    sql_path = "/Users/ismaelblanca/Downloads/UCL CHEM ENG/Year 3/COMP0035/COMP0035-tutorials-2025/week4/paralympics_with_data.sql"
    db_path = "/Users/ismaelblanca/Downloads/UCL CHEM ENG/Year 3/COMP0035/COMP0035-tutorials-2025/src/activities/data/paralympics_data.sqlite"
    create_db(sql_path, db_path)