# 1. Python project structure

_*Theme: Working with code for applications*_

Before you start make sure you have created a GitHub account and have installed Python, git and a Python IDE e.g. Visual
Studio Code or PyCharm Professional. If you have not, go to [computer setup](1-06-opt-computer_setup.md).

## What is a Python project?

A Python project is a structured collection of Python files and resources that work together to solve a specific problem
or build an application. It typically includes:

- Python scripts or modules (.py files) containing the logic
- A main entry point (like main.py or app.py)
- Dependencies, other packages that your code needs to run
- Configuration files
- Optional assets such as data files, templates, or documentation

## Using an IDE to work with Python projects

An IDE (Integrated Development Environment) is a software application that provides tools to help programmers write,
test, and debug code. It combines features that are intended to make writing code more efficient.

There are numerous IDEs for writing Python code, online and standalone.

The course materials refer to VS Code and PyCharm, though neither is mandatory for the course. Notebooks e.g. Jupyter,
are not suitable for this course as these differ from an IDE and don't provide the support for the range of tools and
techniques that you will need to use in this minor. Notebooks are explicitly excluded for the coursework.

## Project file structure: directories, packages, modules and files

There is no single correct structure for a Python project. A common layout is one referred to as the 'src' layout which
for a project with data files might look like this:

Various configuration files for the project code and tools used in the project are placed in the root. An explanation of
the more common files found here is given in a later activity in this document.

The Python code for the application is in a Python package in the **src** directory. "src" is short for "source code".

The application code is within a Python package called **my_package**. A package is a directory that contains an
`__init__.py` file (even if it's empty). A package can include multiple Python files (modules) and sub-packages. A
package allows for organized, modular code and supports importing e.g. `from my_package import some_module`.

A module is a single Python file. That file contains code and the code can be structured within it in classes, functions
or procedural code.

Test code is in a separate **tests** folder. This can also be a package, but it does not need to be.

The **data** folder may be at the root level, or within the `my_project` package. This has implications for how the data
files are referenced.

The **.venv** directory is a structure with code to create a Python virtual environment. This is explained later in this
week's activities.

```text
my_project_name/
├── README.md              # Gives info to others on your project and how to use the it
├── pyproject.toml         # Project metadata and dependencies
├── requirements.txt       # Project dependencies
├── .gitignore             # Files to exclude from Git
├── .env                   # Variables specific to this Python project environment     
├── data/                  # Data files
│   ├── my_data.csv
│   └── my_database.db
├── src/                   # Application code         
│   ├── my_app/                 
│   │   ├── __init__.py
│   │   ├── main.py (or app.py)    
│   │   └── some_module.py          
├── tests/                  # Test code
│   ├── conftest.py
│   └── test_some_module.py    
└── .venv/                  # Python virtual environment
```

## Task: Create a project in your IDE

Good practice for the project name is to:

- keep the project name brief but descriptive
- use all lowercase
- do not have spaces in the name, use underscored if you need to separate words
- avoid non-ASCII characters
- avoid names that conflict with reserved words such as test, setup or python
- avoid names that conflict with existing packages (this may be more difficult and not strictly an issue for the
  coursework, you can check existing packages in [PyPi](https://pypi.org))

How you create a new project will vary by IDE. For example:

- In [VS Code you open folder](https://code.visualstudio.com/docs/getstarted/getting-started)
-
In [PyCharm you create a new python project](https://www.jetbrains.com/help/pycharm/creating-and-running-your-first-python-project.html)

Either of the above will create a new folder (directory) on your computer in the location you specify using a name you
specify.

During the rest of this week's activities, you will learn to use many of the default files shown in the project
structure.

[Next activity](1-02-environments.md)

## Further reading
There are examples of typical Python project structures on these sites:

- [Python Packaging User Guide](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/#src-layout-vs-flat-layout)
- [The Hitchhiker's Guide to Python](https://docs.python-guide.org/writing/structure/#sample-repository)
- [Real Python](https://realpython.com/python-application-layouts/)