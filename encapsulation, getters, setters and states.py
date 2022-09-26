# https://www.youtube.com/watch?v=RJWucpLGBng&list=PLAgbpJQADBGLo24x_xBwGtTDO-bjwrFb_&index=3
# Orientação a Objetos em Python — Encapsulamento Privado
# https://www.youtube.com/watch?v=rHSQ8oam8bQ&list=PLAgbpJQADBGLo24x_xBwGtTDO-bjwrFb_&index=4
# Orientação a Objetos em Python — Getters / Setters e Estados
from dataclasses import dataclass
import re


@dataclass
class Person:
    __name: str
    __age: int
    __cpf: str

    def __post_init__(self):
        validate_name = self.__validate_name()
        validate_age = self.__validate_age()
        validate_cpf = self.__validate_cpf()
        if False not in [validate_name, validate_age, validate_cpf]:
            return self.__name, self.__age, self.__cpf

    def __validate_name(self):
        if self.__name != '' and isinstance(self.__name, str):
            return True
        else:
            raise ValueError('Name must be given')

    def __validate_age(self):
        if self.__age >= 0 and isinstance(self.__age, int):
            return True
        else:
            raise ValueError('Age positive must be given')

    def __validate_cpf(self, new_cpf: str = None):
        cpf_compile = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')
        if new_cpf is not None:
            validate = cpf_compile.findall(new_cpf)
        else:
            validate = cpf_compile.findall(self.__cpf)
        if validate:
            return True
        else:
            raise ValueError('CPF must be given in format "xxx.xxx.xxx-xx"')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name != '' and isinstance(new_name, str):
            self.__name = new_name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if new_age != '' and isinstance(new_age, int):
            self.__age = new_age

    @property
    def cpf(self):
        return self.__cpf  # The context of class can obtain the private atribute.

    @cpf.setter
    def cpf(self, new_cpf):
        validade_cpf = self.__validate_cpf(new_cpf)
        if validade_cpf:
            self.__cpf = new_cpf

    def to_run(self) -> None:
        print(f'{self.__name} is running...')

    def to_drink(self, drink: str = '') -> None:
        drinks_not_allowed = ['beer', 'brandy', 'whiskey', 'amarula']
        if drink.strip().lower() in drinks_not_allowed:
            self.__show_doc()
            if self.__age >= 18:
                print(f'{self.__name} is age {self.__age}. Now, hes drinking {drink}.')
            else:
                print(f'{self.__name} is under 18, cant drink {drink}.')
        else:
            print(f'{self.__name} is drinking {drink}.')

    # Private method: inaccessible to user, only in class/object context.
    def __show_doc(self) -> None:
        print(f'{self.__name} show document n. {self.__cpf}')


# Atribute cpf set private by double underscores on initializer method, so that it's only accessible in class context.
# This is encapsulation. Hidden parameters objects. Therefore, inaccessible directly by user.
# However, possible create a method to access him indirectly. Including, set a property decorator to access it as if
# it were an atribute.
# Another advantage is the possibility of create a setter method to validate operations of modification.

print("it's my object:")
ronaldo = Person('Ronaldo', 30, '0a4.801.710-84')
ronaldo.name = 'Xavier'
ronaldo.cpf = '004.801.710-99'
print(ronaldo)
print()
# Note that 'cpf' isn't the parameter, but the method called by object. Without setter 'ronaldo.cpf = 'any' doesn't
# work.
print('cpf number:')
print(ronaldo.cpf)
print()
print('person will run:')
print(ronaldo.to_run())
print()
print('person will drink:')
print(ronaldo.to_drink('beer'))
print()
