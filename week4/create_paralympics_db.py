import os
import sqlite3

def create_db(sql_script_path, db_path):
    # Make sure the parent folder exists
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    with open(sql_script_path, 'r') as file:
        sql_script = file.read()

    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.executescript(sql_script)

    connection.commit()
    connection.close()

if __name__ == "__main__":
    sql_path = "/Users/ismaelblanca/Downloads/UCL CHEM ENG/Year 3/COMP0035/COMP0035-tutorials-2025/week4/paralympics_schema.sql"
    db_path = "/Users/ismaelblanca/Downloads/UCL CHEM ENG/Year 3/COMP0035/COMP0035-tutorials-2025/src/activities/data/para-normalised.db"
    create_db(sql_path, db_path)