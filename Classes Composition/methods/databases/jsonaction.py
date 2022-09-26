from dataclasses import dataclass
from typing import Final, Dict, List
import json
from .checkbases import arc_exists, move_to_dir_databases
import os

Data = [Dict, List[Dict]]
DATA_BASE: Final = 'database.json'


@dataclass
class ManagerJsonDB:

    @staticmethod
    def load() -> Data:
        arc_exists(DATA_BASE)
        current_dir = move_to_dir_databases()
        with open(DATA_BASE, 'r', encoding="utf-8") as js:
            loaded_data: str = js.read()
        data_db: Data = json.loads(loaded_data)
        os.chdir(current_dir)
        return data_db

    @staticmethod
    def update(data) -> None:
        current_dir = move_to_dir_databases()
        result: str = json.dumps(data, indent=2, ensure_ascii=False, sort_keys=False)
        with open(DATA_BASE, 'w+', encoding="utf-8") as js:
            js.write(result)
        os.chdir(current_dir)

    def insert(self, *data: tuple) -> None:

        data_db: Data = self.load()
        id_list: List = data_db[1]

        if id_list:
            id_dict: Dict = data_db[1][0]
            indexes = range(len(id_dict) + 1,  len(id_dict) + len(data) + 1)
            indexes = [f'n. {index}' for index in indexes]
            dict_data = dict(zip(indexes, data))
            data_db[1][0].update(dict_data)

        else:
            indexes = range(len(data) + 1)
            indexes = [f'n. {index + 1}' for index in indexes]
            dict_data = dict(zip(indexes, data))
            data_db[1].append(dict_data)

        self.update(data_db)

    def select(self, *data: tuple) -> None:
        data_db: Data = self.load()
        id_list: List = data_db[1]

        if id_list:
            id_dict: Dict = id_list[0]
            positive = [_id.upper() for _id in data[0] if _id.upper() in id_dict.values()]
            negative = [_id.upper() for _id in data[0] if _id.upper() not in id_dict.values()]

            if positive:
                [print(f'Id {_id} was selected.') for _id in positive]
            if negative:
                [print(f'Id {_id} not founded.') for _id in positive]
        else:
            print('Error: database is empty.')

    # @staticmethod
    # def delete():
