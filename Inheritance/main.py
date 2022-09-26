# https://www.youtube.com/watch?v=EPBjsPSYIXw&list=PLAgbpJQADBGLo24x_xBwGtTDO-bjwrFb_&index=13
# Orientação a Objetos em Python — Introdução à Herança

from dataclasses import dataclass, field
from types import NoneType
from typing import NoReturn


@dataclass
class Mother:
    name: str
    age: int
    last_name: str = field(default='Nunes', init=False)
    address: str = field(default='POA', init=False)

    def eat(self) -> None:
        print('Im eating')

    def study(self):
        print('Im studying')


@dataclass
class Father(Mother):
    job: str = field(default='JFRS')

    def fart(self) -> NoReturn:
        print('Poom!')

    def drink(self) -> NoReturn:
        print('Nice soda!')


@dataclass(init=True)
class Daughter(Father):
    name: str = field(default='Clara', init=False)
    job: NoneType = field(default=None)

    def to_sex(self) -> NoReturn:
        print(f'Im having sex with my wife!')


@dataclass
class GrandDaugther(Daughter):
    name: str = field(default='Lucy', init=False)
    job: NoneType = field(default=None)

    def to_play(self) -> NoReturn:
        print(f'Im playing!')


daughter = Daughter(34)
granddaughter = GrandDaugther(11)
print(daughter, '\v\n', granddaughter)
daughter.study()
daughter.fart()
