# rectangle.py
from __future__ import annotations
from basic_shape import BasicShape


class Rectangle(BasicShape):
    def __init__(self, length: float, width: float, name: str = "Rectangle"):
        super().__init__(name)
        self._length = length
        self._width = width
        self.calc_area()

    @property
    def length(self) -> float:
        return self._length

    @length.setter
    def length(self, l: float) -> None:
        self._length = l
        self.calc_area()

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, w: float) -> None:
        self._width = w
        self.calc_area()

    def calc_area(self) -> None:
        a = self._length * self._width
        self._set_area(a)
