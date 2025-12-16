# test_date_class.py
from date_class import Date


def main():
    print("=== Default constructor and Format 1 ===")
    d_default = Date()
    print("Default date (Format 1):", d_default.format1())

    print("\n=== Valid constructor and Format 2 ===")
    d_valid = Date(12, 25, 2021)
    print("Valid date (Format 2):", d_valid)  # uses __str__ (Format 2)

    print("\n=== set_date() and Format 3 ===")
    d_set = Date()
    d_set.set_date(4, 18, 2014)
    print("After set_date (Format 3):", d_set.format3())

    print("\n=== Invalid dates default to 1/1/1900 ===")
    for m, d, y in [(13, 45, 2018), (4, 31, 2000), (2, 29, 2009)]:
        tmp = Date(m, d, y)
        print(f"Input ({m}, {d}, {y}) ->", tmp.format1())

    print("\n=== Subtracting two dates (difference in days) ===")
    d1 = Date(4, 18, 2014)
    d2 = Date(4, 10, 2014)
    print("4/18/2014 - 4/10/2014 =", d1 - d2)  # should be 8

    d3 = Date(2, 2, 2006)
    d4 = Date(11, 10, 2003)
    print("2/2/2006 - 11/10/2003 =", d3 - d4)  # should be 815

    print("\n=== Increment/decrement transitions (leap year) ===")
    leap = Date(2, 29, 2008)
    print("Start:", leap.format1())
    leap_plus = leap + 1
    print("2/29/2008 + 1 day =", leap_plus.format1())  # -> 03/01/2008
    back = leap_plus - 1
    print("Back one day =", back.format1())  # -> 02/29/2008

    print("\n=== Year rollover using increment/decrement ===")
    d_roll = Date(12, 31, 2024)
    print("Start:", d_roll.format1())
    d_roll.increment()
    print("After increment:", d_roll.format1())  # 01/01/2025
    d_roll.decrement()
    print("After decrement:", d_roll.format1())  # 12/31/2024

    # Uncomment to test interactive input:
    # print("\n=== From user input ===")
    # user_date = Date.from_input()
    # print("You entered:", user_date)


if __name__ == "__main__":
    main()
