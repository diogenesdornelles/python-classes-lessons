from methods import Select, Insert
from dataclasses import dataclass, field

TypeSelect = Select
TypeInsert = Insert


@dataclass
class Repository:
    __insert: TypeInsert = field(default=Insert())  # Unnecessary do inheritance. FACADE pattern
    __select: TypeSelect = field(default=Select())  # Others classes methods are passed directly to attributes.

    def insert_by_id(self, *args: tuple) -> None:
        self.__insert.insert(*args)

    def select_by_id(self, *args: tuple) -> None:
        self.__select.select(*args)
