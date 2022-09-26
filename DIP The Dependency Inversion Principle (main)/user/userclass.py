from dataclasses import dataclass, field
from typing import Any
from .databases import Repository  # MongoRepository, MySqlRepository

# the object of the class that executes its specific methods (store and remove) accesses the generic methods declared
# in the abstract super class and not the methods defined in the classes referring to the object that is its attribute,
# in case, MongoRepository, MySqlRepository.
# MongoRepository or MySqlRepository are Repository, but not necessarily the other way around.


@dataclass
class User:
    __repository: Repository  # inverted dependency inversion.

    def store_data(self, data: Any) -> str:
        return self.__repository.insert(data)

    def remove_data(self, data: Any) -> str:
        return self.__repository.delete(data)
