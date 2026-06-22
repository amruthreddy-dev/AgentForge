from fastmcp import FastMCP

from tools.trains import (
    search_trains,
    get_train_info,
    check_seat_availability,
    get_train_schedule,
    route_lookup
)

from tools.food import (
    search_restaurants,
    search_food,
    restaurant_details,
    search_by_cuisine,
    rating_lookup
)

mcp = FastMCP("AgentForge")


@mcp.tool()
def train_search(source: str, destination: str):
    return search_trains(source, destination)


@mcp.tool()
def train_info(train_no: str):
    return get_train_info(train_no)


@mcp.tool()
def seat_availability(train_no: str):
    return check_seat_availability(train_no)


@mcp.tool()
def train_schedule(train_no: str):
    return get_train_schedule(train_no)


@mcp.tool()
def train_route(source: str, destination: str):
    return route_lookup(source, destination)


@mcp.tool()
def restaurant_search(city: str):
    return search_restaurants(city)


@mcp.tool()
def food_search(city: str, food_name: str):
    return search_food(city, food_name)


@mcp.tool()
def restaurant_info(restaurant_id: int):
    return restaurant_details(restaurant_id)


@mcp.tool()
def cuisine_search(cuisine: str):
    return search_by_cuisine(cuisine)


@mcp.tool()
def restaurant_rating(min_rating: float):
    return rating_lookup(min_rating)


if __name__ == "__main__":
    mcp.run()