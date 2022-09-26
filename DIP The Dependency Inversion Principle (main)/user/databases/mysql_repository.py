from dataclasses import dataclass
from .interface import Repository


@dataclass
class MySqlRepository(Repository):

    def insert(self, data) -> str:
        return f'Registering {data} in the MySql database'

    def delete(self, data: str) -> str:
        return f'Deleting {data} from the MySql database'
