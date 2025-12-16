# main_parking.py
from parked_car import ParkedCar
from parking_meter import ParkingMeter
from police_officer import PoliceOfficer


def scenario_1():
    print("\n--- Scenario 1: Car Parked Legally ---")
    car = ParkedCar("Toyota", "Camry", "Red", "XYZ123", 30)
    meter = ParkingMeter(40)
    officer = PoliceOfficer("John Doe", "5678")

    ticket = officer.inspect_car(car, meter)
    if ticket:
        print(ticket)
    else:
        print("Car is legally parked. No ticket issued.")


def scenario_2():
    print("\n--- Scenario 2: Illegally Parked (<1 hour over) ---")
    car = ParkedCar("Honda", "Accord", "Blue", "ABC987", 70)
    meter = ParkingMeter(60)
    officer = PoliceOfficer("Jane Smith", "1234")

    ticket = officer.inspect_car(car, meter)
    if ticket:
        print(ticket)
    else:
        print("Car is legally parked. No ticket issued.")


def scenario_3():
    print("\n--- Scenario 3: Illegally Parked (Multiple Hours Over) ---")
    car = ParkedCar("Ford", "Mustang", "Black", "LMN456", 190)
    meter = ParkingMeter(60)
    officer = PoliceOfficer("James Brown", "4321")

    ticket = officer.inspect_car(car, meter)
    if ticket:
        print(ticket)
    else:
        print("Car is legally parked. No ticket issued.")


def scenario_4():
    print("\n--- Scenario 4: Multiple Cars in a Parking Lot ---")
    officer = PoliceOfficer("Sarah Green", "9999")

    cars = [
        (ParkedCar("Nissan", "Altima", "White", "JKL321", 60), ParkingMeter(60)),
        (ParkedCar("Chevy", "Malibu", "Silver", "QWE789", 80), ParkingMeter(60)),
        (ParkedCar("BMW", "X5", "Black", "BMW999", 500), ParkingMeter(60)),
        (ParkedCar("Mazda", "3", "Blue", "MAZ321", 45), ParkingMeter(60)),
    ]

    for car, meter in cars:
        ticket = officer.inspect_car(car, meter)
        if ticket:
            print(ticket)
            print()
        else:
            print(f"{car} is legally parked. No ticket issued.\n")


def main():
    scenario_1()
    scenario_2()
    scenario_3()
    scenario_4()


if __name__ == "__main__":
    main()
