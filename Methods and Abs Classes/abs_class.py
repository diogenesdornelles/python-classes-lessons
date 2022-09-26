from abc import ABC, abstractmethod
from dataclasses import dataclass, field

#  If I don't pass class ABC as a parameter to the abstract class, I can instantiate objects normally, even if one of
#  its methods is abstract.


@dataclass
class AbstractClass(ABC):
    attribute: str = field(default='Hello World!')

    @staticmethod
    def method(element: str) -> None:
        print(element)

    @staticmethod
    @abstractmethod
    def abs_method() -> None:  # child class must implement abstract method obligatorily
        pass
