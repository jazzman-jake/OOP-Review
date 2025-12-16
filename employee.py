# employee.py
from __future__ import annotations
from date_class import Date  # your custom Date class


class Employee:
    """
    Base class for all employees.

    Attributes (protected):
        _name: str
        _employee_number: int | str
        _hire_date: Date
    """

    def __init__(self, name: str, employee_number, hire_date):
        """
        Preconditions:
            - name: non-empty string
            - employee_number: int or str
            - hire_date: Date object OR (month, day, year) tuple
        Postconditions:
            - Employee object initialized with valid date via Date class
        """
        self._name = name
        self._employee_number = employee_number

        if isinstance(hire_date, Date):
            self._hire_date = hire_date
        elif (isinstance(hire_date, tuple) and len(hire_date) == 3):
            m, d, y = hire_date
            self._hire_date = Date(m, d, y)
        else:
            # default hire date
            self._hire_date = Date()

    # Getters / setters (simple, since no special validation beyond Date)

    def get_name(self) -> str:
        return self._name

    def set_name(self, new_name: str) -> None:
        self._name = new_name

    def get_employee_number(self):
        return self._employee_number

    def set_employee_number(self, new_number) -> None:
        self._employee_number = new_number

    def get_hire_date(self) -> Date:
        return self._hire_date

    def set_hire_date(self, new_date) -> None:
        if isinstance(new_date, Date):
            self._hire_date = new_date
        elif (isinstance(new_date, tuple) and len(new_date) == 3):
            m, d, y = new_date
            self._hire_date = Date(m, d, y)
        else:
            self._hire_date = Date()

    def print_employee(self) -> None:
        print(f"Name: {self._name}")
        print(f"Employee Number: {self._employee_number}")
        print(f"Hire Date: {self._hire_date.format1()}")
