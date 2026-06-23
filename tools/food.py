import json
from pathlib import Path
from tools.reservations import create_reservation

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


def search_restaurants(
    city: str,
    date: str = None
):
    restaurants = load_restaurants()

    results = []

    for restaurant in restaurants:

        city_match = (
            restaurant["city"].lower() == city.lower()
        )

        date_match = (
            date is None
            or restaurant["date"] == date
        )

        if city_match and date_match:
            results.append(restaurant)

    return results


def search_food(
    city: str,
    food_name: str,
    date: str = None
):
    restaurants = load_restaurants()

    results = []

    for restaurant in restaurants:

        city_match = (
            restaurant["city"].lower() == city.lower()
        )

        food_match = (
            food_name.lower()
            in restaurant["cuisine"].lower()
        )

        date_match = (
            date is None
            or restaurant["date"] == date
        )

        if city_match and food_match and date_match:
            results.append(restaurant)

    return results


def restaurant_details(restaurant_id: int):
    restaurants = load_restaurants()

    for restaurant in restaurants:
        if restaurant["id"] == restaurant_id:
            return restaurant

    return None


def search_by_cuisine(
    cuisine: str,
    date: str = None
):
    restaurants = load_restaurants()

    results = []

    for restaurant in restaurants:

        cuisine_match = (
            cuisine.lower()
            in restaurant["cuisine"].lower()
        )

        date_match = (
            date is None
            or restaurant["date"] == date
        )

        if cuisine_match and date_match:
            results.append(restaurant)

    return results


def rating_lookup(min_rating: float):
    restaurants = load_restaurants()

    results = []

    for restaurant in restaurants:
        if restaurant["rating"] >= min_rating:
            results.append(restaurant)

    return results


def book_table(
    restaurant_id: int,
    customer_name: str,
    guests: int
):
    restaurant = restaurant_details(restaurant_id)

    if not restaurant:
        return {
            "status": "FAILED",
            "message": "Restaurant not found"
        }

    if restaurant["available_tables"] <= 0:
        return {
            "status": "FAILED",
            "message": "No tables available"
        }

    return create_reservation(
        restaurant_id,
        customer_name,
        guests
    )