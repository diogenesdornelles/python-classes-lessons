from .model import FormalInterface
from dataclasses import dataclass


@dataclass
class LandSquare(FormalInterface):
    __side: float

    def get_perimeter(self) -> float:
        return self.__side * 4

    def get_area(self) -> float:
        return self.__side ** 2
