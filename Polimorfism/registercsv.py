from dataclasses import dataclass
from typing import List, Dict, Final
from checkdb import arc_exists


Data = [Dict, List[Dict]]
DATA_BASE: Final = 'database.csv'


@dataclass
class LoadDB:

    @staticmethod
    def load_data() -> list:
        arc_exists(DATA_BASE)
        with open(DATA_BASE, 'r', encoding="utf-8") as csv:
            data_db = csv.read()
            data_list = data_db.split('\n')
        return data_list


@dataclass
class SearchDB(LoadDB):

    def search(self, name: str) -> bool:
        data_list = self.load_data()
        if data_list.find(name) >= 0:
            return True
        else:
            return False


@dataclass
class InsertDB(LoadDB):
    pass

    # def save_person(self, person: Dict) -> None:
    #     result = self.load_data()
    #     contact = f'{person.}'
    #     result[1].append(person)
    #     result = json.dumps(result, indent=2, ensure_ascii=False, sort_keys=False)
    #     with open(DATA_BASE, 'w+', encoding="utf-8") as js:
    #         js.write(result)
