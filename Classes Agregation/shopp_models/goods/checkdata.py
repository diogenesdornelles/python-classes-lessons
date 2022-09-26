from dataclasses import dataclass


@dataclass
class CheckName:

    @staticmethod
    def check(name):
        if name != '' and isinstance(name, str):
            return True
        else:
            return False


@dataclass
class CheckPrice:
    @staticmethod
    def check(price):
        if price >= 0 and isinstance(price, float):
            return True
        else:
            return False


@dataclass
class CheckQuantity:
    @staticmethod
    def check(quantity):
        if quantity >= 0 and isinstance(quantity, int):
            return True
        else:
            return False
