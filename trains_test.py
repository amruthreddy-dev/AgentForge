from tools.trains import (
    load_trains,
    search_trains,
    get_train_info,
    check_seat_availability,
    get_train_schedule,
    route_lookup
)

print("===================================")
print("      AGENTFORGE TRAIN TESTS")
print("===================================")

# Print ALL trains
trains = load_trains()

print("\n=== ALL TRAINS ===")
print(f"Total Trains Loaded: {len(trains)}\n")

for i, train in enumerate(trains, start=1):
    print(f"{i}. {train}")

print("\n=== SEARCH TRAINS ===")
print(search_trains("Bangalore", "Delhi"))

print("\n=== TRAIN INFO ===")
print(get_train_info("12627"))

print("\n=== SEAT AVAILABILITY ===")
print(check_seat_availability("12627"))

print("\n=== TRAIN SCHEDULE ===")
print(get_train_schedule("12627"))

print("\n=== ROUTE LOOKUP ===")
print(route_lookup("Bangalore", "Delhi"))

print("\n===================================")
print("       TESTS COMPLETED")
print("===================================")