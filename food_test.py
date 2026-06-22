from tools.food import (
    load_restaurants,
    search_restaurants,
    search_food,
    restaurant_details,
    search_by_cuisine,
    rating_lookup
)

print("===================================")
print("      AGENTFORGE FOOD TESTS")
print("===================================")

# Print ALL restaurants
restaurants = load_restaurants()

print("\n=== ALL RESTAURANTS ===")
print(f"Total Restaurants Loaded: {len(restaurants)}\n")

for i, restaurant in enumerate(restaurants, start=1):
    print(f"{i}. {restaurant}")

print("\n=== SEARCH RESTAURANTS ===")
print(search_restaurants("Hyderabad"))

print("\n=== SEARCH FOOD ===")
print(search_food("Hyderabad", "Biryani"))

print("\n=== RESTAURANT DETAILS ===")
print(restaurant_details(1))

print("\n=== SEARCH BY CUISINE ===")
print(search_by_cuisine("Biryani"))

print("\n=== RATING LOOKUP ===")
print(rating_lookup(4.4))

print("\n===================================")
print("       TESTS COMPLETED")
print("===================================")