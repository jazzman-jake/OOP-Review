# basic_shape.py
from __future__ import annotations
from abc import ABC, abstractmethod


class BasicShape(ABC):
    """
    Abstract base class for shapes.
    """

    def __init__(self, name: str):
        self._name: str = name
        self._area: float = 0.0

    # name property
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    # area property (read-only from outside)
    @property
    def area(self) -> float:
        return self._area

    def _set_area(self, value: float) -> None:
        self._area = value

    @abstractmethod
    def calc_area(self) -> None:
        """Subclasses must compute and store area in _area."""
        pass
