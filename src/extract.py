
import json
from pathlib import Path

import requests


API_URL = "https://data.ny.gov/resource/wujg-7c2s.json"

RAW_DATA_PATH = Path("data/raw/subway_ridership.json")


def extract_data():
    print("Starting data extraction...")

    response = requests.get(
        API_URL,
        params={"$limit": 1000},
        timeout=30
    )

    response.raise_for_status()

    data = response.json()

    RAW_DATA_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(RAW_DATA_PATH, "w") as file:
        json.dump(data, file, indent=4)

    print(f"Extracted {len(data)} records")
    print(f"Saved data to {RAW_DATA_PATH}")


if __name__ == "__main__":
    extract_data()
