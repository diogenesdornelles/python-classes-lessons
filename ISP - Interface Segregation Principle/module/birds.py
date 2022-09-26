from dataclasses import dataclass, field
from .models import FlyingBird, NonFlyingBird
from .observer import Observer

# Concrete classes created from abstract classes.
# Note that there is a separation by characteristic, between birds that fly or not.


@dataclass
class Chicken(NonFlyingBird):
    __observer: Observer
    __name: str = field(default='chicken', init=False)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def observer(self):
        return self.__observer

    @observer.setter
    def observer(self, value):
        self.__observer = value

    def eat(self) -> str:
        return f'{self.observer.name} is watching {self.name} eat...'

    def scream(self) -> str:
        return f'{self.observer.name} is watching {self.name} scream...'


@dataclass
class Falcon(FlyingBird):
    __observer: Observer
    __name: str = field(default='falcon', init=False)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def observer(self):
        return self.__observer

    @observer.setter
    def observer(self, value):
        self.__observer = value

    def eat(self) -> str:
        return f'{self.observer.name} is watching {self.name} eat...'

    def fly(self) -> str:
        return f'{self.observer.name} is watching {self.name} fly...'

    def scream(self) -> str:
        return f'{self.observer.name} is watching {self.name} scream...'


@dataclass
class Penguin(NonFlyingBird):
    __observer: Observer
    __name: str = field(default='penguin', init=False)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def observer(self):
        return self.__observer

    @observer.setter
    def observer(self, value):
        self.__observer = value

    def eat(self) -> str:
        return f'{self.observer.name} is watching {self.name} eat... {self.__mate()}'

    def scream(self) -> str:
        return f'{self.observer.name} is watching {self.name} scream...'

    def __mate(self) -> str:
        return f'Now, {self.name} is mating.'
