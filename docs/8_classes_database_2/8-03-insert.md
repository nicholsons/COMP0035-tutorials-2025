# 3. Insert data into a single table

## Recap from week 5

[Activity 5.7](../5_classes_orm/5-06-sqlmodel-add-data.md) introduced how to add data to a single table.

Inserting data into the paralympics database is complex and beyond what you would need in your coursework so this
activity returns to the student database example.

To recap, the SQL syntax to insert is like:

```sql
INSERT INTO tablename (colname1, colname2)
VALUES ("Something", 123.5);
```

You can insert values for all columns, or only named columns.

When using this with sqlite3 you can use parameterised queries to insert one or more values from variables.

The SQLModel equivalents are [`add()`](https://sqlmodel.tiangolo.com/tutorial/insert/) for a single row and `add_all()`
for multiple rows.

The steps when using SQLModel:

```python
from sqlmodel import Session, create_engine
# 1. Create the engine which creates the connection to the database
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=True)

# 2. Create one or more rows to add
teacher = Teacher(name="Freida", email="freida@myorg.com")

# 3. Create a session
with Session(engine) as session:
    # 4. Add the rows (or rows if add_all)
    session.add(teacher)
    # 5. Commit the new row
    session.commit()
```

## Activity: Generate the student database

The `app.py`, `database.py` and `models.py` from week 5 have been modified for the student database
in [activities/starter/db_wk8](../../src/activities/starter/db_wk8).

1. Copy the files to your own package as you will edit the files. Check the imports are correct, you may need to update
   these.
2. Create the database using the code in `app.py`

## Add data to a table without relations

[src/activities/data/student_data.csv](../../src/activities/data/student_data.csv) has the raw data.

It has these fields:
`teacher_name,teacher_email,student_name,student_email,course_name,course_code,course_schedule,course_location`

The class in models.py for the teacher has this structure:

```python
class Teacher(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    teacher_name: str
    teacher_email: str
```

To insert values into the database you could create an object for each row as there are only a few rows; and then add
and commit.

```python
teacher = Teacher(teacher_name="Ani Sarana", teacher_email="as@school.com")
engine = database.engine

with Session(engine) as session:
    session.add(teacher)
    session.commit()
```

In practice, you will have many rows.

There are other ways to read data from a .csv file, however as you know pandas DataFrame then use that.

You can then iterate the rows and use the '.to_dict()' method of the Teacher class that is inherited from pydantic to
get the values for each row.

```python
import pandas as pd


def add_teacher_data():
    data_path = resources.files(data).joinpath("student_data.csv")
    cols = ["teacher_name", "teacher_email"]
    df = pd.read_csv(data_path, usecols=cols)

    # 2. Convert DataFrame rows to SQLModel instances
    teachers = []
    for _, row in df.iterrows():
        record = models.Teacher(**row.to_dict())
        teachers.append(record)

    # 3. Insert into database
    with Session(engine) as session:
        session.add_all(teachers)
        session.commit()
```

## Activity: Add the teacher data to the database

Edit the starter files to add a teacher to the database.

The SQLModel documentation examples add this method to `app.py`. I added it to `database.py`. You choose where you think
is most appropriate.

[Next activity](8-04-insert-multiple.md)