from dataclasses import dataclass
from typing import NoReturn, Dict
from registerjson import SearchDB, InsertDB, DeleteDB, ChangeDB, ConsultDB
# from registercsv import SearchDB, InsertDB

# "ManagerRepositories" is in a layer closer to the data manipulation interface in databases.


@dataclass
class ManagerRepositories:
    """
    Class that manages all generic operations involving database connections. Yet, csv and json.
    """
    @staticmethod
    def select_name(name: str) -> bool:
        search_user: SearchDB = SearchDB()
        result: bool = search_user.search_name(name)
        return result

    @staticmethod
    def select_number(number: int) -> bool:
        search_user: SearchDB = SearchDB()
        result: bool = search_user.search_number_contact_active(number)
        return result

    @staticmethod
    def insert(name: str, age: int) -> NoReturn:
        user_for_registration: Dict = {"Name": name, "Age": age}
        insert: InsertDB = InsertDB()
        insert.save_person(user_for_registration)

    @staticmethod
    def remove(name: str):
        deleted_person: DeleteDB = DeleteDB()
        deleted_person.delete_person(name)

    @staticmethod
    def change_name(number_contact: int, new_name: str) -> NoReturn:
        change: ChangeDB = ChangeDB()
        change.change_person(number_contact=number_contact, name=new_name)

    @staticmethod
    def change_age(number_contact: int, new_age: int) -> NoReturn:
        change: ChangeDB = ChangeDB()
        change.change_person(number_contact=number_contact, age=new_age)

    @staticmethod
    def consult():
        consult: ConsultDB = ConsultDB()
        consult.show_users_actives()
