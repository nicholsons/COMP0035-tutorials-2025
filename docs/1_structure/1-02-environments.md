# 2. Python virtual environments

## What is a virtual environment

A Python virtual environment is like a personal workspace for your Python project. It helps you:

- Keep things clean: It isolates your project’s packages from others on your computer.
- Control dependencies: You can install exactly the versions of libraries your project needs—no conflicts!

Using a virtual environment lets you build your Python project without affecting anything outside it. If you only use
your main Python environment you can experience issues when different projects require libraries of different versions
or that conflict.

A virtual environment, or **venv** is created in a directory, usually within your project, and includes:

- A copy (or symlink) of the Python interpreter you used to create it.
- A dedicated folder structure for installing packages (so they don’t mix with system-wide ones).
- Scripts to activate/deactivate the environment.

The structure of the venv looks a little different on macOS and Windows:

```text
.venv/
├── bin/                    # Contains executables like python, pip, and the activate script
│   ├── activate
│   ├── python
│   └── pip
├── lib/            
│   └── pythonX.Y/          # X.Y is your version of Python, e.g. 3.13
│       └── site-packages/  # Packages installed in this environment
├── pyvenv.cfg              # Configuration for this environment
```

and the Windows version:

```text
.venv/
├── Scripts/            # Contains executables like python, pip, and the activate script
│   ├── activate.bat
│   ├── python.exe
│   └── pip.exe
├── Lib/
│   └── site-packages/  # Packages installed in this environment
├── pyvenv.cfg
```

## Tools for creating a virtual environment

There are various tools for creating virtual environments and some also manage the packages within it.

These include venv, virtualenv, pipenv, conda, poetry, uv.

`venv` is the simplest tool and is bundled with Python so this will be referenced in all the activities for this minor.
However, if you are already familiar with another tool then continue to use it.

## Naming the virtual environment folder

The venv folder can be named anything, however good practice is to name it clearly so common names are: `venv`, `.venv`,
`env` or `.env`. The `.` denotes it as a hidden folder so depending on your operating system settings you may not see
the folder. You don't need to manually edit the venv folder so it is common to make it hidden.

## How to create and activate a virtual environment with venv

This is a 2-step process to create and then activate a virtual environment.

varies by operating system and by IDE.

- [VSCode](https://code.visualstudio.com/docs/python/environments)
- [PyCharm](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html)

A method that also works for most IDEs is to open a Terminal window within the IDE and enter
the [command syntax](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#create-and-use-virtual-environments)
for your operating system.

The following examples create a virtual environment in a folder called `.venv` using a Python tool named `venv`. The
second command then activates that environment.

e.g for MaxOS and Unix:

### Task: Create and activate
```bash
python3 -m venv .venv
source .venv/bin/activate
```

e.g. for Windows:

```bash
py -m venv .venv
.venv\Scripts\activate
```

There is a visual clue in the Terminal that the environment is activiated as the command prompt should now start with
the name of the venv in brackets, e.g. `(.venv)`. For example, mine looks like this:

```text
(.venv) sarahsanders@ML-F37Y6FG64V COMP0035-tutorials-2025 %   
```

NB For Windows users you may experience an issue activating a venv. It may be required to enable the Activate.ps1 script
by setting the [execution policy](https://go.microsoft.com/fwlink/?LinkID=135170) for the user. You can do this by
issuing the following PowerShell command at the prompt:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Adding packages to the virtual environment

You will need to add other Python packages (libraries) to the environment, including your own project's application
code.

There are various package management tools, however we will use `pip` for the same reason as we used `venv`, it is
already bundled with Python and is simple and sufficient for our needs. If you are already using tools such as conda or
poetry then continue to do so.

### pip

`pip` can install one or more packages at once, upgrade packages and delete them. Read more
on [pip here](https://pip.pypa.io/en/stable/user_guide/).

You can find a list of published Python packages, and the `pip` command to install them
on [the Python Package Index, PyPi](https://pypi.org)

A few common pip commands:

```shell
pip install pandas            # Install the latest version of pandas
pip install pandas matplotlib # Install the latest version of pandas and matplotlib
pip install pandas==1.19.5    # Install version 1.3.5 of pandas
pip install --upgrade pandas  # Upgrade to the latest version of pandas
pip uninstall pandas          # Uninstall, remove, pandas from the venv
pip list                      # List the current packages installed in the venv
pip freeze > requirements.txt # Take all the current packages installed in the venv and save the names and versions to a text file named requirements.txt
```

### Task: add pandas to the venv

In the Terminal where the venv is activated try installing one or more packages, e.g. pandas, matplotlib

Run `pip list` before and after you do so you can see what has been installed.

You may find that other packages are also listed, this is because packages can have their own dependencies that need to
be installed. For example, installing pandas also installs:

```text
Package         Version
--------------- -----------
numpy           2.3.2
pandas          2.3.1
python-dateutil 2.9.0.post0
pytz            2025.2
six             1.17.0
tzdata          2025.2
```

### requirements.txt

A common use case is to install multiple packages for a project using a file called `requirements.txt`. This is a file
that lists the additional libraries that are required for the project code to run.

This is useful to allows anyone to create a virtual environment and install the same packages and versions to run the
app code.

To install all the packages listed in a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

You can update the requirements.txt file with new libraries or different versions by editing the file. You can specify
just the package name, or you can also include information about the version to use. The requirements
file format
is [documented here](https://pip.pypa.io/en/stable/reference/requirements-file-format/#requirements-file-format).

Note: you cannot do this yet as you don't have a requirements.txt in this project folder yet.

### pyproject.toml

`pyproject.toml` is a file that is used to specify the build system requirements for the project to allow other
developers to build and run your code. It has a number of uses, including an alternative for listing the packages to be
installed.

More on [pyproject.toml here](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/).

There are many aspects that can be configured using pyproject.toml. Some of the tools, or packages, you use in the
project can be configured using parameters in this pyproject.toml file. For this reason there is no single correct
pyproject.toml, nor a single source of documentation.
Typically, if a package can be configured using pyproject.toml then it will have a reference to that in its own
documentation. For this course you are likely to use sections in pyproject.toml
for [setuptools](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html)
and [pytest](https://docs.pytest.org/en/6.2.x/customize.html#pyproject-toml)

For this course you will use pyproject.toml to install your own project application as a package in the venv.

To do this you can use the command `pip install -e .`

`-e` means install it in editable mode.

`.` means install it from a pyproject.toml in the current folder (usually the project root).

The minimum you will need to include in the pyproject.toml is:

```toml
# Basic project information
[project]
name = "hello-world-sample-project"
version = "2024.0.0"

# Most students will use setuptools, though poetry is also an option
[build-system]
requires = ["setuptools >= 61.0"]
build-backend = "setuptools.build_meta"

# Setuptools configuration see https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html#setuptools-specific-configuration
[tool.setuptools.packages.find]
where = ["src"]  # list of folders that contain the packages (["."] by default)
include = ["my_package*"]  # package names should match these glob patterns (["*"] by default)
exclude = ["my_package.tests*"]  # exclude packages matching these glob patterns (empty by default)
```

### Task: Create a pyproject.toml and install your own code

1. Create a new file in the project root. This is a plain text file. Take care to name it exactly `pyproject.toml` (all
   lowercase).

    ```text
    [project]
    name = "sample-project"
    version = "2025.0.0"
    
    [build-system]
    requires = ["setuptools >= 61.0"]
    build-backend = "setuptools.build_meta"
    ```

2. Enter the command `pip install -e .` in the Terminal window of your project where your venv is already activated.

You should see a new hidden folder (`.egg-info`) is created that has information about the installed project.

[Next activity](1-03-source-code-control.md)

## Further information

[The Hitchhiker's Guide to Python: Structuring your project](https://docs.python-guide.org/writing/structure/)

[Python Packaging User Guide: Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)

[freeCodeCamp: How to Build Your Very First Python Package](https://www.freecodecamp.org/news/build-your-first-python-package/)

[Real Python: Python Application Layouts: A Reference](https://realpython.com/python-application-layouts/)

[setuptools: Package Discovery and Namespace Packages](https://setuptools.pypa.io/en/latest/userguide/package_discovery.html)

[setuptools: Data Files Support](https://setuptools.pypa.io/en/latest/userguide/datafiles.html)

