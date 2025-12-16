# main_workers.py
from production_worker import ProductionWorker
from shift_supervisor import ShiftSupervisor
from team_leader import TeamLeader


def main():
    print("=== Production Workers ===")
    pw1 = ProductionWorker("Alice Smith", 1001, (5, 10, 2020), 1, 18.50)
    pw2 = ProductionWorker("Bob Johnson", 1002, (6, 1, 2021), 2, 20.75)
    pw1.print_production_worker()
    print()
    pw2.print_production_worker()

    print("\n=== Shift Supervisor ===")
    ss = ShiftSupervisor("Carol Supervisor", 2001, (1, 15, 2018),
                         annual_salary=60000.0,
                         annual_production_bonus=5000.0)
    ss.print_shift_supervisor()

    print("\n=== Team Leader ===")
    tl = TeamLeader("Dave Leader", 3001, (9, 1, 2019),
                    shift=1,
                    hourly_pay_rate=22.50,
                    monthly_bonus=750.0,
                    required_training_hours=40,
                    attended_training_hours=32)
    tl.print_team_leader()


if __name__ == "__main__":
    main()
