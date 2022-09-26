# https://www.youtube.com/watch?v=XVQC1b2yPYQ&list=PLAgbpJQADBGLo24x_xBwGtTDO-bjwrFb_&index=9
# Orientação a Objetos em Python - SOLID (O) - Princípio Aberto / Fechado

# OCP - Open-Closed Principle
# https://en.wikipedia.org/wiki/Open%E2%80%93closed_principle#:~:text=Bertrand%20Meyer%20is%20generally%20credited,is%20still%20available%20for%20extension.
# "software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification"

# 1) A module will be said to be open if it is still available for extension. For example, it should be possible to add
# fields to the data structures it contains, or new elements to the set of functions it performs.

# 2) A module will be said to be closed if [it] is available for use by other modules. This assumes that the module has
# been given a well-defined, stable description (the interface in the sense of information hiding).
from dataclasses import dataclass, field


class Circo1:

    # Example of function closed. If we want to add new behavior, we have to add some cod in it.
    def show(self, tp):
        if tp == 1:
            self.introduce_juggler()
        elif tp == 2:
            self.introduce_clown()

    def introduce_juggler(self):
        print('clown is presenting his show')

    def introduce_clown(self):
        print('juggler is presenting his show')


########################################################################################################################

# The artist uses the circus to presenting his shows.
# The solution bellow increase behavior, but without change code, by adding new classes of artists.

"""force the other subclasses to have the attribute name"""


@dataclass
class Presenter:
    name: str = field(default='Presenter')


@dataclass
class Juggler(Presenter):
    name: str = field(default='Juggler')


@dataclass
class Clown(Presenter):
    name: str = field(default='Clown')
    

@dataclass
class Tamer(Presenter):
    name: str = field(default='Tamer')


@dataclass
class TrapezeArtist(Presenter):
    name: str = field(default='Trapeze artist')


@dataclass
class Circo2:

    # Example of function opened. If we want to add new behavior, we have to add some cod outer it.
    @staticmethod
    def present_show(presenter):
        print(f'{presenter.name} is presenting his show!')


circ = Circo2
clown = Clown()
juggler = Juggler()
tamer = Tamer()
trapeze_artist = TrapezeArtist()

# print(circ)
# print(clown)
# print(juggler)
circ.present_show(clown)
