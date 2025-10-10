# Introduction and pre-requisites

_*Theme: Using Python to work with data*_

## Pre-requisites

1. Completed coding activities 1
2. Forked the [COMP0035 tutorials 2025 repository](https://github.com/nicholsons/COMP0035-tutorials-2025), cloned it to
   your computer, and set up a project with a virtual environment within your IDE (VS Code or PyCharm).

### 1. Update the forked tutorials repository

Login to GitHub and navigate to your forked copy of
the [COMP0035 tutorials 2025 repository](https://github.com/nicholsons/COMP0035-tutorials-2025).

Check whether any changes have been made. For example, the image below shows 1 new commit has been made to the
original (2024 version shown, you must use 2025).
![Sync the forked repository](../img/gh-synch-fork.png)

If changes have been made, you will need to update your forked repository.

Click on the "Synch fork" button; and then on "Update branch".
![Update branch](../img/gh-update-branch.png)

Now, open your IDE (VS Code, PyCharm) and update the local copy of the repository. This assumes you have integrated your
IDE with your GitHub account in week 1. You may be prompted to log in to GitHub before you can carry out the
following.

- In PyCharm try menu option Git > Pull
- In VS Code click on the source code control icon on the left side panel, then when the source code control pane opens,
  click on the three dots and select Pull.

There are other methods, look in the Help for either PyCharm or VSCode.

### 2. Check you have the virtual environment activated

Open a terminal window within your IDE in the project directory.

Check that your virtual environment is activated. There are various ways to do this, IDEs vary, usually a quick visual
way is to check whether the prompt starts with `(.venv)` or the name if your venv folder if not `.venv`. You can also
use Python in the Terminal:

```python
import os

print(os.environ.get('VIRTUAL_ENV'))
```

The following screenshot shows this in PyCharm on macOS:

![Check for active venv](../img/venv-check.png)

If you are not in a venv, refer to activating a virtual environment
in [Week 1 activity 2](../1_structure/1-02-environments.md).

### 3. Check you have the required libraries installed in the virtual environment

Open the Terminal in your IDE.

At the prompt, enter: `pip list`

This outputs a list of installed Python packages and their versions. Check for `pandas` and `openpyxl`.

If missing, install these using `pip` e.g.  `pip install pandas openpyxl`

<sup>1</sup> The default installation of pandas can only open Excel `.xlsx` files with an additional library called `openpyxl` <sup>1</sup>.

## Complete the activities

This set of activities use Python pandas to describe, explore and prepare data from one or more raw data files (data
set). The activities also introduce you to writing code in a way that is potentially re-usable in a project.

The activities in weeks 2, 3 and 4 are not evenly balanced, with more in week 2 and less in week 4. If you can't
complete this set of activities within the week, continue in a later week.

1. [Create a package and module](2-01-python-structure)
2. [Open .csv and .xlsx files and create a DataFrame](2-02-pandas-df)
3. [Describe the dataframe](2-03-pandas-describe)
4. [Identify missing values](2-04-missing-values-identify.md)
5. [Overview of plots](2-05-plot-overview.md)
6. [Plots to show distributions](2-06-plot-distribution.md)
7. [Plots for timeseries data](2-07-plot-timeseries.md)
8. [Columns with categorical values](2-08-categorical-data)
9. [Data preparation](2-09-data-prep.md)
10. [Locating rows and columns](2-10-locating-rows-cols.md)
11. [Remove columns](2-11-removing-columns.md)
12. [Remove and replace values](2-12-resolve-missing-incorrect-values.md)
13. [Change data types](2-13-change-datatypes.md)
14. [Add new data by computing](2-14-new-column.md)
15. [Add new data by combining dataframes](2-15-joining-dataframes.md)
16. [Save dataframe to file](2-16-save-df-to-file.md)
17. [Check the prepared data suits the purpose](2-17-questions.md)
18. [Next steps](2-18-next-steps.md)
