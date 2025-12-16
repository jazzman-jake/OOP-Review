# circle.py
from __future__ import annotations
import math
from basic_shape import BasicShape


class Circle(BasicShape):
    def __init__(self, x_center: float, y_center: float, radius: float, name: str = "Circle"):
        super().__init__(name)
        self._x_center = x_center
        self._y_center = y_center
        self._radius = radius
        self.calc_area()

    # center & radius getters
    @property
    def x_center(self) -> float:
        return self._x_center

    @property
    def y_center(self) -> float:
        return self._y_center

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, r: float) -> None:
        self._radius = r
        self.calc_area()

    def calc_area(self) -> None:
        a = math.pi * (self._radius ** 2)
        self._set_area(a)
