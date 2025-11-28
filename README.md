# COMP0035 2025-26 Weekly practical activities

This repository contains the activities for the COMP0035 module for the academic year 2025-26.

## Instructions for using this repository

1. Fork this repository to your own GitHub account.
2. Clone the forked repository to your local machine (e.g. in VS Code or PyCharm).
3. Each week, update the repository using the 'Sync fork' button in GitHub to check for changes, if it is out of date
   then select the 'Update branch' button.

## Activity instructions and code files

The `docs` folder contains the activity instructions for each week.

The `src` package contains any starter code for each week. You can also use this package to store your own code
that you create during the activities.

One solution to the week's activities will be added to the [tutor_solution repository](https://github.com/nicholsons/comp0035-tutorials-solutions). Other solutions will be
possible, and some may be better than the solution offered, so don't feel
your code has to match the tutors code!

git add .
git commit -m"Week 1 tutorial done!"
git push

## List of activity instructions

This will be updated each week with the activities for that week.

### Week 1 Source code control, environment, structure

_*Theme: Working with code for applications*_

Required:

1. [Python project structure](docs/1_structure/1-01-structure.md)
2. [Python virtual environment](docs/1_structure/1-02-environments.md)
3. [Source code control (GitHub)](docs/1_structure/1-03-source-code-control.md)
4. [Set up the course activities project and repository](docs/1_structure/1-04-activities-repo.md)
5. [Set up the coursework project and repository](docs/1_structure/1-05-coursework-repo.md)

Optional:

6. [Computer setup for COMP0035](docs/1_structure/1-06-opt-computer_setup.md)
7. [Integrate your IDE with GitHub](docs/1_structure/1-07-opt-integrate-IDE-GitHub.md)
8. [Using CoPilot in VS Code and PyCharm](docs/1_structure/1-08-opt-copilot-ide.md)

### Week 2 Pandas to describe, explore and prepare a dataset

_*Theme: Using Python to work with data*_

This week's activities are more than you can complete in a week. There are less in weeks 4 and 5 so you could delay
some.

[Week 2 instructions](docs/2_pandas/2-0-instructions.md) are in the docs/2_pandas folder:

1. [Create a package and module](docs/2_pandas/2-01-python-structure)
2. [Open .csv and .xlsx files and create a DataFrame](docs/2_pandas/2-02-pandas-df)
3. [Describe the dataframe](docs/2_pandas/2-03-pandas-describe)
4. [Identify missing values](docs/2_pandas/2-04-missing-values-identify.md)
5. [Overview of plots](docs/2_pandas/2-05-plot-overview.md)
6. [Plots to show distributions](docs/2_pandas/2-06-plot-distribution.md)
7. [Plots for timeseries data](docs/2_pandas/2-07-plot-timeseries.md)
8. [Columns with categorical values](docs/2_pandas/2-08-categorical-data)
9. [Data preparation](docs/2_pandas/2-09-data-prep.md)
10. [Locating rows and columns](docs/2_pandas/2-10-locating-rows-cols.md)
11. [Remove columns](docs/2_pandas/2-11-removing-columns.md)
12. [Remove and replace values](docs/2_pandas/2-12-resolve-missing-incorrect-values.md)
13. [Change data types](docs/2_pandas/2-13-change-datatypes.md)
14. [Add new data by computing](docs/2_pandas/2-14-new-column.md)
15. [Add new data by combining dataframes](docs/2_pandas/2-15-joining-dataframes.md)
16. [Save dataframe to file](docs/2_pandas/2-16-save-df-to-file.md)
17. [Check the prepared data suits the purpose](docs/2_pandas/2-17-questions.md)
18. [Next steps](docs/2_pandas/2-18-next-steps.md)


### Week 3 Code quality: linting, docstrings, exception handling, project structure and imports

_*Theme: Working with code for applications*_

[Week 3 instructions](docs/3_code_quality/3-0-instructions.md) are in the docs/3_code_quality folder:

1. [Docstring](docs/3_code_quality/3-01-docstrings.md)
2. [Linting](docs/3_code_quality/3-02-linting.md)
3. [Auto-formatting](docs/3_code_quality/3-03-formatter.md)
4. [GitHub Actions lint report](docs/3_code_quality/3-04-github-actions.md)
5. [(Optional) Static analysis: beyond linting](docs/3_code_quality/3-05-static-analysis.md)
6. [Project structure](docs/3_code_quality/3-06-project-structure.md)
7. [Imports](docs/3_code_quality/3-07-imports.md)
8. [Error handling](docs/3_code_quality/3-08-error-handling.md)

### Week 4 Database design; sqlite3

_*Themes: Designing applications*_ & _*Using Python to work with data*_

This week's activities are more than you can complete in a week. There are less in weeks 4 and 5 so you could delay
some.

[Activity instructions](docs/4_database/4-0-instructions.md) are in the docs/4_database folder:

1. [Introduction to database design (lecture recap)](docs/4_database/4-01-database-design.md)
2. [Introduction to ERD (lecture recap) and ERD drawing tools](docs/4_database/4-02-erd-intro.md)
3. [Conceptual database design](docs/4_database/4-03-conceptual-design.md)
4. [Logical design to 1NF](docs/4_database/4-04-logical-design-1nf.md)
5. [Logical design to 2NF](docs/4_database/4-05-logical-design-2nf.md)
6. [Logical design to 3NF](docs/4_database/4-06-logical-design-3nf.md)
7. [Logical design - constraints](docs/4_database/4-07-logical-design-constraints-data.md)
8. [Logical design - referential integrity](docs/4_database/4-08-logical-design-constraints-fk.md)
9. [Logical design activity](docs/4_database/4-09-logical-design-activity.md)
10. [Physical design - SQLite schema](docs/4_database/4-10-physical-design-structure.md)
11. [Physical design - Python to create SQLite database structure](docs/4_database/4-11-physical-design-create-db.md)
12. [Database design - next steps](docs/4_database/4-16-next-steps.md)
13. [SQL INSERT and SELECT intro](docs/4_database/4-12-sql-add-data.md)
14. [Add data to tables with no FK](docs/4_database/4-13-insert-no-fk.md)
15. [Select data](docs/4_database/4-14-select-query.md)
16. [Add data to tables with an FK](docs/4_database/4-15-insert-with-fk.md)
17. [Normalisation and application code](docs/4_database/4-17-normalisation-tradeoff.md)- A brief intro to the trade-off
    between database normalisation and query design


<hr>

**Activities after this point relate to coursework 2**

<hr>

### Week 5 Database to Python class: ORM

_*Theme: Using Python to work with data*_

[Week 5 instructions](docs/5_classes_orm/5-0-instructions.md)are in the docs/5_classes_orm folder:

1. [Python classes](docs/5_classes_orm/5-01-class.md)
2. [Class relationships - inheritance, composition](docs/5_classes_orm/5-02-inheritance-composition.md)
3. [Pydantic](docs/5_classes_orm/5-03-pydantic.md)
4. [ORM and SQLModel](docs/5_classes_orm/5-04-orm-sqlmodel.md)
5. [Using SQLModel to create SQLite database](docs/5_classes_orm/5-05-sqlmodel-create-db.md)
6. [Using SQLModel to add data](docs/5_classes_orm/5-06-sqlmodel-add-data.md)
7. [Summary](docs/5_classes_orm/5-07-summary.md)
8. Optional [Using SQLAlchemy in place of SQLModel](docs/5_classes_orm/5-08-sqlalchemy.md)

### Week 6 Requirements; interface design

_*Theme: Designing applications*_

[Instructions](docs/6_requirements/6-0-instructions.md) in the docs/6_requirements folder:

1. [Introduction](6-01-introduction.md)
2. [Identify requirements](6-02-identify-requirements.md)
3. [Document requirements](6-03-document-requirements.md)
4. [Prioritise requirements](6-04-prioritise-requirements.md)
5. [Draw wireframes](6-05-wireframes.md)

### Week 7 Application design

_*Theme: Designing applications*_

[Instructions](docs/7_app_design/7-0-instructions.md) are in the docs/7_app_design folder:

1. [Introduction to application design](docs/7_app_design/7-01-introduction.md)
2. [Examples of application designs](docs/7_app_design/7-02-diagram-examples.md)
3. [Identify classes](docs/7_app_design/7-03-identify-classes.md)
4. [Draw the application design diagram](docs/7_app_design/7-04-draw-design.md)
5. [Review the design](docs/7_app_design/7-05-review-design.md)
6. [Draw the application design for the paralympics prediction web app](docs/7_app_design/7-06-design-medals.md)
7. [Results of using genAI for the application design](docs/7_app_design/7-07-genAI.md)

### Week 8 Classes and database 2

_*Theme: Using Python to work with data*_

[Instructions](docs/8_classes_database_2/8-0-instructions.md) are in the docs/8_classes_database_2 folder:

1. [Adding methods to classes](docs/8_classes_database_2/8-01-methods.md)
2. [Tables with relationships in SQLModel](docs/8_classes_database_2/8-02-relationships.md)
3. [Add data using SQLModel](docs/8_classes_database_2/8-03-insert.md)
4. [Add data to tables with relationships](docs/8_classes_database_2/8-04-insert-multiple.md)
5. [Selecting data from a database with SQLModel](docs/8_classes_database_2/8-05-select.md)
6. [Update data in a database with SQLModel](docs/8_classes_database_2/8-07-update.md)
7. [Delete data from a database with SQLModel](docs/8_classes_database_2/8-06-delete.md)
8. [Reminder: code quality still matters!](docs/8_classes_database_2/8-08-quality.md)
9. [SQLModel queries for the paralympics database](docs/8_classes_database_2/8-09-paralympics-queries.md)

### Week 9 Unit testing, CI and coverage

_*Theme: Working with code for applications*_

[Instructions](docs/9_testing/9-0-instructions.md) and activities can be found in the docs/9_testing folder:

1. [Introduction to testing and conventions](docs/9_testing/9-01-introduction.md)
2. [Testing with pytest](docs/9_testing/9-02-pytest-tests.md)
3. [Pytest fixtures](docs/9_testing/9-03-fixtures.md)
4. [Reporting test coverage](docs/9_testing/9-04-coverage.md)
5. [Running tests with GitHub Actions](docs/9_testing/9-05-ci-github.md)
6. [Further information](docs/9_testing/9-06-further.md)

### Week 10 No new activities

Tutorial reserved for final coursework support

## Data set

Most activities use paralympics data that was originally compiled from
the [IPC website](https://www.paralympic.org/paralympic-games) in 2021.

The data may be duplicated in some instances in `src/data` and other sub-folders in `src`. This is for teaching purposes
for an activity that requires a different copy or location.

### External examples using similar paralympics data

[Onyx data challenge 2024](https://zoomcharts.com/en/microsoft-power-bi-custom-visuals/challenges/onyx-data-september-2024?utm_source=youtube&utm_medium=social&utm_campaign=onyx_september24_workshop&utm_content=ZcHeader)
