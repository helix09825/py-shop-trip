import json
from typing import Any, cast

from app.customer import Customer


class ShopManager:
    """Manages loading shop and customer data from a configuration file."""

    def __init__(self, config_path: str = "app/config.json") -> None:
        """
        Initializes the ShopManager by loading data from the config file.

        Args:
            config_path: The path to the JSON configuration file.
        """
        with open(config_path, "r") as f:
            config: dict[str, Any] = json.load(f)

        self.fuel_price: float = config["FUEL_PRICE"]
        self.shops: list[dict[str, Any]] = config["shops"]
        self.customers: list[Customer] = [
            Customer(
                name=cust_data["name"],
                product_cart=cust_data["product_cart"],
                location=cust_data["location"],
                money=cust_data["money"],
                car_data=cust_data["car"],
            )
            for cust_data in cast(list[dict[str, Any]], config["customers"])
        ]
