# parking_ticket.py
import math
from parked_car import ParkedCar


class ParkingTicket:
    """
    Represents a citation issued to a car parked beyond the paid time.
    """

    def __init__(self, car: ParkedCar, officer_name: str,
                 badge_number: str, illegal_minutes: int):
        self.car = car
        self.officer_name = officer_name
        self.badge_number = badge_number
        self.illegal_minutes = illegal_minutes
        self.fine = self.calculate_fine()

    def calculate_fine(self) -> float:
        """
        $25 for the first hour or part of an hour,
        + $10 for each additional hour or part.
        """
        if self.illegal_minutes <= 0:
            return 0.0
        hours = math.ceil(self.illegal_minutes / 60.0)
        if hours <= 1:
            return 25.0
        else:
            return 25.0 + (hours - 1) * 10.0

    def __str__(self) -> str:
        lines = [
            "=== PARKING TICKET ===",
            f"Car: {self.car.color} {self.car.make} {self.car.model}",
            f"License: {self.car.license_number}",
            f"Illegal Minutes: {self.illegal_minutes}",
            f"Fine: ${self.fine:.2f}",
            f"Issued by Officer: {self.officer_name}",
            f"Badge Number: {self.badge_number}",
        ]
        return "\n".join(lines)
