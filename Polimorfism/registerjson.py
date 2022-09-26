from dataclasses import dataclass
from typing import List, Dict, Final
from checkdb import arc_exists
import json

Data = [Dict, List[Dict]]
DATA_BASE: Final = 'database.json'


@dataclass
class LoadDB:

    @staticmethod
    def load_data() -> Data:
        arc_exists(DATA_BASE)
        with open(DATA_BASE, 'r', encoding="utf-8") as js:
            loaded_data: str = js.read()
        data_db: Data = json.loads(loaded_data)
        print('Loading data from database...')
        return data_db


@dataclass
class SearchDB(LoadDB):

    def search_name(self, name: str) -> bool:
        data_db: Data = self.load_data()
        contact_list: List = data_db[1]
        if contact_list:
            for person in contact_list:
                if name == person['Name']:
                    print(f'{name} founded in database...')
                    return True
        print(f'{name} not founded in database...')
        return False

    def search_number_contact_active(self, number: int) -> bool:
        data_db: Data = self.load_data()
        contact_list: List = data_db[1]
        if contact_list:
            for person in contact_list:
                if number == int(person['Number']):
                    print(f'Contact {person["Number"]} number {number} founded in database...')
                    if person['Active']:
                        return True
                    else:
                        print(f'Contact {person["Number"]} number {number} is inactive in database...')
                        return False
            print(f'{number} not founded in database...')
        else:
            print(f'{number} not founded in database...')
            return False


@dataclass
class InsertDB(LoadDB):

    def save_person(self, person: Dict) -> None:
        data_db: Data = self.load_data()
        contact_list: List = data_db[1]
        person: Dict = TreatEntry.treat(contact_list, person)
        data_db[1].append(person)
        print('Inserting new user on database...')
        UpdateDB.update(data_db)


@dataclass
class DeleteDB(SearchDB):
    def delete_person(self, name: str) -> None:
        data_db: Data = self.load_data()
        for person in data_db[1]:
            if name == person['Name']:
                person['Active'] = False
                break
        print('Deleting contact from database...')
        UpdateDB.update(data_db)


@dataclass
class ChangeDB(SearchDB):
    def change_person(self, **kwargs) -> None:
        data_db: Data = self.load_data()
        for person in data_db[1]:
            if kwargs['number_contact'] == int(person['Number']):
                if 'age' in kwargs:
                    person['Age'] = kwargs['age']
                    print(f"Assigning {person['Name']} new age {kwargs['age']}...")
                    break
                elif 'name' in kwargs:
                    person['Name'] = kwargs['name']
                    print(f"Assigning contact n. {kwargs['number_contact']} new name {kwargs['name']}...")
                    break
        UpdateDB.update(data_db)


@dataclass
class TreatEntry:
    @staticmethod
    def treat(contact_list: list, person: Dict) -> Dict:
        print(f"Assigning {person['Name']} number and active status...")
        number: int = len(contact_list)
        person['Number'] = f'{number + 1}'
        person['Active'] = True
        print(f"{person['Name']} contact n. {person['Number']}...")
        return person


@dataclass
class UpdateDB:
    @staticmethod
    def update(data: Data) -> None:
        print('Updating database...')
        result: str = json.dumps(data, indent=2, ensure_ascii=False, sort_keys=False)
        with open(DATA_BASE, 'w+', encoding="utf-8") as js:
            js.write(result)


class ConsultDB(LoadDB):
    def show_users_actives(self) -> None:
        data_db: Data = self.load_data()
        contact_list: List = data_db[1]
        print('All contact actives:')
        for person in contact_list:
            if person['Active']:
                print(person)
