from dataclasses import dataclass, field
from .find_errors import ValidateInput


@dataclass
class Person:
    __name: str
    __local: any = field(default=None)  # This atribute will set in the future with house obj.

    @property
    def name(self) -> str:
        return self.__name

    @property
    def local(self) -> any:
        return self.__local

    @local.setter
    def local(self, local: any) -> None:
        if ValidateInput.type_local('local', local):
            self.__local = local.address

    def enter_the_place(self, local: any) -> None:
        return local.turn_on_lights(self.name)

    def present_yourself(self) -> str:
        return f'Hello! Im {self.__name}!'

    def present_local(self) -> str:
        return f'I live at {self.__local}'
