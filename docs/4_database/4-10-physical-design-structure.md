# 10. Physical design: defining an SQLite schema in Python

## Physical design

Goal: Optimize the logical model for performance and storage on a specific DBMS.

Output: A physical schema detailing file structure, indexing, and more.

Focus: How the data will be stored and accessed efficiently.

Connolly and Begg's definition of physical design goes beyond what is covered in this course. **For COMP0035** physical
design is interpreted as the creation of the schema in an SQLite database.

For this activity you will use the `sqlite3` library which is part of the base Python installation so you do not need to
explicitly install it in your virtual environment. Later in the course, `sqlmodel` or `sqlalchemy` will be used instead
of `sqlite3`; these use a different approach so `sqlite3` is suggested for coursework 1.

Python is not required to create an SQLite database; independent tools such as DBBrowser lite, and tools
integrated in the IDE that can create SQLite databases. However, for the coursework assessment you must create the
database by defining a SQL schema and implement that as an SQLite file using Python code.

## Using SQL

Structured Query Language or SQL provides a syntax for creating relational database. SQLite is a variant of SQL, and
there are some differences.

- [SQLite documentation](https://www.sqlite.org/docs.html)
- [general SQL references](https://www.w3schools.com/sql/)

The general structure of a SQLite statement to [create two related tables](https://www.sqlite.org/lang_createtable.html)
is:

```SQL
CREATE TABLE table_name_1
(
    column_name_1 data_type PRIMARY KEY,
    column_name_2 data_type NOT NULL,
    column_name_3 data_type NOT NULL UNIQUE,
    FOREIGN KEY (column_name_1) REFERENCES table_name_2 (column_name_1)
);

CREATE TABLE table_name_2
(
    column_name_1 data_type PRIMARY KEY,
    column_name_2 data_type
);
```

SQL keywords are not case-sensitive, writing 'create table' has the same effect as 'CREATE TABLE'. By convention the SQL
keywords are upper case and adhering to this makes your code more readable by others.

The `;` at the end of a SQL statement is required by some database management systems and is used to separate SQL
statements.

## SQLite data types

SQLite uses a dynamic type system, which is different from the static type systems used in other DBMS such as PostgreSQL
or MySQL.

SQLite does not enforce strict data types for columns. Instead, it uses a concept called type affinity, which means each
column has a preferred type, but it can still store values of other types.

Type affinity is determined by the declared type of the column (e.g., INTEGER, TEXT, REAL, etc.). SQLite will attempt to
convert values to the column's affinity when inserting data.

SQLite maps declared types to one of five storage classes:

- NULL: The value is a NULL.
- INTEGER: A signed integer.
- REAL: A floating-point number.
- TEXT: A text string.
- BLOB: A binary large object.

Note there is no DATE. Dates can be stored as TEXT (e.g. '2025-09-19 10:30:00'), INTEGER or REAL. TEXT is generally used
unless you have a specific reason to use the other types.

For more refer to the [SQLite documentation](https://www.sqlite.org/datatype3.html).

The main thing to consider is:

> Prefer the 5 SQLite data types when you define the schema, if you use other data types then SQLite will attempt to
> map these to its types. Dates are typically stored as text in the format '2025-09-19 00:00:00'

## Activity: Write SQL statements to define the tables

You can write SQL statements as Python strings.

However, IDEs typically have tools that support checking of SQL written in SQL files so this approach is suggested.

By default, SQLite does not enforce FK unless specifically configured. Add `PRAGMA foreign_keys = ON;` to the start of
the
sql statements to enable this.

1. Copy the starter file [paralympics_schema_starter.sql](../../src/activities/starter/paralympics_schema_starter.sql)
   to your module. Rename it to remove `_starter`.
2. Write SQL statements that define the tables, their keys and any constraints. Some tables are defined for you so you
   see the syntax. The starter file has the ERD in comments for ease of reference.

   NB:
    - Store dates as TEXT.
    - Table creation order matters. You cannot add an FK if the table it refers to has not yet been created. Start with
      the tables that don't have any FK.
    - Keep table names to all lowercase, no spaces or underscores (not important now but will make it easier in later
      activities!)

[Next activity](4-11-physical-design-create-db.md)
