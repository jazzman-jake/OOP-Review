# shift_supervisor.py
from employee import Employee


class ShiftSupervisor(Employee):
    """
    Inherits from Employee.
    Adds annual_salary and annual_production_bonus.
    """

    def __init__(self, name, employee_number, hire_date,
                 annual_salary: float, annual_production_bonus: float):
        super().__init__(name, employee_number, hire_date)
        self._annual_salary = annual_salary
        self._annual_production_bonus = annual_production_bonus

    def get_annual_salary(self) -> float:
        return self._annual_salary

    def set_annual_salary(self, new_salary: float) -> None:
        self._annual_salary = new_salary

    def get_annual_production_bonus(self) -> float:
        return self._annual_production_bonus

    def set_annual_production_bonus(self, new_bonus: float) -> None:
        self._annual_production_bonus = new_bonus

    def print_shift_supervisor(self) -> None:
        self.print_employee()
        print(f"Annual Salary: ${self._annual_salary:,.2f}")
        print(f"Annual Production Bonus: ${self._annual_production_bonus:,.2f}")
