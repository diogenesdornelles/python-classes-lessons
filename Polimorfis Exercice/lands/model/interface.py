from abc import ABCMeta, abstractmethod
from dataclasses import dataclass


@dataclass
class FormalInterface(metaclass=ABCMeta):

    @abstractmethod
    def get_perimeter(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def get_area(self) -> float:
        raise NotImplementedError
