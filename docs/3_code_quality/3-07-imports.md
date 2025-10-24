# 7. Importing Python packages/libraries

You are already aware that to use Python packages in your code you import them. This activity covers guidance on how to
structure the imports, including how to import your own application packages and modules.

## Structuring imports

[PEP8](https://peps.python.org/pep-0008/#imports) says that:

- Imports should be at the top of the Python file
- Group imports in the following order with a blank space between each group
    - Standard library imports
    - Related third-party imports
    - Local application/library specific imports
- Order imports alphabetically within the group
- Avoid wildcard imports like `from module import *`
- Prefer absolute imports over relative imports

For example:

```python
# Standard library imports
import os
from math import pi

# Related third-party library imports
import pandas as pd
from plotly.graph_objs import Bar, Layout

# Local application specific imports
import my_module
from my_module import my_function
```

In PyCharm, the menu option Code > Reformat Code will automatically sort the imports in this order. Some formatters may
also.

## Importing your own code

To import your own packages and modules within your code depends on Python being able to locate them.

PEP8 states **prefer absolute imports to relative imports**.

**Relative imports** are a way to import modules based on their location relative to the current module (i.e. the
file doing the importing), rather than from the root of the project or the Python path, e.g., `from . import module_a`

**Absolute imports** to importing modules using their full path from the project's root directory. This is the most
common and recommended way to import modules, especially in larger projects. For example:
`from my_package import my_module` or `from my_package.my_module import my_function_one, my_function_two`.

Importing modules using their full path does not mean you have to specify the full directory path in the import. By
installing your own code in the Python environment allows it to determine the full path from the registered package
names. This is why it is important to install your own code as a package in the Python environment you are using for the
project.

### `pip install -e .` with `pyproject.toml`

Executing `pip install -e .` in the Python venv installs your project and any dependencies that are specified in
`pyproject.toml`.

`-e` stands for "editable". It tells pip to install your project in a way that any changes you make to the source code
are immediately reflected when you run or import the package so there is no need to reinstall after every change.

`.` tells the pip to treat the current directory you are in as the root project directory when you run the command.
Make sure the `pyproject.toml` is in this root directory (i.e. the top level of the project). In most cases you should
be in the project root directory when you run `pip install -e .`.

What you specify in `pyproject.toml` is important. However, there is no single solution to this as it depends on your
project structure and the tool you are using to build the package. The examples in this course all assume you are using
`setuptools` to build the package; however if you are using poetry you will need to read the relevant poetry
documentation instead. There
is [guidance for writing pyproject.toml is here](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/) -
make sure you select setuptools in the code examples it gives you.

If you are using a default Python project structure with your app code in a `src` directory (note `src` is a plain
directory and not a Python package, there is no `src/__init__.py`), then setuptools and pip should auto discover your
packages. If you deviate from this, e.g. using a folder other than src that has code in, or you have multiple packages
in the root of the project folder, then you need to specify the package location for setuptools to find. Refer to
the [setuptools documentation](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html) for what to put in
the `[tool.setuptools.packages.find]` section of `pyproject.toml`.

If the data files are in a sub-package of your main application package then you should be able to import them without
further configuration in `pyproject.toml`. If you place them elsewhere then refer to
the [setuptools documentation for data files](https://setuptools.pypa.io/en/latest/userguide/datafiles.html).

### Checking that your own package code is installed

Execute the command `pip list` in the venv. It should list your project package name as one of the installed packages,
e.g.:

```text
(.venv) pip list
Package    Version Editable project location
---------- ------- -----------------------------------------
aproject    1       /Users/someone/aproject
pip        24.3.1
setuptools 80.9.0
```

If not, then execute the command `pip install -e .`. This should return a message such as "Successfully installed
myproject-2025.0.1" and you may see a folder created with the extension `.egg-info`, e.g. `myproject.egg-info`.

If it returns something else then check for the error messages in the output in the terminal.

For example:

>`Getting requirements to build editable did not run successfully.`

This indicates that you have more than one package at the root of the project so it cannot determine
which is the main package code. A solution is to move these into a 'src' directory or if you want to keep the
flat-layout then move them to be sub-packages of a single top level package.

```text
  × Getting requirements to build editable did not run successfully.
  │ exit code: 1
  ╰─> [14 lines of output]
      error: Multiple top-level packages discovered in a flat-layout: ['onepackage', 'anotherpackage'].
```

>`ERROR: file:///Users/sarahsanders/PycharmProjects/snake does not appear to be a Python project: neither 'setup.py'
nor 'pyproject.toml' found.`

This is often because you named `pyproject.toml` incorrectly; `pyproject.toml` isn't in the root folder; or you are
running the command while not in the project root folder.

## Data and database file locations

How to reference data files was already covered
in [2-01-python-structure.md](../2_pandas/2-01-python-structure.md#file-locations)

Please recap if you don't remember the guidance. Incorrectly referencing files frequently causes issues in coursework
submissions.

## Check the pyproject.toml for your project

- [Read the guidance](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#static-vs-dynamic-metadata)
  for the `[project]` section and include `name`, `version` and `dependencies`
- [Read the guidance](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#declaring-the-build-backend)
  for the `[build-system]` section using `setuptools`
- If not using `src/my_package` style layout, read
  the [guidance for setuptools package discovery](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html).

[Next activity](3-08-error-handling.md)