from dataclasses import dataclass
from operations import Inserter, Deleter, Modifier, Consultant
from repository import ManagerRepositories
from collections import namedtuple
from checker import CheckName, CheckAge


# https://www.youtube.com/watch?v=8FF8wasg7KU&list=PLAgbpJQADBGLo24x_xBwGtTDO-bjwrFb_&index=16
# Orientação a Objetos em Python — Polimorfismo

# Subtyping – a form of polymorphism – is when calling code can be independent of which class in the supported hierarchy
# it is operating on – the parent class or one of its descendants. Meanwhile, the same operation name among objects in
# an inheritance hierarchy may behave differently.

# Object that represents the layer in charge of generic database operations.

# register object of the Inserter class receives as a parameter the object of the
# ManagerRepositories class, so that all its methods can be used in the context of ManagerRepositories class


def call_menu() -> int:
    print('---' * 20)
    print('What do you want to do?')
    print('1 - Register user.')
    print('2 - Delete user.')
    print('3 - Modify user.')
    print('4 - Consult registration.')
    print('5 - Exit.')
    print('---' * 20)
    choice = int(input('Choose an option above:'))
    print('---' * 20)
    return choice


@dataclass
class Interface:
    @staticmethod
    def menu():
        proceed = True
        while proceed:

            choice = call_menu()

            if choice == 1:
                Option1.insert()

            elif choice == 2:
                Option2.delete()

            elif choice == 3:
                Option3.modify()

            elif choice == 4:
                Option4.consult()

            elif choice == 5:
                proceed = False

        print('Program being terminated')


class Option1:

    @staticmethod
    def insert():
        Person = namedtuple('Person', ['name', 'age'])
        result = False
        while not result:
            name = input('Inform the name:')
            age = int(input('Inform the age:'))
            print('---' * 20)
            name_checked = CheckName(name)
            age_checked = CheckAge(age)
            if name_checked.result and age_checked.result:
                person = Person(name_checked.name, age_checked.age)
                repo = ManagerRepositories()
                register = Inserter(repo)
                register.insert_data(person.name, person.age)
                result = True
            else:
                pass


class Option2:
    @staticmethod
    def delete():
        name = input('Inform the name:')
        print('---' * 20)
        repo = ManagerRepositories()
        deleter = Deleter(repo)
        deleter.delete_data(name)


class Option3:
    @staticmethod
    def modify():
        number = int(input('Inform the number"s user:'))
        print('---' * 20)
        repo = ManagerRepositories()
        changer = Modifier(repo)
        result = False
        while not result:
            choice = input(f'Want to change {Modifier.name} or {Modifier.age}?')
            if choice != 'n' or choice != 'a':
                print('Option not properly informed...')
                print('---' * 20)
            else:
                if choice == 'n':
                    name = input('Inform new name:')
                    print('---' * 20)
                    changer.modify_name(number, name)
                elif choice == 'a':
                    age = int(input('Inform new age:'))
                    print('---' * 20)
                    changer.modify_age(number, age)
                result = True


class Option4:
    @staticmethod
    def consult():
        repo = ManagerRepositories()
        consulter = Consultant(repo)
        consulter.consult_users()


var = Interface()
var.menu()
