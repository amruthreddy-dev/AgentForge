import json
from pathlib import Path

DATA_FILE = Path(__file__).parent.parent / "data" / "news.json"


def load_news():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        print("Error: news.json not found")
        return []

    except json.JSONDecodeError:
        print("Error: Invalid JSON format")
        return []


def search_news(
    category: str = None,
    city: str = None,
    date: str = None
):
    news = load_news()

    results = news

    if category:
        results = [
            item for item in results
            if item["category"].lower()
            == category.lower()
        ]

    if city:
        results = [
            item for item in results
            if item["city"].lower()
            == city.lower()
        ]

    if date:
        results = [
            item for item in results
            if item["date"] == date
        ]

    return results[:10]