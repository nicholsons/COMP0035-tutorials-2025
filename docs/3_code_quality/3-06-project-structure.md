# 6. Project structure

## Recap from week 2

Activity [2-01-python-structure.md](../2_pandas/2-01-python-structure.md) introduced the concept of organising your
project using packages, modules, functions and/or classes.

- A Python [module](https://docs.python.org/3/tutorial/modules.html) is "a file containing Python definitions and
  statements. The file name is the module name with the suffix .py appended."
- A Python [package](https://docs.python.org/3/tutorial/modules.html#packages) is "a way of structuring Python’s module
  namespace by using 'dotted module names'. For example, the module name A.B designates a submodule named B in a package
  named A." There is a more advanced concept, 'namespace packages', in Python that is not covered in this minor.
- A Python [function](https://docs.python.org/3/glossary.html#term-function) is "A series of statements which returns
  some value to a caller. It can also be passed zero or more arguments which may be used in the execution of the body."
- Directories (or folders) and files that are not Python code files, e.g. data files such as `.csv`, `.xlsx`;
  or database files such as `.sqlite` or `.db` files.
- Project configuration and information files e.g. README.md, .gitignore, pyproject.toml etc.

## Typical Python application project structure

There is no single pattern for structuring the files associated with a Python application. However, there are common
patterns. Adhering to these is useful, as often Python tools will auto discover or recognise files and folders saved in
these patterns; and it will also help other developers to more easily understand your code.

There are examples of typical Python project structures on these sites:

- [Python Packaging User Guide](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/#src-layout-vs-flat-layout)
- [The Hitchhiker's Guide to Python](https://docs.python-guide.org/writing/structure/#sample-repository)
- [Real Python](https://realpython.com/python-application-layouts/)

_The tutorial project is not a good example of how to structure an application project_, it is not designed for an app,
it is designed as a weekly series of activities and so there are repeated module names, repeated functions, etc. You
will likely see lots of warnings in your IDE about duplicated code.

Many of the package and module names also break the Python convention in PEP8. This is usually as I made the names
longer so it is clearer what the code is. [PEP8](https://peps.python.org/pep-0008/#package-and-module-names) says:

- Modules should have short, all-lowercase names. Underscores can be used in the module name if it improves readability.
- Python packages should also have short, all-lowercase names, although the use of underscores is discouraged.

A more suitable structure for your coursework might be as follows. Use meaningful package and module names, not
"my_python_project", "module1" or "app". You may also have sub-packages within your project package. You won't have
tests until coursework 2.:

```text
my_python_project/
    ├── README.md            # Information about your project for you and other developers who use your code
    ├── requirements.txt     # Lists packages your code requires. Used when creating a virtual environment.
    ├── pyproject.toml       # Configuration values for your project and tools that might be used (e.g. test, lint, formatter)
    ├── .gitignore           # Lists files that git should ignore and not add to github e.g., venv, IDE config, temporary files
    ├── .venv/               # Code for the virtual environment, '.' hides the folder depending on your operating system settings
    ├── my_python_project/   # The main package for your project, usually the app or project name
    │   ├── __init__.py
    │   ├── app.py           # The entry point to run the app code
    │   ├── module1.py
    │   └── module2.py
    ├── data/               # Data files and database.
    │   ├── __init__.py
    │   ├── processed_data.csv
    │   ├── my_database.db
    │   └── raw_data.csv
    ├── tests/               # Contains test code, "tests" is a name recognised by most test runners.
    │   ├── __init__.py
    │   ├── test_app.py      # Test modules usually start with 'test_' or end '_test'
    │   ├── test_module1.py
    │   └── test_module2.py
```

## Project and tool config files

These files were explained in week 1.

- requirements.txt in [1-02-environments.md](../1_structure/1-02-environments.md#requirementstxt)
- pyproject.toml in [1-02-environments.md](../1_structure/1-02-environments.md#pyprojecttoml)
- README.md in [1-03-source-code-control.md](../1_structure/1-03-source-code-control.md#readmemd)
- .gitignore in [1-03-source-code-control.md](../1_structure/1-03-source-code-control.md#gitignore)

## Activity: review project structure for the coursework

Review the structure for your coursework repository. Does your project structure look consistent with a typical
Python application project structure?

Using the src layout, or a flat layout, is encouraged as tools often auto recognise this by default, so avoiding the
need for additional configuration such as in `pyproject.toml` (see next activity).

There are examples of Python project structures on these sites:

- [Python Packaging User Guide](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/#src-layout-vs-flat-layout)
- [The Hitchhiker's Guide to Python](https://docs.python-guide.org/writing/structure/#sample-repository)
- [Real Python](https://realpython.com/python-application-layouts/)

[Next activity](3-07-imports.md)