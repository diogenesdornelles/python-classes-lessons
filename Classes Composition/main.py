from dataclasses import dataclass
from inputs import choose_one_operation, inform_id
from repository import Repository


# Composition is an association relationship between classes in object-oriented programming, where one class (the container or composite) contains or is composed of other classes (the components or parts). 
# The composition relationship implies a strong "whole-part" relationship, where the lifecycle of the component objects is tightly tied to the lifecycle of the container. In other words, if the container is destroyed, all of its component objects are also destroyed.
# Composition is a more specific and stronger form of association compared to aggregation. In composition, the component objects are considered an integral part of the container, and they cannot exist independently outside of it. This means that the container class is responsible for creating, managing, and destroying its component objects.
# In UML (Unified Modeling Language), composition is typically represented by a diamond-shaped arrowhead on the side of the container class pointing towards the component class, similar to aggregation.
# The difference lies in the strength of the relationship and the lifecycle management of the component objects.


# https://www.youtube.com/watch?v=px7UphXv4B8&list=PLAgbpJQADBGLo24x_xBwGtTDO-bjwrFb_&index=22
# Orientação a Objetos em Python — Composição de Classes

# Composition: Relation used to escape the idea of inheritance. Other classes will compose the behavior that a
# main class will have.


def menu() -> None:
    print('===' * 15)
    print('System')
    print('===' * 15)
    print('Operations available:')
    print('1 - Insert data by Id')
    print('2 - Select data by Id')
    print('===' * 15)


@dataclass
class MainLooping:

    @staticmethod
    def looping() -> None:
        result1 = True
        while result1:
            menu()
            entry_op = choose_one_operation()
            entry_id = inform_id()
            repository = Repository()
            #  insert data
            if entry_op == 1:
                repository.insert_by_id(*entry_id)
            # select data
            elif entry_op == 2:
                repository.select_by_id(*entry_id)
            other = input('Wish to do another operation? (enter: no)')
            if other == '':
                result1 = False


var = MainLooping()
var.looping()
