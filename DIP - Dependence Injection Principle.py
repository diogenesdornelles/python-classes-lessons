# https://www.youtube.com/watch?v=aZH5bRvRDyk&list=PLAgbpJQADBGLo24x_xBwGtTDO-bjwrFb_&index=11
# Orientação a Objetos em Python — Injeção de Dependência.

from dataclasses import dataclass, field

########################################################################################################################
# Example without using dependency injection.
# Note that obj 'ana', from class 'person', must be instantiated, as well 'house'. House obj must be given as parameter
# of methods in class person to be useful. In this case, the dependence is implicit between classes.


@dataclass
class House:
    address: str = field(default='Vitoria Street')

    def turn_on_light(self) -> None:
        print('The lights are on')

    def get_address(self):
        return self.address


@dataclass
class Person:
    name: str

    def enter_the_place(self, place: any) -> None:
        place.turn_on_light()

    def present_the_place(self, place: any) -> None:
        address = place.get_address()
        print(address)


house = House()
ana = Person('Ana')
print(ana)
ana.enter_the_place(house)
ana.present_the_place(house)

print()
print()
########################################################################################################################
# Example with using dependency injection.
# Note that obj 'joao', from class 'Person2', must be instantiated, like 'house' too. However, in this time, house obj
# are given as atribute of 'joao', so that all methods from class 'House2' are directly accessible in Person2 scope, by
# using atribute 'self.local'.
# In this case, the dependence is explicit between classes.


@dataclass
class House2:
    address: str = field(default='Vitoria Street')

    def turn_on_light(self) -> None:
        print('The lights are on')

    def get_address(self):
        return self.address


@dataclass
class Person2:
    name: str
    local: House2

    def enter_the_place(self) -> None:
        self.local.turn_on_light()

    def present_the_place(self) -> str:
        address = self.local.get_address()
        return address


house = House2()
joao = Person2('joao', house)
local = joao.present_the_place()
print(local)
