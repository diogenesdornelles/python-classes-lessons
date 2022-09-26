from dataclasses import dataclass
from .interface import Repository


@dataclass
class MongoRepository(Repository):

    def insert(self, data) -> str:
        return f'Registering {data} in the MongoDB database'

    def delete(self, data: str) -> str:
        return f'Deleting {data} from the MongoDB database'
