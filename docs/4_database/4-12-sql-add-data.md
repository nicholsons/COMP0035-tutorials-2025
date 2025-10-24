# 12. Introduction to SQL queries to add data to the database

So far you have used SQL statements to create tables.

To add data to those tables you need to learn the basics of the SELECT and INSERT statements.

- INSERT is used to add new rows to a table.
- SELECT is used to find values row a table.

To add data to the tables that do not have any FK attributes you can simply INSERT values into the rows.

To add data to tables that have an FK attribute, then you need to query the parent table to find the value of the PK
field for the relevant row and then use this value when you insert the new row in the child table.

For example, imagine you have a table for owners and a table for their pets. An owner can have more than one pet.
To add a new owner, Zavian, and his pet, Frodo, you would need to:

- INSERT a row into the owners for Zavian.
- SELECT the id of the row where name=Zavian, assume the result is 3.
- Now you can INSERT a row for Champion where the owner_id is 3.

| id | name   |
|:---|:-------|
| 1  | Fred   |
| 2  | Skylar |

| id | pet_name | owner_id |
|:---|:---------|:---------|
| 1  | Champion | 1        |

The next two activities walk through the basic skills for INSERT and SELECT.

## SQL references and tutorials

The following references have more details:

- [SQLite SELECT reference](https://www.sqlite.org/lang_select.html)
- [SQLite SELECT tutorial](https://www.sqlitetutorial.net/sqlite-select/) gives examples.
- [SQLite INSERT reference](https://www.sqlite.org/lang_insert.html)
- [SQLite INSERT tutorial](https://www.sqlitetutorial.net/sqlite-insert/) gives examples.

There are plenty of other reference sites available if you search.

[Next activity](4-13-insert-no-fk.md)