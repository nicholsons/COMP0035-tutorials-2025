"""
create_student_db.py

COMP0035 Week 4 – Relational Database Design and Normalisation (3NF)

This script loads student-course-teacher data from CSV and creates a fully normalised
relational SQLite database (`student_db.sqlite`) that includes:

- `teachers`: each teacher appears once
- `courses`: each course appears once
- `students`: each student appears once
- `enrolments`: maps students to courses (many-to-many join table)

This implements:
• Relational database design (entities + relationships)
• 3NF normalisation (no redundancy, foreign key integrity)
• Physical schema in SQLite

Author: Ismael Blanca Lahrech
"""

import sqlite3
import pandas as pd
from pathlib import Path

# -------------------------------------------------------------------------
# Step 0: File paths
# -------------------------------------------------------------------------

CSV_PATH = Path(
    "/Users/ismaelblanca/Downloads/UCL CHEM ENG/Year 3/COMP0035/"
    "COMP0035-tutorials-2025/src/activities/data/student_data.csv"
)

DB_PATH = Path(
    "/Users/ismaelblanca/Downloads/UCL CHEM ENG/Year 3/COMP0035/"
    "COMP0035-tutorials-2025/src/activities/data/student_db.sqlite"
)

# -------------------------------------------------------------------------
# Step 1: Read and inspect the raw data
# -------------------------------------------------------------------------

df = pd.read_csv(CSV_PATH)
print("Original CSV Data:")
print(df.head())

# -------------------------------------------------------------------------
# Step 2: Connect to SQLite and prepare database
# -------------------------------------------------------------------------

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Drop existing tables (for repeat runs)
cursor.execute("DROP TABLE IF EXISTS enrolments;")
cursor.execute("DROP TABLE IF EXISTS students;")
cursor.execute("DROP TABLE IF EXISTS courses;")
cursor.execute("DROP TABLE IF EXISTS teachers;")

# -------------------------------------------------------------------------
# Step 3: Create relational schema (4 tables)
# -------------------------------------------------------------------------

cursor.execute("""
    CREATE TABLE teachers (
        teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
        teacher_name TEXT NOT NULL,
        teacher_email TEXT UNIQUE NOT NULL
    );
""")

cursor.execute("""
    CREATE TABLE courses (
        course_id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_name TEXT NOT NULL,
        course_code TEXT UNIQUE,
        course_schedule TEXT,
        course_location TEXT,
        teacher_id INTEGER,
        FOREIGN KEY (teacher_id) REFERENCES teachers (teacher_id)
    );
""")

cursor.execute("""
    CREATE TABLE students (
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_name TEXT NOT NULL,
        student_email TEXT UNIQUE NOT NULL
    );
""")

cursor.execute("""
    CREATE TABLE enrolments (
        student_id INTEGER,
        course_id INTEGER,
        PRIMARY KEY (student_id, course_id),
        FOREIGN KEY (student_id) REFERENCES students (student_id),
        FOREIGN KEY (course_id) REFERENCES courses (course_id)
    );
""")

# -------------------------------------------------------------------------
# Step 4: Populate normalised tables
# -------------------------------------------------------------------------

# Insert teachers
teacher_id_map = {}
for _, row in df.drop_duplicates(subset=["teacher_email"]).iterrows():
    cursor.execute("""
        INSERT INTO teachers (teacher_name, teacher_email)
        VALUES (?, ?);
    """, (row["teacher_name"], row["teacher_email"]))
    teacher_id_map[row["teacher_email"]] = cursor.lastrowid

# Insert courses
course_id_map = {}
for _, row in df.drop_duplicates(subset=["course_code"]).iterrows():
    teacher_fk = teacher_id_map[row["teacher_email"]]
    cursor.execute("""
        INSERT INTO courses (
            course_name, course_code, course_schedule,
            course_location, teacher_id
        ) VALUES (?, ?, ?, ?, ?);
    """, (
        row["course_name"],
        row["course_code"],
        row["course_schedule"],
        row["course_location"],
        teacher_fk
    ))
    course_id_map[row["course_code"]] = cursor.lastrowid

# Insert students
student_id_map = {}
for _, row in df.drop_duplicates(subset=["student_email"]).iterrows():
    cursor.execute("""
        INSERT INTO students (student_name, student_email)
        VALUES (?, ?);
    """, (row["student_name"], row["student_email"]))
    student_id_map[row["student_email"]] = cursor.lastrowid

# Insert enrolments (many-to-many)
for _, row in df.iterrows():
    student_fk = student_id_map[row["student_email"]]
    course_fk = course_id_map[row["course_code"]]
    cursor.execute("""
        INSERT INTO enrolments (student_id, course_id)
        VALUES (?, ?);
    """, (student_fk, course_fk))

# ------------------------------------------------------------------------
# Step 5: Commit and close
# -------------------------------------------------------------------------

conn.commit()
conn.close()

print("\n✅ Student database created successfully and normalised to 3NF.")
print(f"Database saved at: {DB_PATH}")
