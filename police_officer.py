# police_officer.py
from parked_car import ParkedCar
from parking_meter import ParkingMeter
from parking_ticket import ParkingTicket


class PoliceOfficer:
    """
    Represents a police officer inspecting parked cars.
    """

    def __init__(self, name: str, badge_number: str):
        self.name = name
        self.badge_number = badge_number

    def inspect_car(self, car: ParkedCar, meter: ParkingMeter) -> ParkingTicket | None:
        """
        Compare minutes_parked vs minutes_purchased.
        If over, issue and return a ParkingTicket; otherwise return None.
        """
        illegal_minutes = car.minutes_parked - meter.minutes_purchased
        if illegal_minutes > 0:
            return ParkingTicket(car, self.name, self.badge_number, illegal_minutes)
        else:
            return None
