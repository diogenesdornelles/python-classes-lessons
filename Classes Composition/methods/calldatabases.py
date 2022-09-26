from dataclasses import dataclass
from abc import ABCMeta, abstractmethod
from .databases import ManagerJsonDB


@dataclass
class ManagerDB(metaclass=ABCMeta):

    @abstractmethod
    def insert(self, *data: tuple):
        raise NotImplementedError

    @abstractmethod
    def select(self, *data: tuple):
        raise NotImplementedError


@dataclass
class JsonDB(ManagerDB):

    def insert(self, *data: tuple) -> None:
        inserter = ManagerJsonDB()
        inserter.insert(*data)

    def select(self, *data: tuple) -> None:
        picker = ManagerJsonDB()
        picker.select(*data)


@dataclass
class PostgreSqlDB(ManagerDB):

    def insert(self, data: dict):
        pass
        # ManagerPostgreSqlDB.insert(data)

    def select(self, data: dict):
        pass
        # ManagerPostgreSqlDB.select(data)
