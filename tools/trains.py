import json
from pathlib import Path
from tools.bookings import create_booking

DATA_FILE = Path(__file__).parent.parent / "data" / "trains.json"


def load_trains():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        print("Error: trains.json not found")
        return []

    except json.JSONDecodeError:
        print("Error: Invalid JSON format")
        return []


def search_trains(
    source: str,
    destination: str,
    date: str = None
):
    trains = load_trains()

    results = []

    for train in trains:

        source_match = (
            train["source"].lower() == source.lower()
        )

        destination_match = (
            train["destination"].lower() == destination.lower()
        )

        date_match = (
            date is None
            or train["date"] == date
        )

        if source_match and destination_match and date_match:
            results.append(train)

    return results


def get_train_info(train_no: str):
    trains = load_trains()

    for train in trains:
        if train["train_no"] == train_no:
            return train

    return None


def check_seat_availability(train_no: str):
    train = get_train_info(train_no)

    if train:
        return {
            "train_no": train["train_no"],
            "train_name": train["train_name"],
            "available_seats": train["available_seats"]
        }

    return None


def get_train_schedule(train_no: str):
    train = get_train_info(train_no)

    if train:
        return {
            "train_no": train["train_no"],
            "train_name": train["train_name"],
            "departure": train["departure"],
            "arrival": train["arrival"]
        }

    return None


def route_lookup(
    source: str,
    destination: str,
    date: str = None
):
    trains = search_trains(
        source,
        destination,
        date
    )

    routes = []

    for train in trains:
        routes.append(
            {
                "date": train["date"],
                "train_no": train["train_no"],
                "train_name": train["train_name"],
                "route": f"{train['source']} → {train['destination']}"
            }
        )

    return routes


def book_train(
    train_no: str,
    passenger_name: str
):
    train = get_train_info(train_no)

    if not train:
        return {
            "status": "FAILED",
            "message": "Train not found"
        }

    if train["available_seats"] <= 0:
        return {
            "status": "FAILED",
            "message": "No seats available"
        }

    return create_booking(
        train_no,
        passenger_name
    )