# 1. Working with Pandas

Read and complete actions before moving to the next activity.

## Introduction

This minor focuses on developing data-driven software applications using Python.

Writing code for applications differs to simply writing code that functions. COMP0035 focuses on the supporting
practices.

In this tutorial, you are asked to write code considering how the code could be re-used as part of an application. This
implies also that other developers may use your code so your code needs to run for anyone, not just yourself.

This tutorial expects you to:

- Use modules, packages and functions to structure your application code
- Import modules, packages and functions in your code
- Access data files in a way that is not specific only to your computer

## Project directory structure

Last week you cloned the activities repository to a project in your IDE and created a virtual python environment.

Check if you already installed the tutorial code by running `pip list`. The output should have something like:

```text
Package            Version     Editable project location
------------------ ----------- -----------------------------------------------------------
astroid            3.3.11
comp0035-tutorials 2025.0.1    /path_on_your_computer/your_projects/COMP0035-tutorials-2025
contourpy          1.3.3
```

If not then install an editable version of your own code in it using `pip install -e .`.

This tells your IDE about the structure of your COMP0035 tutorials project, that you have a directory called 'src' which
contains packages. Packages by default are auto discovered in the root of a project, not in a non-package subdirectory.

The code package location is defined in `pyproject.toml`.

The project structure can contain the following:

- A Python [module](https://docs.python.org/3/tutorial/modules.html) is "a file containing Python definitions and
  statements. The file name is the module name with the suffix .py appended."
- A Python [package](https://docs.python.org/3/tutorial/modules.html#packages) is "a way of structuring Python’s module
  namespace by using 'dotted module names'. For example, the module name A.B designates a submodule named B in a package
  named A." There is a more advanced concept, 'namespace packages', in Python that is not covered in this minor.
- A Python [function](https://docs.python.org/3/glossary.html#term-function) is "A series of statements which returns
  some
  value to a caller. It can also be passed zero or more arguments which may be used in the execution of the body."
- Directories (or folders) and files that are not Python code files, e.g. data files such as `.csv`, `.xlsx`;
  or database files such as `.sqlite` or `.db` files.
- Project configuration and information files e.g. README.md, .gitignore, pyproject.toml etc.

## ACTIVITY: Create a package and module for the tutorial activities

In the src/activities folder create a package (folder) for your work. Give it a meaningful name so you know this is your
code solutions to the activities, e.g. 'solutions', 'student', 'my_code'.

Inside the folder you just created, add a python file named exactly like this: `__init__.py` (you might already have
this, some IDEs add it for you when you add a new package)

Now create a new python file, a module, in that package folder for the tutorial activities. Note: Do not call it
pandas.py as it could conflict with the pandas package!

## File locations

### The problem with file paths

You will be using data files that are stored in your project's directory structure. You will need to be able to
reference the location of these files in your Python code.

If you hard-code the file paths that are specific to your computer when writing code that others will use issues will
arise due to:

1. Windows and Unix/Mac file paths are different.

   Consider a Mac/Unix style file path `/Users/jojo/py_project/test.py`
   and a Windows file path `C:\\Documents\py_project\test.py`. The syntax and structure are different. Further where you
   have the files for a project on your computer is likely different to where someone else does, so using shared code
   where file paths are written using a particular operating system format using a given person's directory structure
   quickly becomes problematic.

2. The root folder can differ depending on your code editor.

   If you are writing code in VSCode and PyCharm then filepath roots are typically the project root, that is you can add
   paths that are relative to your project root and ignore the preceding local file system directory structure. As an
   example a file in the data folder would be `data/file.csv` and not `C:\\Documents\py_project\data\file.csv`
   Different environments and editors may set the project root differently.

3. The relative path can differ depending on where the code is called from.

   If you use a file path in a code file so that it is relative to the current file, you are likely to get issues if you
   then import that file and execute it from another. For example:
   You have the following directories and files: `/data/datafile.csv`, `/module_a/code_a.py`
   and`/module_a/module_b/code_b.py`. In `code_a.py` if you reference the datafile using `../data/datafile.csv` in a
   function that you then import and use inside `code_b.py` you might get an issue as relative to `code_b.py` the data
   file is not in `../data/datafile.csv` but in `../../data/datafile.csv`. It's a little more complex than this,
   however, using relative file paths can lead to problems.

   When you are working with packages in Python then relative paths are relative to the current working directory rather
   than the code file it is written in.

4. Referencing files in web apps introduces further complexity.

   In web apps you will also need to consider that where files are located on a development platform for example is
   likely different to that of the deployed version. This isn't covered in COMP0035.

### Using Python libraries to determine the path

There are different ways you can do this in Python, and differing opinions on which is best.

#### Using `pathlib`

One approach is to use the `os` or `pathlib` package, both are part of the base Python installation. These allow you to
define relative paths to the file i.e. locate a file relative to another. Pathlib is newer, it:

- Avoids the `\\` versus `/` issue by using the Pathlib `joinpath` method.
- Has methods that let you determine the current working directory e.g. `pathlib.Path.cwd()`. For
  example: `my_file_path = pathlib.Path.cwd().joinpath('data','datafile.csv')` instead of `data/datafile.csv`
  or `data\datafile.csv`
- Allows you to code relative to the current code file, whatever that file is
  e.g. `pathlib.Path(__file__).parent` would go to the directory that is the parent of the current file.

For example, given the file structure below:

```text
my_python_project/   (root)
├── this_script.py
├── data/
│   ├── example.csv
```

Then pathlib can be used in `this_script.py` to locate the `example.csv` file:

```python
from pathlib import Path

# This script is located in the project root, so find the path to the current file and then go to the parent of that file
project_root = Path(__file__).parent

# Find the .csv file relative to the project root and join to that path the data folder and then the example.csv file
csv_file = project_root.joinpath('data', 'example.csv')
# csv_file = project_root / 'data' / 'example.csv' # this notation would also work, even though you think the '/' is only unix/macOS

# Check if the file exists, this will print 'true' if it exists
print(csv_file.exists())
```

`Path(__file__)` refers to the file in which the code is i.e. `this_script.py`
`.parent` refers to the parent that the `this_script.py`is in, so `my_python_project` which is the project root, the
highest folder in the project
`.joinpath` takes the current location in this case `my_python_project` and joins to that the `data` directory and then
the `example.csv` so will be `my_python_project/data/example.csv`

You can use the same technique to navigate up through multiple hierarchical directories, 'parents', so given the next
scenario where the script and the data are in different subdirectories:

```text
my_python_project/   (root)
├── src/
│   ├── this_script.py
├── data/
│   ├── example.csv
```

then you can use pathlib like this:

```python
from pathlib import Path

# This script is located in a subfolder so you need to navigate up to the parent (src) and then its parent (project root), then down to the 'data' directory and finally the .csv file
csv_file = Path(__file__).parent.parent.joinpath('data', 'example.csv')
csv_file_v2 = Path(__file__).parent.parent / 'data' / 'example.csv'  # also works

# Check if the file exists
if csv_file.exists():
    print(f"CSV file found: {csv_file}")
else:
    print("CSV file not found.")
```

#### Using `importlib resources`

An alternative approach that is available from Python v10 onwards is
the [method recommended in the setuptools guide](https://setuptools.pypa.io/en/stable/userguide/datafiles.html#accessing-data-files-at-runtime).

This uses the [
`importlib.resources` package](https://docs.python.org/3.11/library/importlib.resources.html#module-importlib.resources)
from Python.

```python
from importlib import resources

from activities import data


paralympics_data_file_csv = resources.files(data).joinpath("paralympics_raw.csv")
```

## ACTIVITY: Add code to reference a .csv file

In the Python module you created earlier add code to locate the data file `paralmpics_raw.csv`.

Try using `pathlib.Path` and the `importlib.resources` approach i.e. do the activity twice using a different approach
each time.

_Optional_, check you can access the file by opening and printing a line e.g.:

```python
import csv

if __name__ == '__main__':
    data_file =  # Your code that locates the file

    with open(data_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        first_row = next(csv_reader)
        print(first_row)

```

Delete the csv reader code once you've demonstrated your file is accessed. You won't be using `csv` to read the files.

[Next activity](2-02-pandas-df)