# 1. Introduction to database design (recap)

This is a brief recap of the lecture material.

## Relational database

A **relational database** is a method of structuring data as **tables** associated to each other by shared attributes:

- a row corresponds to a unit of data called a record
- a column corresponds to an attribute (or field) of that record
- a table contains these rows and columns

<img alt="Table, record, attribute" src="../img/db-intro.png" title="Table, record, attribute"/>

Relational databases typically use **Structured Query Language (SQL)** to define, manage, and search data.

### Relational database design

**Database design** is the organization of data according to a database model. The designer determines what data must be
stored and how the data elements interrelate.

Connolly & Begg describe three stages of database design, summarised as:

1. Conceptual database design

    - Goal: Create a high-level data model that captures the data requirements.
    - Output: An Entity-Relationship (ER) model.
    - Focus: What data should be stored, and the relationships between data items.

2. Logical database design

    - Goal: Translate the conceptual model into a logical model that can be implemented in a specific type of database (
      e.g., relational).
    - Output: A relational schema with tables, attributes, primary/foreign keys, and constraints. Includes normalization
      to reduce redundancy and improve integrity. Can also be drawn as an ERD.
    - Focus: How the data will be structured logically, independent of any specific database management system (DBMS).

3. Physical database design

   Goal: Optimize the logical model for performance and storage on a specific DBMS.
   Output: A physical schema detailing file structure, indexing, and more. The full definition in Connolly & Begg's book
   goes beyond what is covered in this course.
   Focus: How the data will be stored and accessed efficiently.
   **For COMP0035, physical design is interpreted as the creation of the schema in an SQLite database.**

## Normalisation

**Normalisation** is the process of structuring data into tables in a way that avoids update anomalies; and reduces data
redundancy and the resulting data storage.

Update anomalies can occur when the same value is in multiple tables and needs to be updated or deleted in both; issues
can occur if not all occurrences are identified and updated.

The process of normalisation divides larger tables into smaller tables and links them using relationships between key
attributes.

- **Primary key (PK)**: a column (or combination of columns) guaranteed to be unique for each record and cannot be NULL
- **Foreign key (FK)**: a column in table A storing a primary key value from table B

![Keys](../img/db-key.png)

<p style="text-align: center; font-style: italic">A course is taken by many students, each student is enrolled on only one course<p>

There are different levels of normalisation. It is not always desired, or necessary, to achieve 6th normal form, for the
purposes of this course (and many applications) 3rd normal form is typically sufficient.

This course focuses on the general principles of normalization rather than the formal relational theory (refer to either
of the database textbooks in the reading list if you wish to understand this topic in more detail).

Design your database so that:

- Each column/row intersection has only one entry.
- Each row and column in a table is unique.
- Each table has a primary key (a unique identifier).
- Tables with relationships are linked by primary/foreign key relationships.
- If you delete a record you don’t also lose a value that may still be needed.
- Where there is a many-to-many relationship you will need to add a new table between the two tables so forming two
  one-to-many relationships.

[Next activity](4-02-erd-intro.md)