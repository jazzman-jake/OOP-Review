# square.py
from __future__ import annotations
from rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side: float, name: str = "Square"):
        self._side = side
        super().__init__(side, side, name)
        # ensure name set in base class again if needed
        self.name = name

    @property
    def side(self) -> float:
        return self._side

    @side.setter
    def side(self, s: float) -> None:
        self._side = s
        # update length and width in parent
        self.length = s
        self.width = s
        # calc_area will be called by the setters
