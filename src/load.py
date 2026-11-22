import sqlite3
import pandas as pd
from pathlib import Path

CSV_PATH = Path("data/processed/cleaned_ridership.csv")
DB_PATH = Path("data/transit.db")
TABLE_NAME = "ridership"


def create_table(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS ridership (
            transit_timestamp TEXT NOT NULL,
            transit_mode TEXT,
            station_complex_id INTEGER,
            station_complex TEXT,
            borough TEXT,
            payment_method TEXT,
            fare_class_category TEXT,
            ridership REAL NOT NULL,
            transfers REAL,
            latitude REAL,
            longitude REAL,
            date TEXT,
            hour INTEGER
        )
    """)

def load_data():
    print("Starting data load. . .")

    if not CSV_PATH.exists():
        raise FileNotFoundError(f"CSV file not found at {CSV_PATH}")
    df = pd.read_csv(CSV_PATH)

    print(f"Records to load: {len(df)}")

    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(DB_PATH) as conn:
        create_table(conn)

        # Replace the previous contents
        conn.execute(f"DELETE FROM ridership")
        
        # Insert the cleaned records
        df.to_sql(
            TABLE_NAME,
            conn,
            if_exists="append",
            index=False
        )

        # Verify the loaded row count
        cursor = conn.execute(
            "SELECT COUNT(*) FROM ridership"
        )

        row_count = cursor.fetchone()[0]

    print(f"Records loaded: {row_count}")
    print(f"Database saved to: {DB_PATH}")

    return row_count

if __name__ == "__main__":
    load_data()
