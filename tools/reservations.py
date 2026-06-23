import json
from pathlib import Path

DATA_FILE = Path(__file__).parent.parent / "data" / "reservations.json"


def load_reservations():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []


def save_reservations(reservations):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(reservations, file, indent=4)


def create_reservation(
    restaurant_id: int,
    customer_name: str,
    guests: int
):
    reservations = load_reservations()

    reservation_id = f"RS{1000 + len(reservations) + 1}"

    new_reservation = {
        "reservation_id": reservation_id,
        "restaurant_id": restaurant_id,
        "customer_name": customer_name,
        "guests": guests,
        "status": "CONFIRMED"
    }

    reservations.append(new_reservation)

    save_reservations(reservations)

    return new_reservation


def get_reservation_status(
    reservation_id: str
):
    reservations = load_reservations()

    for reservation in reservations:
        if reservation["reservation_id"] == reservation_id:
            return reservation

    return {
        "status": "NOT_FOUND"
    }