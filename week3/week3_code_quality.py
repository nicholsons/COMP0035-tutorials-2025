"""
COMP0035 – Week 3 Activities (Code Quality)
Each activity below corresponds to a Week 3 task. Comments explain what to do, and where.
"""

import os
import pandas as pd

# 📘 ACTIVITY 1: Docstrings
def calculate_area(radius):
    """
    Calculate the area of a circle.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    return 3.14159 * radius ** 2


def generate_histogram(values):
    """
    Generate a textual histogram using a list of values.

    Each value will be represented as a row of asterisks (*), where the number of asterisks equals the value.

    Args:
        values (list of int): A list of integers representing the values to plot.

    Returns:
        list of str: A list of strings, each string is a row of the histogram.
    """
    return ["*" * value for value in values]


def describe(values):
    """
    Return basic statistics for a list of numeric values.

    Calculates the minimum, maximum, average and number of items in the list.

    Args:
        values (list of float): The numeric values to describe.

    Returns:
        dict: A dictionary with keys 'min', 'max', 'mean', and 'count'.
    """
    return {
        "min": min(values),
        "max": max(values),
        "mean": sum(values) / len(values),
        "count": len(values),
    }


if __name__ == "__main__":
    # Load sample data from paralympics_raw.csv
    paralympics_path = "/Users/ismaelblanca/Downloads/UCL CHEM ENG/Year 3/COMP0035/COMP0035-tutorials-2025/src/activities/data/paralympics_raw.csv"
    
    try:
        df = pd.read_csv(paralympics_path)

        # EXAMPLE 1: Use 'sports' column to generate histogram
        sports_values = df['sports'].dropna().astype(int).tolist()
        histogram_output = generate_histogram(sports_values[:10])  # Just first 10 to keep it short
        print("\n📊 Histogram (based on 'sports' column):")
        for line in histogram_output:
            print(line)

        # EXAMPLE 2: Use 'participants' column for stats
        participants = df['participants'].dropna().astype(float).tolist()
        stats = describe(participants)
        print("\n📈 Stats (based on 'participants' column):")
        print(stats)

    except Exception as e:
        print(f"Error loading Paralympics CSV: {e}")


# 🧽 ACTIVITY 2: Linting
# ----------------------------------------
# This is run OUTSIDE of Python, in the Terminal.
# Step-by-step:
# 1. Open your terminal and navigate to the folder with this file:
#    cd path/to/your/folder
# 2. Then run:
#    flake8 week3_code_quality.py
# This will print out any linting issues in your code.


# 🛠️ ACTIVITY 3: Auto-formatting
# ----------------------------------------
# Run this from the terminal to auto-fix formatting:
# Option 1: Using Black (recommended)
#    black week3_code_quality.py
#
# Option 2: Using autopep8
#    autopep8 --in-place --aggressive week3_code_quality.py


# 🔁 ACTIVITY 4: GitHub Actions Lint Report
# ----------------------------------------
# Create a file called `.github/workflows/lint.yml` in your GitHub repo.
# Paste the following YAML into that file to enable automatic linting on push:

'''
name: Lint Python

on: [push]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v3
        with:
          python-version: '3.10'
      - name: Install flake8
        run: pip install flake8
      - name: Run flake8
        run: flake8 .
'''


# 📊 ACTIVITY 5: Static Analysis (Optional)
# ----------------------------------------
# This is a more advanced linting tool. Run it from the terminal:
# 1. First, install prospector:
#    pip install prospector
# 2. Then run:
#    prospector week3_code_quality.py


# 📁 ACTIVITY 6: Project Structure
# ----------------------------------------
# This is a convention for how your folders should be laid out.
# There's nothing to "run" – just organise your folders like this:

'''
my_project/
├── src/
│   └── my_package/
│       ├── __init__.py
│       ├── module1.py
├── tests/
│   └── test_module1.py
├── pyproject.toml
├── requirements.txt
└── README.md
'''


# 📦 ACTIVITY 7: Imports
# ----------------------------------------
# Use this order:
# 1. Standard library
# 2. Third-party packages
# 3. Your own modules

import os  # standard library
import pandas as pd  # third-party

# from my_package import utils  # your own (local) module


# ⚠️ ACTIVITY 8: Error Handling (using real data)
# ----------------------------------------
# Try to read an actual dataset and handle missing file or read errors.

real_data_path = "/Users/ismaelblanca/Downloads/UCL CHEM ENG/Year 3/COMP0035/COMP0035-tutorials-2025/src/activities/data/paralympics_raw.csv"

try:
    with open(real_data_path, "r") as file:
        first_lines = [next(file) for _ in range(5)]  # Print first 5 lines
    print("✅ Successfully read file! Here's a preview:\n")
    print("".join(first_lines))
except FileNotFoundError:
    print("❌ File not found. Check if the path is correct.")
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")

# 📂 ACTIVITY 9: Advanced File Handling (Bonus)
# ----------------------------------------
# This section builds on Activity 8 by loading the CSV into Pandas and running basic analysis.

import pandas as pd

try:
    df = pd.read_csv(real_data_path)
    print("\n✅ File loaded into a Pandas DataFrame.")

    # Preview first 3 rows
    print("\nFirst 3 rows of the dataset:")
    print(df.head(3))

    # Summary metrics
    print("\nQuick statistics:")
    print(f"• Total number of rows: {len(df)}")
    print(f"• Number of unique host cities: {df['host'].nunique()}")
    print(f"• Total participants (excluding NaN): {df['participants'].sum()}")

except FileNotFoundError:
    print("❌ File not found. Please double-check the file path.")
except pd.errors.ParserError:
    print("❌ Pandas couldn't parse the file — it might not be a proper CSV.")
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")