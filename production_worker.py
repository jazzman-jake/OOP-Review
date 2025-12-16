# production_worker.py
from employee import Employee


class ProductionWorker(Employee):
    """
    Inherits from Employee.
    Adds shift (1=day, 2=night) and hourly_pay_rate.
    """

    def __init__(self, name, employee_number, hire_date, shift: int, hourly_pay_rate: float):
        super().__init__(name, employee_number, hire_date)
        self._shift = shift
        self._hourly_pay_rate = hourly_pay_rate

    def get_shift(self) -> int:
        return self._shift

    def set_shift(self, new_shift: int) -> None:
        self._shift = new_shift

    def get_hourly_pay_rate(self) -> float:
        return self._hourly_pay_rate

    def set_hourly_pay_rate(self, new_rate: float) -> None:
        self._hourly_pay_rate = new_rate

    def print_production_worker(self) -> None:
        self.print_employee()
        shift_name = "Day" if self._shift == 1 else "Night"
        print(f"Shift: {shift_name} ({self._shift})")
        print(f"Hourly Pay Rate: ${self._hourly_pay_rate:.2f}")
