from abc import ABCMeta, abstractmethod
from dataclasses import dataclass, field
from types import NoneType

# Abstract classes that serve as a template for the classes that give rise to the various objects representing birds.
# Note that there are two classes divided by method specs - Interface Segregation Principle ISP.


@dataclass
class FlyingBird(metaclass=ABCMeta):
    __name: NoneType = field(default=None, init=False)

    @property
    @abstractmethod
    def name(self):
        raise NotImplementedError('Should implement name method')

    @name.setter
    @abstractmethod
    def name(self, value):
        raise NotImplementedError('Should implement setter name method')

    @property
    @abstractmethod
    def observer(self):
        raise NotImplementedError('Should implement name method')

    @observer.setter
    @abstractmethod
    def observer(self, value):
        raise NotImplementedError('Should implement setter name method')

    @abstractmethod
    def eat(self) -> str:
        raise NotImplementedError('Should implement eat method')

    @abstractmethod
    def fly(self) -> str:
        raise NotImplementedError('Should implement fly method')

    @abstractmethod
    def scream(self) -> str:
        raise NotImplementedError('Should implement scream method')


@dataclass
class NonFlyingBird(metaclass=ABCMeta):
    __name: NoneType = field(default=None, init=False)

    @property
    @abstractmethod
    def name(self):
        raise NotImplementedError('Should implement name method')

    @name.setter
    @abstractmethod
    def name(self, value):
        raise NotImplementedError('Should implement setter name method')

    @property
    @abstractmethod
    def observer(self):
        raise NotImplementedError('Should implement name method')

    @observer.setter
    @abstractmethod
    def observer(self, value):
        raise NotImplementedError('Should implement setter name method')

    @abstractmethod
    def eat(self) -> str:
        raise NotImplementedError('Should implement eat method')

    @abstractmethod
    def scream(self) -> str:
        raise NotImplementedError('Should implement scream method')


@dataclass
class FlyingBird2(metaclass=ABCMeta):
    __name: NoneType = field(default=None, init=False)

    @property
    @abstractmethod
    def name(self):
        raise NotImplementedError('Should implement name method')

    @name.setter
    @abstractmethod
    def name(self, value):
        raise NotImplementedError('Should implement setter name method')

    @abstractmethod
    def eat(self) -> str:
        raise NotImplementedError('Should implement eat method')

    @abstractmethod
    def fly(self) -> str:
        raise NotImplementedError('Should implement fly method')

    @abstractmethod
    def scream(self) -> str:
        raise NotImplementedError('Should implement scream method')


@dataclass
class NonFlyingBird2(metaclass=ABCMeta):
    __name: NoneType = field(default=None, init=False)

    @property
    @abstractmethod
    def name(self):
        raise NotImplementedError('Should implement name method')

    @name.setter
    @abstractmethod
    def name(self, value):
        raise NotImplementedError('Should implement setter name method')

    @abstractmethod
    def eat(self) -> str:
        raise NotImplementedError('Should implement eat method')

    @abstractmethod
    def scream(self) -> str:
        raise NotImplementedError('Should implement scream method')