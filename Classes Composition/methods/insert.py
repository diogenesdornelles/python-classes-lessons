from dataclasses import dataclass
from .calldatabases import JsonDB


@dataclass
class Insert:

    @staticmethod
    def insert(*args: tuple) -> None:
        inserter = JsonDB()
        inserter.insert(*args)
