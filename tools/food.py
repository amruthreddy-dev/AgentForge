import json
from pathlib import Path

DATA_FILE = Path(__file__).parent.parent / "data" / "restaurants.json"


def load_restaurants():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        print("Error: restaurants.json not found")
        return []

    except json.JSONDecodeError:
        print("Error: Invalid JSON format")
        return []


def search_restaurants(city: str):
    restaurants = load_restaurants()

    results = []

    for restaurant in restaurants:
        if restaurant["city"].lower() == city.lower():
            results.append(restaurant)

    return results


def search_food(city: str, food_name: str):
    restaurants = load_restaurants()

    results = []

    for restaurant in restaurants:
        if (
            restaurant["city"].lower() == city.lower()
            and food_name.lower() in restaurant["cuisine"].lower()
        ):
            results.append(restaurant)

    return results


def restaurant_details(restaurant_id: int):
    restaurants = load_restaurants()

    for restaurant in restaurants:
        if restaurant["id"] == restaurant_id:
            return restaurant

    return None


def search_by_cuisine(cuisine: str):
    restaurants = load_restaurants()

    results = []

    for restaurant in restaurants:
        if cuisine.lower() in restaurant["cuisine"].lower():
            results.append(restaurant)

    return results


def rating_lookup(min_rating: float):
    restaurants = load_restaurants()

    results = []

    for restaurant in restaurants:
        if restaurant["rating"] >= min_rating:
            results.append(restaurant)

    return results