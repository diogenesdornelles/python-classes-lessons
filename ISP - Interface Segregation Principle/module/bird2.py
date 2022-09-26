from dataclasses import dataclass, field
from .models import NonFlyingBird2, FlyingBird2

# Concrete classes created from abstract classes.
# Note that there is a separation by characteristic, between birds that fly or not.


@dataclass
class Chicken2(NonFlyingBird2):
    __name: str = field(default='chicken', init=False)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def eat(self) -> str:
        return f'eat korn...'

    def scream(self) -> str:
        return f' scream pó pó pó..'


@dataclass
class Falcon2(FlyingBird2):
    __name: str = field(default='falcon', init=False)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def eat(self) -> str:
        return f' eat a mouse...'

    def fly(self) -> str:
        return f' fly high in the sky...'

    def scream(self) -> str:
        return f' scream over the mountain...'


@dataclass
class Penguin2(NonFlyingBird2):
    __name: str = field(default='penguin', init=False)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def eat(self) -> str:
        return f' eat fish... {self.__mate()}'

    def scream(self) -> str:
        return f' scream ...'

    @staticmethod
    def __mate() -> str:
        return f'Now, is mating.'
