# 2. Use pandas to open .csv and .xlsx files and create a DataFrame

## Read: Data and questions

The data in the activities is from the following
source: [Paralympic medals and event info](https://www.paralympic.org/london-2012/results/medalstandings)

The data is saved in the `paralympics_raw.csv` file. Some data quality issues have been introduced such that it can be
used for the tutorial activities.

In the activities you will be describing and exploring a dataset, and then preparing it for used in a scenario.

## Pandas DataFrame overview

You may have seen spreadsheets that contain data in rows and columns, where the columns represent variables and
the rows the values of those variables for a particular instance.

The paralympics data has data in rows with variables names in columns:

![Raw data set table](../img/data_raw.png)

The data values can be a mix of data types: integers, text, dates, etc.

The pandas library has many functions for analysing, cleaning, exploring and manipulating data. Pandas works with
one-dimensional data array using pandas Series, and with two-dimensional data using the pandas DataFrame. Each of these
has functions. These activities use Pandas DataFrame since the data is two-dimensional.

You can create a pandas DataFrame in a number of ways -
see [pandas documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html). In this course you will
typically create it by reading data that is stored in a `.csv` or `.xlsx` file.

## ACTIVITY: Read .csv and .xlsx into a DataFrame

There are two data files in the `src/activities/data/` package:

- [paralympics_raw.csv](../../src/tutorialpkg/data/paralympics_events_raw.csv) - a .csv file with data about paralympic games
- [paralympics_all_raw.xlsx](../../src/tutorialpkg/data/paralympics_all_raw.xlsx) - an Excel file with 2 worksheets, the first with the data about paralympic games, the second with the medal tables of the competing teams

Use a different Pandas function for each type of file:

- [pandas.read_csv](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html) for csv files
- [pandas.read_excel](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html) for xlsx files

The linked documentation for each function shows the options that can be applied such as selecting which columns to
import, setting data types for columns, etc.

In the 'main' section:

1. You already have a variable that locates the file `/activities/data/paralympics_raw.csv`. Add a second variable to
   locate the .xlsx file `activities/data/paralympics_all_raw.xlsx`.
2. Add code to the function to read the contents of the .csv file into a pandas DataFrame using
   `variable_name_for_df = pd.read_csv(your_filepath_variable)`.
3. Add code to read the .xlsx file into two further pandas DataFrames. The Excel file has several worksheets, by default
   `read_excel` will open the first worksheet. You can change this by
   specifying the worksheet e.g. `pd.read_excel(paralympics_datafile_excel, sheet_name=1)` reads the second worksheet (
   counts from 0), `pd.read_excel(paralympics_datafile_excel, sheet_name="name_of_sheet")` to read a sheet called '
   name_of_sheet'. Add code to read in each of the two sheets.
4. Run the code. It won't return anything if all is well. If you have errors, read the error messages to try and
   identify what is wrong and correct your code. Some common issues:

   `FileNotFoundError: [Errno 2] No such file or directory: '.../src/data/paralympics_raw.csv'` - check if the directory
   structure printed matches your directory structure

   ```text
     Traceback (most recent call last):
        File ".../src/tutorialpkg/data_prep/analyse_dataframe.py", line 55, in <module>
        paralympics_excel_df = pd.read_csv(paralympics_datafile_excel)
                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     <lines omitted here for brevity> 
     UnicodeDecodeError: 'utf-8' codec can't decode byte 0xde in position 16: invalid continuation byte
   ``` 
   This one is more tricky to detect as the issue is that `read_csv` has been used for a file that is an Excel data file
   instead of `read_excel`

   `ImportError: Missing optional dependency 'openpyxl'.  Use pip or conda to install openpyxl.` - you forgot to install
   openpyxl which is needed to read an Excel file. Install it in the virtual environment using `pip install openpyxl`


[Next activity](2-03-pandas-describe)