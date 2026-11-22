
import pandas as pd
from pathlib import Path

# Read our raw JSON data
df = pd.read_json("data/raw/subway_ridership.json")

# Display the first five rows
print(df.head())

# Number of rows and columns
print("\nDataset shape:")
print(df.shape)

# Column names
print("\nColumn names:")
print(df.columns.tolist())

# Column data types
print("\nDataset information:")
df.info()

# Missing values by column
print("\nMissing values:")
print(df.isna().sum())


# Select columns needed for analysis
columns_to_keep = [
    "transit_timestamp",
    "transit_mode",
    "station_complex_id",
    "station_complex",
    "borough",
    "payment_method",
    "fare_class_category",
    "ridership",
    "transfers",
    "latitude",
    "longitude"
]

df = df[columns_to_keep]

print("\nSelected columns:")
print(df.columns.tolist())

# Convert timestamp to datetime values
df["transit_timestamp"] = pd.to_datetime(df["transit_timestamp"], errors="coerce")

# Extract date and time components
df["date"] = df["transit_timestamp"].dt.date
df["hour"] = df["transit_timestamp"].dt.hour

print("\nConverted timestamps:")
print(df[["transit_timestamp", "date", "hour"]].head())

# Count rows before cleaning
original_count = len(df)

# Remove exact duplicate rows
df = df.drop_duplicates()

# Remove records missing essential values
df = df.dropna(subset = ["transit_timestamp", "ridership"])

# Remove invalid negative values
df = df[(df["ridership"] >= 0) & (df["transfers"] >= 0)].copy()

# Count rows after cleaning
cleaned_count = len(df)

print("\nData Cleaning Results:")
print(f"Original row count: {original_count}")
print(f"Cleaned row count: {cleaned_count}")
print(f"Rows removed: {original_count - cleaned_count}")

# Calculate ridership totals by borough
borough_summary = (df.groupby("borough")["ridership"]
                   .sum().sort_values(ascending=False))

print("\nRidership totals by borough:")
print(borough_summary)

# Define the processed data location
output_path = Path("data/processed/cleaned_ridership.csv")

# Create the directory if it doesn't exist
output_path.parent.mkdir(
    parents = True,
    exist_ok = True
)

# Save the cleaned Dataframe
df.to_csv(output_path, index=False)

print("\nCleaned data saved to:", output_path)