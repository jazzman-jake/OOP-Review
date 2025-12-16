# main_shapes.py
from circle import Circle
from rectangle import Rectangle
from square import Square


def main():
    shapes = [
        Circle(0, 0, 4, "Circle_1"),
        Circle(1, 1, 9, "Circle_2"),
        Rectangle(10, 20, "Rectangle_1"),
        Rectangle(20, 30, "Rectangle_2"),
        Square(10, "Square"),
    ]

    print("--- Polymorphism check ---")
    for s in shapes:
        print(f"{s.name} Area = {s.area:.5f}")

    print("\n--- Getter/setter check ---")

    c1: Circle = shapes[0]
    print(f"{c1.name} Current:  {c1.radius} {c1.area:.5f}")
    c1.radius = c1.radius * 2
    print(f"{c1.name} Doubled:  {c1.radius} {c1.area:.5f}")

    r1: Rectangle = shapes[2]
    print(f"\n{r1.name} Current:  {r1.length} {r1.width} {r1.area:.0f}")
    r1.length *= 2
    r1.width *= 2
    print(f"{r1.name} Doubled:  {r1.length} {r1.width} {r1.area:.0f}")

    sq: Square = shapes[4]
    print(f"\n{sq.name} Current:  {sq.side} {sq.area:.0f}")
    sq.side *= 2
    print(f"{sq.name} Doubled:  {sq.side} {sq.area:.0f}")


if __name__ == "__main__":
    main()
