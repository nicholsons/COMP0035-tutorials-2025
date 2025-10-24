# 3. Fixing issues with a formatter

The purpose of using is a linter is to identify the issues. The benefit however is only achieved once you fix the
identified issues. Running a linter is the easy part, the challenge is to then fix the identified issues.

Formatters are packages that will autoformat your code, e.g.

- [ruff](https://pypi.org/project/ruff/) - ruff can be used to detect and correct
- [Black](https://black.readthedocs.io/en/stable/)
- [autopep8](https://pypi.org/project/autopep8/) that you may wish to explore.

The tools use rules and correct your code to meet these. You may not always agree with the rules

PyCharm has options that will correct your code. If you are using PyCharm, try opening the code_to_lint.py and go to the
menu option 'Code | Format Code' and it should correct the spacing, line break and any indentation issues.

Both PyCharm and VS Code, particularly when you combine them with Copilot, will warn of style issues and offer
solutions.

Typically, where you see an error (by default a red squiggly underline in VS Code, or highlighted code in PyCharm, or a
lightbulb symbol); then the IDE will help you to fix it. Usually, clicking on the lightbulb will tell you what is wrong
and if possible, offer to fix it for you.

You will need to refer to the documentation for your IDE to work out how to identify warnings and use linting:

- [VS Code linting](https://code.visualstudio.com/docs/python/linting)
- [VS Code identify warnings](https://code.visualstudio.com/Docs/editor/editingevolved#_errors-warnings)
- [PyCharm Python code inspections](https://www.jetbrains.com/help/pycharm/running-inspections.html)
- [PyCharm fix problems](https://www.jetbrains.com/help/pycharm/resolving-problems.html)

Example of PyCharm style warnings, click on the warning triangle in the upper right of the code pane:

![PyCharm lint example](../img/pycharm-lint.png)

Example of VS Code style warning, hover over the squiggle to see the options:

![VS Code lint example](../img/vsc-lint.png)

NB: In VS Code, the warnings will not disappear as soon as you correct the code, you need to save the changes. The
linter appears to run only on save.

## Activity: Use a formatter to correct issues

Run commands in the terminal virtual environment.

1. Make a copy of [cq_code_to_reformat.py](../../src/activities/starter/cq_code_to_reformat.py) - this is just so you
   can repeat the activity later if you want. Open the file to see the issues but do not correct anything.
2. Run a linter: `flake8 src/activities/starter/cq_code_to_reformat.py`
3. Install autopep8: `pip install autopep8`
4. Auto-format the file: `autopep8 --in-place --aggressive --aggressive src/activities/starter/cq_code_to_reformat2.py`
5. Run a linter again: `flake8 src/activities/starter/cq_code_to_reformat.py`. Fewer issues should be reported.
6. Open the file again and see the changes that have been made.

[Next activity](3-04-github-actions.md)