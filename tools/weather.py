import json
from pathlib import Path
from typing import List, Dict, Optional

DATA_FILE = Path(__file__).parent.parent / "data" / "weather.json"


def load_weather() -> List[Dict]:
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        print("Error: weather.json not found")
        return []

    except json.JSONDecodeError:
        print("Error: Invalid JSON format")
        return []


def get_weather(
    city: str,
    date: str = None
) -> Optional[Dict]:

    weather_data = load_weather()

    for item in weather_data:

        city_match = (
            item["city"].lower() == city.lower()
        )

        date_match = (
            date is None
            or item["date"] == date
        )

        if city_match and date_match:
            return item

    return None


def get_all_weather() -> List[Dict]:
    return load_weather()


def search_by_condition(
    condition: str,
    date: str = None
) -> List[Dict]:

    weather_data = load_weather()

    results = []

    for item in weather_data:

        condition_match = (
            item["condition"].lower()
            == condition.lower()
        )

        date_match = (
            date is None
            or item["date"] == date
        )

        if condition_match and date_match:
            results.append(item)

    return results