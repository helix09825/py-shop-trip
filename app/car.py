class Car:
    """Represents a car with its brand and fuel consumption."""

    def __init__(self, brand: str, fuel_consumption: float) -> None:
        """
        Initializes a Car instance.

        Args:
            brand: The brand of the car.
            fuel_consumption: The car's fuel consumption in liters per 100 km.
        """
        self.brand = brand
        self.fuel_consumption = fuel_consumption
