# 6. Delete rows

## SQL
The SQL syntax for deleting rows is:

```sql
DELETE 
FROM tablename
WHERE condition
```

Executing DELETE in SQL without specifying a condition will delete all rows from a table!

## Delete one or more rows

The SQLModel equivalent of SQL DELETE is: `session.delete()`

To use this, you first locate the row or rows to be deleted using `select()` and then pass the results to `delete()`.

An example with the statements from the documentation:

```python
with Session(engine) as session:
    # select the row
    statement = select(Hero).where(Hero.name == "Spider-Youngster")
    results = session.exec(statement)
    # create the object
    hero = results.first()
    # Delete and commit
    session.delete(hero)
    session.commit()
```

## Delete from tables with relationships

If you did not set any constraints for 'ON DELETE' in the classes, then using SQL no via SQLModel by default SQL takes
no action on the related records when the parent is deleted.

According to the SQLModel documentation the default is to SET NULL.

By setting `cascade_delete=True` in a Relationship(), SQLModel automatically deletes the related records when the parent
one is deleted.

Example from the SQLModel documentation:

`heroes: list["Hero"] = Relationship(back_populates="team", cascade_delete=True)`

If you also intend to interact with database directly, outside SQLModel, then `ondelete` must also be configured in the
Field().

`team_id: int | None = Field(default=None, foreign_key="team.id", ondelete="CASCADE")`

For more details, refer to
the [cascade delete relationships documentation](https://sqlmodel.tiangolo.com/tutorial/relationship-attributes/cascade-delete-relationships/#cascade-delete-relationships).

# Activity: Delete rows

Add code to delete the following. Print before and after to show the results. Print the Enrollment table as well.

1. Delete the Teacher with name "John Smith"
2. Delete the Enrollment for Student with student_id 1 from Course with Course_id 1

[Next activity](8-07-update.md)