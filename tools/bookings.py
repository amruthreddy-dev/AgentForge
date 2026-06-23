import json
from pathlib import Path

DATA_FILE = Path(__file__).parent.parent / "data" / "bookings.json"


def load_bookings():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []


def save_bookings(bookings):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(bookings, file, indent=4)


def create_booking(
    train_no: str,
    passenger_name: str
):
    bookings = load_bookings()

    booking_id = f"AF{1000 + len(bookings) + 1}"

    new_booking = {
        "booking_id": booking_id,
        "train_no": train_no,
        "passenger_name": passenger_name,
        "status": "CONFIRMED"
    }

    bookings.append(new_booking)

    save_bookings(bookings)

    return new_booking


def get_booking_status(
    booking_id: str
):
    bookings = load_bookings()

    for booking in bookings:
        if booking["booking_id"] == booking_id:
            return booking

    return {
        "status": "NOT_FOUND"
    }