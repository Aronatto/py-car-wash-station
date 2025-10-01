from typing import List


class Car:
    """Represents a car with a comfort class, cleanliness rating, and brand."""

    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        """Initialize a car with comfort class (1-7), clean mark (1-10), and brand."""
        self.comfort_class: int = comfort_class
        self.clean_mark: int = clean_mark
        self.brand: str = brand


class CarWashStation:
    """
    Represents a car wash station that can clean, calculate pricing,
    and manage its service rating.
    """

    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        """Initialize car wash station with distance (1.0-10.0), clean power, rating (1.0-5.0), and rating count."""
        self.distance_from_city_center: float = distance_from_city_center
        self.clean_power: int = clean_power
        self.average_rating: float = average_rating
        self.count_of_ratings: int = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        """
        Calculates the cost for a single car wash based on the formula:
        comfort_class * (clean_power - car.clean_mark) * average_rating / distance_from_city_center
        Returns 0.0 if the car is already clean enough (car.clean_mark >= clean_power).
        Result is rounded to 1 decimal.
        """
        if car.clean_mark >= self.clean_power:
            return 0.0

        # Formula: car's comfort class * difference * station rating / distance
        price: float = (car.comfort_class *
                        (self.clean_power - car.clean_mark) *
                        self.average_rating /
                        self.distance_from_city_center)

        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        """
        Washes a single car by setting its clean_mark to the station's clean_power,
        only if the station's clean_power is greater than the car's current clean_mark.
        """
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: List[Car]) -> float:
        """
        Washes only cars with clean_mark < clean_power.
        Returns total income from all served cars, rounded to 1 decimal.
        """
        total_income: float = 0.0

        for car in cars:
            # Check if the car needs washing
            if car.clean_mark < self.clean_power:
                # 1. Calculate price and add to income
                total_income += self.calculate_washing_price(car)

                # 2. Wash the car (update its clean_mark)
                self.wash_single_car(car)

        return round(total_income, 1)

    def rate_service(self, rating: int) -> None:
        """
        Adds a single rate to the wash station and updates the average_rating 
        and count_of_ratings using a weighted average.
        """
        # Calculate the sum of all previous ratings
        total_rating_sum: float = self.average_rating * self.count_of_ratings

        # Add the new rating
        total_rating_sum += rating
        self.count_of_ratings += 1

        # Calculate the new average and round to 1 decimal
        self.average_rating = round(total_rating_sum / self.count_of_ratings, 1)