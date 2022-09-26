from dataclasses import dataclass, field
from typing import List
from .goods import Good

Basket = List[Good]


@dataclass
class ShoppingCart:
    __goods: Basket = field(default_factory=list, init=False)

    def add(self, good: Good) -> None:
        self.__goods.append(good)
        print(f'{good.name} added!')
        result = self.show_info()
        print(result)

    def remove(self, good: Good) -> None:
        self.__goods.remove(good)
        print(f'{good.name} removed!')
        result = self.show_info()
        print(result)

    def total_price(self) -> float:
        total = 0
        for item in self.__goods:
            total += item.price
        return total

    def total_quantity(self) -> int:
        total = 0
        for item in self.__goods:
            total += item.quantity
        return total

    def show_info(self) -> str:
        result = ''
        for n, item in enumerate(self.__goods):
            result += '----' * 15 + '\n'
            result += f'{n + 1} - {item.info_good()}\n'
        return result

    def finalize(self) -> str:
        result = '====' * 15 + '\n'
        result += 'Completed purchases. Shopping cart information:\n'
        result += '====' * 15 + '\n'
        result += self.show_info()
        result += '----' * 15 + '\n'
        result += f'Number of items: {len(self.__goods)}\n'
        result += '----' * 15 + '\n'
        result += f'Quantity of items: {self.total_quantity()}\n'
        result += '----' * 15 + '\n'
        result += f'Total $UDS: {self.total_price():.2f}\n'
        result += '====' * 15 + '\n'
        result += f'Would you like to make payment now?'
        return result
