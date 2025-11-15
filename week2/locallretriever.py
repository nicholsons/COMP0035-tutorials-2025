import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# 📁 ACTIVITY 1: Load CSV data
data_path = Path("/Users/ismaelblanca/Downloads/UCL CHEM ENG/Year 3/COMP0035/COMP0035-tutorials-2025/src/activities/data/paralympics_raw.csv")
df = pd.read_csv(data_path)

# 📊 ACTIVITY 2: Bracket and dot notation
print(df['country'])  # Bracket notation
print(df.year)        # Dot notation

# 📍 ACTIVITY 3: Access rows and columns using .loc
print(df.loc[2])  # Single row
print(df.loc[:, ['country', 'year']])  # All rows, two columns

# 🎯 ACTIVITY 4: Access using .iloc
print(df.iloc[0])  # First row
print(df.iloc[1:4, 0:3])  # Rows 1 to 3, columns 0 to 2

# 🔎 ACTIVITY 5: Access single value with .iat
print(df.iat[0, 2])  # Row 0, column 2

# 🔐 ACTIVITY 6: Access single value with .at
print(df.at[3, 'host'])

# 🔍 ACTIVITY 7: Use .query with hardcoded string
summer_df = df.query("type.str.lower() == 'summer'", engine='python')
print(summer_df[['year', 'host']])

# 🧠 ACTIVITY 8: Use .query with variable
game_type = 'winter'
winter_df = df.query("type.str.lower() == @game_type", engine='python')
print(winter_df[['year', 'host']])

# 🧪 ACTIVITY 9: Combine .query with column selection
event_type = 'summer'
print(df.query("type == @event_type")[['year', 'country']])

# ✏️ ACTIVITY 10: Modify values using loc, at, iloc
print("\nACTIVITY 10: Data modification")
df.loc[df['type'] == 'Summer', 'type'] = 'summer'
df.loc[df['type'] == 'winter ', 'type'] = 'winter'  # Fix trailing space
print("Updated 'type' values:", df['type'].unique())

df.at[3, 'host'] = 'Corrected City'
print("Updated host at index 3 (with .at):", df.at[3, 'host'])

row_idx = df.index.get_loc(3)
col_idx = df.columns.get_loc('host')
df.iloc[row_idx, col_idx] = 'Updated Again'
print("Host after .iloc update:", df.iloc[3]['host'])

# 📈 ACTIVITY 11: Plot participants over time
def plot_participants_over_time(df):
    year = pd.to_numeric(df['year'], errors='coerce')
    participants = pd.to_numeric(df['participants'], errors='coerce')
    temp = pd.DataFrame({'year': year, 'participants': participants}).dropna()
    if temp.empty:
        print("No valid year/participants data to plot.")
        return
    agg = temp.groupby('year')['participants'].sum().sort_index()
    plt.figure(figsize=(10, 5))
    plt.plot(agg.index, agg.values, marker='o', linestyle='-', color='green')
    plt.title('Total participants over time')
    plt.xlabel('Year')
    plt.ylabel('Number of participants')
    plt.grid(True)
    out_path = Path(__file__).parent.parent.parent / "src" / "activities" / "participants_over_time.png"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(out_path, bbox_inches='tight')
    print(f"Saved plot to {out_path}")
    plt.show()

plot_participants_over_time(df)

# 🔧 ACTIVITY 12: Check for missing values
print("\nACTIVITY 12: Missing value checks")
missing_summary = df.isna().sum()
print("Missing values per column:\n", missing_summary)

# 🧽 ACTIVITY 13: Fill missing values
print("\nACTIVITY 13: Filling missing values")
df_filled = df.fillna({'participants': 0, 'country': 'Unknown'})
print("Sample filled data:\n", df_filled.head())

# 🧹 ACTIVITY 14: Drop rows with missing values
print("\nACTIVITY 14: Dropping rows with missing values")
df_dropped = df.dropna()
print(f"Original length: {len(df)}, After dropna: {len(df_dropped)}")

# 🔁 ACTIVITY 15: Convert column types
print("\nACTIVITY 15: Type conversion")
df['year'] = df['year'].astype(int)
df['participants'] = pd.to_numeric(df['participants'], errors='coerce')
print(df.dtypes)

# 🔗 ACTIVITY 16: Merge with mock dataset
print("\nACTIVITY 16: Merge operation")
mock_medals = pd.DataFrame({
    'year': [1960, 1964, 1968],
    'medal_count': [100, 150, 200]
})
merged_df = pd.merge(df, mock_medals, how='left', on='year')
print("Merged DataFrame sample:\n", merged_df[['year', 'country', 'medal_count']].head())

# 📊 ACTIVITY 17: Use groupby with aggregation (participants per year)
print("\nACTIVITY 17: Participants grouped by year")
participants_by_year = df.groupby('year')['participants'].sum().sort_index()
print(participants_by_year)

# 📋 ACTIVITY 18: Describe dataframe
def describe_dataframe(df):
    print("\nACTIVITY 18: Descriptive summary")
    print("DataFrame Shape:", df.shape)
    print("Column Types:\n", df.dtypes)
    print("First 5 Rows:\n", df.head())
    print("Summary Statistics:\n", df.describe(include='all'))

describe_dataframe(df)