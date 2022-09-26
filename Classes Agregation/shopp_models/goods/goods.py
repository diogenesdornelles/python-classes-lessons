from dataclasses import dataclass
from .checkdata import CheckPrice, CheckName, CheckQuantity


@dataclass
class Good:
    __name: str
    __price: float
    __quantity: int

    def __post_init__(self):
        check_name = CheckName.check(self.__name)
        check_price = CheckPrice.check(float(self.__price))
        check_quantity = CheckQuantity.check(self.__quantity)
        result = [check_name, check_price, check_quantity]
        print(result)
        if False not in result:
            return self.__name, self.__price, self.__quantity
        else:
            raise ValueError

    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> float:
        return self.__price

    @property
    def quantity(self) -> int:
        return self.__quantity

    def info_good(self) -> str:
        return f'Name: {self.__name} | Price: {self.__price} | Quantity {self.__quantity}'
