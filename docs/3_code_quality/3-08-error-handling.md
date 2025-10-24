# 8. Error handling

NB This activity mentions database connections. Database connections are covered in week 4. This should not prevent you
completing this activity as any database specific code is given to you within this activity and the associated starter
code files.

## Introduction

Errors and exceptions can lead to unexpected behaviour, or even cause an app or script to stop running.

Errors is an issue that occurs that prevents the code from completing. For example, a syntax error such as
`print(0 / 0))` (unmatched brackets).

Exceptions are slightly different. The code may be syntactically correct yet when the code is run an error occurs.
Exceptions can be caught and handled using try/except.

Linting and as static analysis tools will typically find errors; however potential exceptions are harder to identify.

Instead, it is better to consider how your code might fail when you are writing it and identify potential exceptions.

You should then write code that allows your code to handle the exception gracefully.

## try/except/else/finally

Use the try and except block to catch and handle exceptions. You can optionally add else and/or finally.

- **try** Python executes code following the `try` statement as a normal part of the program execution.
- **except** If there is an exception is raised, execute the code within the `except` statement. You can have multiple
  except statement to handle different types of exception.
- **else** If there is no exception, execute the code after the `else` statement after the code in the `try` statement
- **finally** This is optional but if included the code after the `finally` statement is always run, even if there is an
  exception. Often used for cleaning up resources, for example closing a file.

There is an example of this in the `print_data` function
in [starter_exceptions.py](../../src/activities/starter/starter_exceptions.py)

### Alternative methods for catching multiple exceptions

More detail on catching multiple exceptions in this
tutorial: [Real Python: How to Catch Multiple Exceptions in Python](https://realpython.com/python-catch-multiple-exceptions/)

#### Structural pattern matching

Structural pattern matching is a feature introduced in Python 3.10 that allows you to match complex conditions using a
match statement, similar to switch statements in other languages. This is considered more readable than if/elif chains.

The technique is not specifically for exception handling. However, it could be used to write the code to handle multiple
potential errors more clearly.

There is an example of this in the `print_data_pattern_example` function
in [starter_exceptions.py](../../src/activities/starter/starter_exceptions.py)

#### Exception groups and add_note

Introduced from Python 3.11. Bundles multiple unrelated exceptions, useful when multiple tasks fail at once, and you
want to raise them together e.g. useful in asynch functions in web apps

Exception groups take two arguments:

- The usual description
- A sequence of sub-exceptions

## Which exception to use?

Python and most Python libraries have built in exceptions with descriptions that can be raised when a given type of
issue arises.

As far as you can try to identify which exception is likely to be raised, and be as specific as possible

For example, if you try to open a file that may not be found in the location specified, don't raise the base Python
`Exception` instead raise an OS `FileNotFoundError` exception.

Most guidance, and therefore linters (e.g., [ruff](https://docs.astral.sh/ruff/rules/bare-except/)), warn that you
should not raise a bare exception. A bare exception is when you don't specify the type of exception to catch, e.g.:

```python
try:
    # some code
except:
    # handle any exception
```

A bare except will catch all exceptions, including system-exiting exceptions like KeyboardInterrupt and SystemExit. This
can make it hard to stop your program with Ctrl+C, or can hide errors and bugs. It is considered bad practice because it
makes your code less predictable and harder to maintain. It's considered better to catch only the exceptions you expect
and know how to handle.

You can also define your own exceptions. If you do this note that PEP8 says exceptions should be named with the suffix
`Error` e.g. `ConnectionError`

## Which exceptions to handle?

Deciding when you need to handle an exception is tricky. You will learn more as you experiment with running code,
reading documentation and tutorials etc.

As a starting point for this coursework, errors typically arise when the file can't be found, a database can't be
opened, or a data attribute or value is not found.

Consider the following situations that might lead to an error:

- File and I/O errors for files that don’t exist, insufficient permissions
- Database errors: connection errors, data integrity issues, programming syntax error, invalid data types
- Data parsing and format when reading csv, xlsx, JSON data
- Type and value errors for incorrect data types and invalid values
- Index or key errors when index is out of range or a key is not found
- Math computation errors such as division by zero

Some of the more common exceptions to use:

Python file handling:

- [FileNotFound](https://docs.python.org/3/library/exceptions.html#FileNotFoundError)

Pandas dataframes:

- [AttributeError](https://docs.python.org/3/library/exceptions.html#AttributeError)
- [KeyError](https://docs.python.org/3/library/exceptions.html#KeyError)
- [DtypeWarning](https://pandas.pydata.org/docs/reference/api/pandas.errors.DtypeWarning.html)

sqlite3 invalid data:

- [IntegrityError](https://docs.python.org/3/library/sqlite3.html#sqlite3.IntegrityError)

Also consider
using
a [context manager to handle sqlite3 database connections](https://docs.python.org/3/library/sqlite3.html#sqlite3-connection-context-manager).
This automatically commits or rolls back transactions and is useful to combine with exceptions. This example is from the
sqlite3 documentation:

```python
con = sqlite3.connect(":memory:")
con.execute("CREATE TABLE lang(id INTEGER PRIMARY KEY, name VARCHAR UNIQUE)")

# Successful, con.commit() is called automatically afterwards
with con:
    con.execute("INSERT INTO lang(name) VALUES(?)", ("Python",))

# con.rollback() is called after the with block finishes with an exception,
# the exception is still raised and must be caught
try:
    with con:
        con.execute("INSERT INTO lang(name) VALUES(?)", ("Python",))
except sqlite3.IntegrityError:
    print("couldn't add Python twice")

# Connection object used as context manager only commits or rollbacks transactions,
# so the connection object should be closed manually
con.close()
```

## Activity: add exception handling

1. Consider the `create_db` and `describe` functions in
   [starter_exceptions.py](../../src/activities/starter/starter_exceptions.py).
2. Identify where errors might be likely to occur.
3. Add exception handling.
4. Test out your exception handling by passing incorrect values to the functions.

AI spoiler: If you add a `Raises:` section to the docstring and specify the exceptions and conditions when they should
be raised, copilot can more easily add the relevant try/catch for you.