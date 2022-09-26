from dataclasses import dataclass, field

NameAnimal = NameBird = NameHuman = str


@dataclass
class Animal:
    name: NameAnimal = field(default='Animal', init=False)

    def eat(self) -> str:
        return f'{self.name} eat'

    def sleep(self) -> str:
        return f'{self.name} sleep'

    def walk(self) -> str:
        return f'{self.name} walk'


@dataclass
class Bird(Animal):
    name: NameBird = field(default='Bird', init=False)

    def sing(self) -> str:
        return f'{self.name} sing'


@dataclass
class Penguin(Bird):
    name: NameBird = field(default='Penguin', init=False)

    def slide(self) -> str:
        return f'{self.name} sliding on ice'


@dataclass
class Human:
    name: NameHuman = field(default='Diogenes', init=False)

    def observe(self, animal: [Animal | Bird]) -> str:
        return f'{self.name} is observing the {animal.sing()} '


diogenes = Human()
penguin = Penguin()

print(diogenes.observe(penguin))

print(penguin.eat())