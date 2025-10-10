# 7. Summary

Many concepts have been introduced this week. These are key concepts that you need to understand to support the design
work in the next 5 weeks as well as the application development work next term.

If you are unsure of the concepts, please ask questions during office hours or in a tutorial; or carry out your own
research, there are many tutorials online.

The key points to understand:

- A Python **class** models a real world object. It has attributes that can store data values, and methods that carry
  out functions or behaviour. A class can have just attributes. An **object** is one instance of a class that has been
  created.

- A Python **dataclass** is used where the primary purpose of the class is to store data, the syntax is cleaner and
  requires less code that the standard Python class.

- **Inheritance** is a concept that allows one class to inherit the attributes and methods of another, whilst also
  implementing its own.

- **Pydantic** is a Python library that is used to provide **data validation** for Python classes. To use pydantic, a
  class inherits the pydantic `BaseModel` class. Data validation is useful as you will be creating apps that deal with
  data and need to ensure that the data is valid before using it in your database.

- Object-Relational Mapping **ORM** is a programming technique that lets you interact with a database using objects in
  your code, instead of writing raw SQL queries. ORMs automatically map database tables to classes and rows to objects,
  making it easier to work with data in a more Pythonic and intuitive way.

- **SQLModel** is ORM that is build on pydantic and SQLAlchemy. It is a Python package.

- Pydantic and SQLModel refer to 'models'. A **model** is simply a Python class that defines the structure and types of
  data. That is it 'models' the data that an application will use.

- Python classes, Python data classes, pydantic model classes vary in their syntax which could seem confusing. Focus on
  learning SQLModel syntax.

Note that for coursework 2 you are welcome to use SQLAlchemy instead of SQLModel if you prefer.