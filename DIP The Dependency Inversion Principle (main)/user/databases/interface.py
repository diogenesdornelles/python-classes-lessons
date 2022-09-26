from dataclasses import dataclass
from abc import ABCMeta, abstractmethod


@dataclass
class Repository(metaclass=ABCMeta):
    @abstractmethod
    def insert(self, data) -> str:
        raise NotImplementedError

    @abstractmethod
    def delete(self, data: str) -> str:
        raise NotImplementedError
