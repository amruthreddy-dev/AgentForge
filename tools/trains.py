import json
from pathlib import Path

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


def search_trains(source: str, destination: str):
    trains = load_trains()

    results = []

    for train in trains:
        if (
            train["source"].lower() == source.lower()
            and train["destination"].lower() == destination.lower()
        ):
            results.append(train)

    return results


def get_train_info(train_no: str):
    """
    Get train information using train number.
    """

    trains = load_trains()

    for train in trains:
        if train["train_no"] == train_no:
            return train

    return None


def check_seat_availability(train_no: str):
    """
    Check available seats for a train.
    """

    train = get_train_info(train_no)

    if train:
        return {
            "train_no": train["train_no"],
            "train_name": train["train_name"],
            "available_seats": train["available_seats"]
        }

    return None


def get_train_schedule(train_no: str):
    """
    Get departure and arrival schedule.
    """

    train = get_train_info(train_no)

    if train:
        return {
            "train_no": train["train_no"],
            "train_name": train["train_name"],
            "departure": train["departure"],
            "arrival": train["arrival"]
        }

    return None


def route_lookup(source: str, destination: str):
    """
    Find route between source and destination.
    """

    trains = search_trains(source, destination)

    routes = []

    for train in trains:
        routes.append(
            {
                "train_no": train["train_no"],
                "train_name": train["train_name"],
                "route": f"{train['source']} → {train['destination']}"
            }
        )

    return routes