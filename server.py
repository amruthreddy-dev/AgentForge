from fastmcp import FastMCP

from tools.trains import (
    search_trains,
    get_train_info,
    check_seat_availability,
    get_train_schedule,
    route_lookup,
    book_train
)

from tools.food import (
    search_restaurants,
    search_food,
    restaurant_details,
    search_by_cuisine,
    rating_lookup,
    book_table
)

from tools.weather import get_weather
from tools.news import search_news

# Create MCP Server
mcp = FastMCP("AgentForge")


# =========================
# TRAIN TOOLS
# =========================

@mcp.tool()
def train_search(
    source: str,
    destination: str,
    date: str = None
):
    return search_trains(
        source,
        destination,
        date
    )


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
def train_route(
    source: str,
    destination: str,
    date: str = None
):
    return route_lookup(
        source,
        destination,
        date
    )


@mcp.tool()
def train_booking(
    train_no: str,
    passenger_name: str
):
    return book_train(
        train_no,
        passenger_name
    )


# =========================
# FOOD TOOLS
# =========================

@mcp.tool()
def restaurant_search(
    city: str,
    date: str = None
):
    return search_restaurants(
        city,
        date
    )


@mcp.tool()
def food_search(
    city: str,
    food_name: str,
    date: str = None
):
    return search_food(
        city,
        food_name,
        date
    )


@mcp.tool()
def restaurant_info(restaurant_id: int):
    return restaurant_details(restaurant_id)


@mcp.tool()
def cuisine_search(
    cuisine: str,
    date: str = None
):
    return search_by_cuisine(
        cuisine,
        date
    )


@mcp.tool()
def restaurant_rating(min_rating: float):
    return rating_lookup(min_rating)


@mcp.tool()
def table_booking(
    restaurant_id: int,
    customer_name: str,
    guests: int
):
    return book_table(
        restaurant_id,
        customer_name,
        guests
    )


# =========================
# WEATHER TOOLS
# =========================

@mcp.tool()
def weather(
    city: str,
    date: str = None
):
    return get_weather(
        city,
        date
    )


# =========================
# NEWS TOOLS
# =========================

@mcp.tool()
def get_news(
    category: str = None,
    city: str = None,
    date: str = None
):
    return search_news(
        category,
        city,
        date
    )


# =========================
# RUN SERVER
# =========================

if __name__ == "__main__":
    mcp.run()