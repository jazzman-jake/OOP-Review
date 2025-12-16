# parked_car.py
class ParkedCar:
    """
    Represents a parked car with identifying info and minutes parked.
    minutes_parked is private with validation via property.
    """

    def __init__(self, make: str, model: str, color: str,
                 license_number: str, minutes_parked: int = 60):
        self.make = make
        self.model = model
        self.color = color
        self.license_number = license_number
        self._minutes_parked = 60  # default
        self.minutes_parked = minutes_parked  # use setter for validation

    @property
    def minutes_parked(self) -> int:
        return self._minutes_parked

    @minutes_parked.setter
    def minutes_parked(self, minutes: int) -> None:
        if minutes <= 0:
            raise ValueError("minutes_parked must be > 0")
        self._minutes_parked = minutes

    def __str__(self) -> str:
        return (f"{self.color} {self.make} {self.model} "
                f"({self.license_number}), parked {self.minutes_parked} minutes")
