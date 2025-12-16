
from __future__ import annotations
from dataclasses import dataclass
from datetime import date, timedelta


@dataclass
class Date:i8
"""Custom Date class that wraps month/day/year and uses datetime for logic."""

    month: int = 1
    day: int = 1
    year: int = 1900

    def __post_init__(self):
        if not self._is_valid_date(self.month, self.day, self.year):
            # default to 1/1/1900 on invalid input
            self.month, self.day, self.year = 1, 1, 1900

    # ---------- internal helpers ----------

    @staticmethod
    def _is_valid_date(month: int, day: int, year: int) -> bool:
        try:
            date(year, month, day)
            return True
        except ValueError:
            return False

    def _to_datetime(self) -> date:
        return date(self.year, self.month, self.day)

    @classmethod
    def _from_datetime(cls, d: date) -> "Date":
        return cls(d.month, d.day, d.year)

    # ---------- core API ----------

    def set_date(self, month: int, day: int, year: int) -> None:
        """Set date if valid; otherwise default to 1/1/1900."""
        if self._is_valid_date(month, day, year):
            self.month, self.day, self.year = month, day, year
        else:
            self.month, self.day, self.year = 1, 1, 1900

    # ----- leap year -----

    def is_leap_year(self) -> bool:
        """Instance method: is *this* date's year a leap year?"""
        return Date.is_leap_year_static(self.year)

    @staticmethod
    def is_leap_year_static(year: int) -> bool:
        """Leap year if:
          - divisible by 4 and not by 100
          - divisible by 400"""
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    # alias 
    is_leap_year_class = is_leap_year_static

    # ----- last_day -----

    def last_day(self) -> int:
        """
        Last day of this object's month/year.
        """
        return Date.last_day_static(self.month, self.year)

    @staticmethod
    def last_day_static(month: int, year: int) -> int:
        """Static version: last day for given month/year."""
        
        if month == 12:
            first_next = date(year + 1, 1, 1)
        else:
            first_next = date(year, month + 1, 1)
        last = first_next - timedelta(days=1)
        return last.day

    # ---------- string representations ----------

    def format1(self) -> str:
        """Format 1: MM/DD/YYYY"""
        d = self._to_datetime()
        return d.strftime("%m/%d/%Y")

    def format2(self) -> str:
        """Format 2: MonthName DD, YYYY"""
        d = self._to_datetime()
        return d.strftime("%B %d, %Y")

    def format3(self) -> str:
        """Format 3: DD MonthName YYYY"""
        d = self._to_datetime()
        return d.strftime("%d %B %Y")

    def __str__(self) -> str:
        """
        For print(), use Format 2 as required:
        e.g., "April 18, 2018"
        """
        return self.format2()

    # ---------- arithmetic / comparison ----------

    def __add__(self, days: int) -> "Date":
        """
        Return NEW Date object after adding days.
        (days can be negative, but __sub__ covers date - date)
        """
        if not isinstance(days, int):
            return NotImplemented
        new_dt = self._to_datetime() + timedelta(days=days)
        return Date._from_datetime(new_dt)

    __radd__ = __add__  # allow int + Date

    def __sub__(self, other) -> int | "Date":
        """
        Overload:
          - Date - Date -> int (difference in days)
          - Date - int  -> Date (subtract days)
        """
        if isinstance(other, Date):
            return (self._to_datetime() - other._to_datetime()).days
        elif isinstance(other, int):
            new_dt = self._to_datetime() - timedelta(days=other)
            return Date._from_datetime(new_dt)
        else:
            return NotImplemented

    # ----- increment/decrement -----

    def increment(self) -> "Date":
        """Add 1 day to this object, handling month/year rollover."""
        new_dt = self._to_datetime() + timedelta(days=1)
        self.month, self.day, self.year = new_dt.month, new_dt.day, new_dt.year
        return self

    def decrement(self) -> "Date":
        """Subtract 1 day from this object, handling month/year rollback."""
        new_dt = self._to_datetime() - timedelta(days=1)
        self.month, self.day, self.year = new_dt.month, new_dt.day, new_dt.year
        return self

    # ---------- input ----------

    @classmethod
    def from_input(cls) -> "Date":
        """Prompt the user for a date and return a Date object.
        Invalid input defaults to 1/1/1900"""
        try:
            m = int(input("Enter month (1-12): "))
            d = int(input("Enter day (1-31): "))
            y = int(input("Enter year (e.g., 2024): "))
        except ValueError:
            print("Invalid numeric input; defaulting to 1/1/1900.")
            return cls()  # defaults
        return cls(m, d, y)



