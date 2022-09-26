from dataclasses import dataclass
from inputs import choose_one_operation, inform_id
from repository import Repository

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
