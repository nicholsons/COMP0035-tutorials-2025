# 15. Insert data to tables with foreign keys

In the previous activities you used INSERT to add data to the student, teacher and course tables; and SELECT to retrieve
values from the data that was added.

This activity combines SELECT and INSERT to add rows to the tables with foreign keys.

To add an enrollment record for a row in the csv file you need to find the id values from teacher, student, and course
for that row.

You could take the row values and run three separate SELECT queries to find the relevant ids from the teacher, student,
and course tables.

You could shorten the SQL needed using a nested SQL query.

An example of the syntax:

```sql

INSERT INTO employees (emp_name, dept_id)
SELECT 'Alice Johnson', dept_id
FROM departments
WHERE dept_name = 'Computer Science';
```

## Activity: use nested query to insert data into the enrollment table

The following is a paramaterised query that could be used to get the values or the enrollment table.

```sql
INSERT INTO enrollment (student_id, course_id, teacher_id)
VALUES ((SELECT student_id FROM student WHERE student_email = ?),
        (SELECT course_id FROM course WHERE course_name = ? AND course_code = ?),
        (SELECT teacher_id FROM teacher WHERE teacher_email = ?))            
```

1. Delete the current data from the tables. Your code would fail database constraints if you try to add the same data
   again. You could drop and recreate the tables, or the following deletes all rows from all the tables.
    ```python
    def delete_rows(db_path):
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
        table_names = [row[0] for row in cur.fetchall()]
        for table_name in table_names:
            cur.execute(f"DELETE FROM {table_name}")
        conn.commit()
        conn.close()
   ```
2. Add code to your function where you added the data to also add the enrollment data.
   ```python
    enrollment_insert_sql = """
                            INSERT INTO enrollment (student_id, course_id, teacher_id)
                            VALUES ((SELECT student_id FROM student WHERE student_email = ?), \
                                    (SELECT course_id FROM course WHERE course_name = ? AND course_code = ?), \
                                    (SELECT teacher_id FROM teacher WHERE teacher_email = ?)) \
                            """
    for _, row in df.iterrows():
        cursor.execute(
            enrollment_insert_sql,
            (
                row['student_email'],
                row['course_name'],
                row['course_code'],
                row['teacher_email'],
            )
        )
    ```
3. Run the code again to create the add the data to the database. You should now have data in all the tables

## Activity: Add data to the paralympics database

Code to add data is given in `starter/add_data_paralympics.py`. You may need to modify it to suit your schema.

The general approach used in this activity was:

1. Use pandas to load the data from .csv
2. Define the file path to the database
3. Create a connection to the database using sqlite3
4. Create a sqlite3 cursor that will be used to execute the SQL
5. Enable foreign key support
6. Execute the SQL using sqlite3 to create the database structure 
7. Use sqlite3 and SQL queries to write code to add the data from the dataframe to the database
8. Close the connection