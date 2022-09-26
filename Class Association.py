# https://www.youtube.com/watch?v=HAtr_Sk4xiY&list=PLAgbpJQADBGLo24x_xBwGtTDO-bjwrFb_&index=8
# Orientação a Objetos em Python — Associação de Classes
from dataclasses import dataclass

# In an association, one object from a class uses services from another, but one exists independently of the other.


@dataclass
class LightSwitch:
    __room: str

    def turn_on(self, name: str) -> None:
        print(f'{name} turn on light in {self.__room}.')

    def turn_off(self, name: str) -> None:
        print(f'{name} turn off light in {self.__room}.')


@dataclass
class Person:
    __name: str

    def turn_on_light(self, lightswitch: LightSwitch) -> None:
        lightswitch.turn_on(self.__name)

    def turn_off_light(self, lightswitch: LightSwitch) -> None:
        lightswitch.turn_off(self.__name)

    def sleep(self) -> None:
        print(f'{self.__name} going to sleep.')


otavio = Person('Otavio')
lightswitch_room = LightSwitch('Room')

# These calls have the same effect, showing that the classes are independent:
otavio.turn_on_light(lightswitch_room)
lightswitch_room.turn_on('Otávio')

# In the first one, object 'otavio', from class Person, uses services (methods) from object/class LightSwitch
# 'lightswitch_room'. Note that object 'otavio' exists by itself.
# In the other hand, in the second case, methods from class LightSwitch are callable directly, which reinforces the
# idea of independence between both classes.
