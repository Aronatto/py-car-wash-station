class Car:
    """Represents a car with a comfort class, cleanliness rating, and brand."""

    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        """Initialize a car with comfort class (1-7), clean mark (1-10), and brand."""
        if not 1 <= comfort_class <= 7:
            raise ValueError("comfort_class must be between 1 and 7")
        if not 1 <= clean_mark <= 10:
            raise ValueError("clean_mark must be between 1 and 10")

        self.comfort_class: int = comfort_class
        self.clean_mark: int = clean_mark
        self.brand: str = brand

    def __repr__(self) -> str:
        return (
            f"Car(brand={self.brand}, comfort_class={self.comfort_class}, "
            f"clean_mark={self.clean_mark})"
        )


class CarWashStation:
    """
    Represents a car wash station that can clean, calculate pricing,
    and manage its service rating.
    """

    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int,
    ) -> None:
        """
        Initialize car wash station with distance (1.0-10.0), clean power,
        rating (1.0-5.0), and rating count.
        """
        if not 1.0 <= distance_from_city_center <= 10.0:
            raise ValueError("distance_from_city_center must be between 1.0 and 10.0")
        if not 1 <= average_rating <= 5:
            raise ValueError("average_rating must be between 1 and 5")

        self.distance_from_city_center: float = distance_from_city_center
        self.clean_power: int = clean_power
        self.average_rating: float = average_rating
        self.count_of_ratings: int = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        """
        Calculates the cost for a single car wash.
        Returns 0.0 if the car is already clean enough. Result rounded to 1 decimal.
        """
        if car.clean_mark >= self.clean_power:
            return 0.0

        price: float = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        """
        Washes a single car by setting its clean_mark to the station's
        clean_power if the car is dirty.
        """
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list[Car]) -> float:
        """
        Washes only cars with clean_mark < clean_power.
        Returns total income from all served cars, rounded to 1 decimal.
        """
        total_income: float = 0.0

        for car in cars:
            if car.clean_mark < self.clean_power:
                total_income += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return round(total_income, 1)

    def rate_service(self, rating: int) -> None:
        """
        Adds a single rate to the wash station and updates the average_rating
        and count_of_ratings using a weighted average.
        """
        if not 1 <= rating <= 5:
            raise ValueError("Rating must be between 1 and 5")

        total_rating_sum: float = self.average_rating * self.count_of_ratings
        total_rating_sum += rating
        self.count_of_ratings += 1
        self.average_rating = round(total_rating_sum / self.count_of_ratings, 1)

    def __repr__(self) -> str:
        return (
            f"CarWashStation(distance={self.distance_from_city_center}, "
            f"clean_power={self.clean_power}, "
            f"average_rating={self.average_rating}, "
            f"count_of_ratings={self.count_of_ratings})"
        )
