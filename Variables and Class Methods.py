# https://www.youtube.com/watch?v=i76UF0inUV0&list=PLAgbpJQADBGLo24x_xBwGtTDO-bjwrFb_&index=6
# Orientação a Objetos em Python — Variáveis e Métodos de Classe
from dataclasses import dataclass, field
from typing import Any


class MyClass:
    static = 'SOLID'  # Class variable or static variable. Behave like global variable.

    def __init__(self, state) -> None:
        self.state = state

    def print_static(self):
        print(self.static)  # Only works if called in self.

    def change_static_obj(self):
        self.static = 'PLASMA'  # Only change variable in self.

    @classmethod
    def change_static_cls(cls):
        cls.static = 'Bose-Einstein Condensed'  # Same thing to do "MyClass.static"


if __name__ == '__main__':
    obj1 = MyClass(True)
    obj2 = MyClass(False)
    obj3 = MyClass(False)

    obj2.static = 'SOLID'  # If you change the value of static variable on object, the change remains.
    MyClass.static = 'LIQUID'  # If you change the class static parameter, all objects (self) chance too.
    obj1.static = 'GAS'

    # Principle: the context of objects with them remain.

    print(obj1.static)
    print(obj2.static)
    print(MyClass.static)

    print()
    obj1.change_static_obj()

    print(obj1.static)  # Changed only in obj context.
    print(obj2.static)
    print(MyClass.static)

    print()
    obj2.change_static_cls()  # with classmethod I can change class variable from an any object.

    print(obj1.static)
    print(obj2.static)
    print(MyClass.static)
    print(obj3.static)

print()


@dataclass
class Store:
    tax: float = field(default=1.03, init=False)  # Static variable on dataclasses.
    __address: str

    def show_address(self):
        print(self.__address)

    @classmethod
    def sell_item(cls, value: float, item: str, store: Any):
        print(f'Store {store.__address} sells {item} for {value * cls.tax}')

    @classmethod
    def change_tax(cls, new: float) -> None:
        cls.tax = new


sr1 = Store('TK')
sr2 = Store('BG')
sr3 = Store('POA')
sr4 = Store('CXS')

# sr2.tax = 1.33
# Store.tax = 2
# sr1.tax = 1.56
#
# print(sr1.tax)
# print(sr2.tax)
# print(sr3.tax)
# print(Store.tax)

print(sr3.sell_item(100, 'handbag', sr3))
sr2.change_tax(1.56)
print(sr2.sell_item(100, 't-shirt', sr2))
sr3.change_tax(1.4)
print(sr1.sell_item(100, 'tennis', sr3))

