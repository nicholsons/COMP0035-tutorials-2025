# 5. (Optional) Static analysis: beyond linting

**This activity is optional**, you can skip to the [next activity](3-06-project-structure.md).

Linters belong to a category of tools referred to as 'static analysers', that is tools that check or analyse code but
don't change it.

As well as linters, there are tools that check for:

- cyclomatic complexity [mccabe](https://github.com/PyCQA/mccabe)
- security vulnerabilities [bandit](https://bandit.readthedocs.io/en/latest/)
- duplicated code [PMD CPD](https://pmd.github.io/pmd/pmd_userdocs_cpd)

Some tools combine several tools in one such as [prospector](https://pypi.org/project/prospector/)

## Cyclomatic complexity

Cyclomatic complexity is a metric used to measure the complexity of a program by quantifying the number of
independent paths through its source code. It was introduced by Thomas McCabe in 1976 and is used in
assessing how difficult a function or module might be to test or maintain.

The code in `paralympics_add_data.py` is more complex than other code in the examples so try the following:

1. `pip install mccabe`
2. `python -m mccabe src/activities/starter/paralympics_add_data.py`

While there are no specific rules as to what is an acceptable or desired level of complexity. 10 is often cited as a
score that indicates excessively complex code that could be more efficiently broken down into smaller, more manageable
parts.

NB you can also configure flake8 and ruff to report on complexity.

## Combined tools

Try using prospector to see the combined output of several static analysis tools:

1. `pip install prospector`
2. `prospector src/activities/starter/paralympics_add_data.py`

Results in:

```text
src/activities/starter/paralympics_add_data.py
  Line: 3
    pylint: line-too-long / Line too long (103/100)
  Line: 72
    pylint: f-string-without-interpolation / Using an f-string that does not have any interpolated variables (col 19)
  Line: 80
    pylint: f-string-without-interpolation / Using an f-string that does not have any interpolated variables (col 27)
  Line: 94
    pylint: line-too-long / Line too long (101/100)
  Line: 102
    pylint: line-too-long / Line too long (109/100)
    pylint: f-string-without-interpolation / Using an f-string that does not have any interpolated variables (col 31)
  Line: 104
    pylint: line-too-long / Line too long (102/100)
  Line: 115
    pylint: line-too-long / Line too long (102/100)
  Line: 128
    pylint: line-too-long / Line too long (110/100)
  Line: 131
    pylint: line-too-long / Line too long (101/100)
  Line: 137
    pylint: line-too-long / Line too long (101/100)
  Line: 153
    pylint: line-too-long / Line too long (102/100)
  Line: 225
    pylint: line-too-long / Line too long (111/100)



Check Information
=================
         Started: 2025-09-20 19:54:22.789916
        Finished: 2025-09-20 19:54:24.494414
      Time Taken: 1.70 seconds
       Formatter: grouped
        Profiles: default, no_doc_warnings, no_test_warnings, strictness_medium, strictness_high, strictness_veryhigh, no_member_warnings
      Strictness: Noneprospector --no-django src/activities/starter/paralympics_add_data.py
       Tools Run: dodgy, mccabe, profile-validator, pycodestyle, pyflakes, pylint
  Messages Found: 14
 External Config: pylint: /PycharmProjects/COMP0035-tutorials-2025/pyproject.toml
```

[Next activity](3-06-project-structure.md)