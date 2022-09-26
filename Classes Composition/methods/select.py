from dataclasses import dataclass
from .calldatabases import JsonDB


@dataclass
class Select:

    @staticmethod
    def select(*args: tuple) -> None:
        picker = JsonDB()
        picker.select(args)
