from abs_class import AbstractClass
from dataclasses import dataclass


# https://www.youtube.com/watch?v=itchdl_0prw&list=PLAgbpJQADBGLo24x_xBwGtTDO-bjwrFb_&index=17
# Orientação a Objetos em Python — Métodos e Classes Abstratas

# In an abstracted class you cannot instantiate an object
# abs is scoped to produce elements from which the other child classes are forcibly implemented.
# So they work more like a mold.

# As abstract method implemented in a class abstract forces child subclasses to implement these too.

# For python, an abstract class must have, at least, one abstract method. Once recognized as an abstract class, it is
# not possible to instantiate objects


@dataclass
class Child(AbstractClass):

    def show_method(self) -> None:
        print(self.attribute)

    def abs_method(self) -> None:  # Class Child must implement all abstract methods.
        print('Child"s abstractmethod implemented')


print('SUPERCLASS (abs mode):')
print('CHILD CLASS:')
child = Child()
print(child.attribute + ' = Mother"s attribute called in child')
child.show_method(), print(' = Mother"s method called in child')
child.method('Called superclass "method" in child class.')
print()
print('SUPERCLASS:')
# mother = AbstractClass()  # TypeError: Can't instantiate abstract class AbstractClass with abstract method abs_method.
# print(mother.attribute)
# mother.method('Called method in superclass.')
# print()
# although not accessible through an object, the attributes and methods of the abstract class can be accessed by itself
print(AbstractClass.method('Hello world!'))
print(AbstractClass.attribute)
print(AbstractClass.abs_method())
