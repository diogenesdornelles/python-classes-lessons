from dataclasses import dataclass, field
from repository import ManagerRepositories
from typing import ClassVar

#   Classes Inserter, Deleter, Modifier, Consultant have a greater proximity to the user interface. The means of linking
# with the next lower layer is attribute '__repository', object instantiated from the ManagerRepositories class


@dataclass
class Inserter:
    """Main class of the program that receives objects from 'Repository' class (dependence injection);
    :param __repository (Repository): Object from Repository class.
    """
    __repository: ManagerRepositories

    def insert_data(self, name: str, age: int) -> None:
        """ Method that uses methods of the Repository class to validate and insert data in the register;
        :param name: username;
        :param age: user age
        :return: None
        """
        registered = self.__repository.select_name(name)
        if registered:
            raise Exception(f'{name} already in registration!')
        else:
            self.__repository.insert(name, age)
            print(f'Registration user "{name}" successfully Complete!')


@dataclass
class Deleter:
    __repository: ManagerRepositories

    def delete_data(self, name: str) -> None:
        registered = self.__repository.select_name(name)
        if not registered:
            raise Exception(f'{name} not in registration!')
        else:
            self.__repository.remove(name)
            print(f'Deletion user "{name}" successfully Complete!')


@dataclass
class Modifier:
    __repository: ManagerRepositories
    name: ClassVar[str] = field(default='name (type "n")', init=False)
    age: ClassVar[str] = field(default='age (type "a")', init=False)

    def modify_name(self, number_contact: int, new_name: str):
        registered = self.__repository.select_number(number_contact)
        if not registered:
            raise Exception(f'{number_contact} not in registration!')
        else:
            self.__repository.change_name(number_contact, new_name)
            print(f'User n. "{number_contact}" successfully modified!')

    def modify_age(self, number_contact: int, new_age: int):
        registered = self.__repository.select_number(number_contact)
        if not registered:
            raise Exception(f'Contact n. {number_contact} not in registration!')
        else:
            self.__repository.change_age(number_contact, new_age)
            print(f'User n. "{number_contact}" successfully modified!')


@dataclass
class Consultant:
    __repository: ManagerRepositories

    def consult_users(self):
        self.__repository.consult()
