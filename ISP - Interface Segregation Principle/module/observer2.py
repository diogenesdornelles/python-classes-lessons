from dataclasses import dataclass
from .bird2 import Penguin2, Falcon2, Chicken2

Bird = [Penguin2 | Falcon2 | Chicken2]


@dataclass
class Observer2:
    name: str

    def note_eat(self, bird: Bird):
        return f'{self.name} is watching {bird.name} {bird.eat()}'

    def note_fly(self, bird: Bird):
        try:
            return f'{self.name} is watching {bird.name} {bird.fly()}'
        except AttributeError:
            return f'{bird.name} dont know fly!'

    def note_scream(self, bird: Bird):
        return f'{self.name} is watching {bird.name} {bird.scream()}'
