# team_leader.py
from production_worker import ProductionWorker


class TeamLeader(ProductionWorker):
    """
    Inherits from ProductionWorker.
    Adds monthly_bonus, required_training_hours, attended_training_hours.
    """

    def __init__(self, name, employee_number, hire_date,
                 shift, hourly_pay_rate,
                 monthly_bonus: float,
                 required_training_hours: int,
                 attended_training_hours: int):
        super().__init__(name, employee_number, hire_date, shift, hourly_pay_rate)
        self._monthly_bonus = monthly_bonus
        self._required_training_hours = required_training_hours
        self._attended_training_hours = attended_training_hours

    def get_monthly_bonus(self) -> float:
        return self._monthly_bonus

    def set_monthly_bonus(self, new_bonus: float) -> None:
        self._monthly_bonus = new_bonus

    def get_required_training_hours(self) -> int:
        return self._required_training_hours

    def set_required_training_hours(self, new_hours: int) -> None:
        self._required_training_hours = new_hours

    def get_attended_training_hours(self) -> int:
        return self._attended_training_hours

    def set_attended_training_hours(self, new_hours: int) -> None:
        self._attended_training_hours = new_hours

    def print_team_leader(self) -> None:
        self.print_production_worker()
        print(f"Monthly Bonus: ${self._monthly_bonus:.2f}")
        print(f"Required Training Hours: {self._required_training_hours}")
        print(f"Attended Training Hours: {self._attended_training_hours}")
