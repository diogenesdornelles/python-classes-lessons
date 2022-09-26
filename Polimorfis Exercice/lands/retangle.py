from .model import FormalInterface
from dataclasses import dataclass


@dataclass
class LandRetangle(FormalInterface):
    __length: float
    __width: float

    def get_perimeter(self) -> float:
        return (self.__length * 2) + (self.__width * 2)

    def get_area(self) -> float:
        return self.__length * self.__width
