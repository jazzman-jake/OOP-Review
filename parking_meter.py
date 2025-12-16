# parking_meter.py
class ParkingMeter:
    """
    Represents a parking meter with minutes purchased.
    """

    def __init__(self, minutes_purchased: int = 60):
        self._minutes_purchased = 60
        self.minutes_purchased = minutes_purchased

    @property
    def minutes_purchased(self) -> int:
        return self._minutes_purchased

    @minutes_purchased.setter
    def minutes_purchased(self, minutes: int) -> None:
        if minutes <= 0:
            raise ValueError("minutes_purchased must be > 0")
        self._minutes_purchased = minutes
