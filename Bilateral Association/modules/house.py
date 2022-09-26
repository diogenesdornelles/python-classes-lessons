from dataclasses import dataclass, field
from .find_errors import ValidateInput


# Bilateral association: classes knows another and vice versa.
# Note that aren't dependence injection. One class are not inserted as atribute another.


@dataclass
class House:
    __address: str = field(default='Vitoria Street')
    __owner: any = field(default=None)  # This atribute will set in the future with person obj.

    @property
    def address(self):
        return self.__address

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, person: any):
        if ValidateInput.type_person('person', person):
            self.__owner = person.name

    def turn_on_lights(self, lighter: str = None):
        if self.__owner == lighter or lighter is None:
            return f'{self.__owner} turn the lights on.'
        else:
            return f'{lighter} isn"t the owner! Its {self.__owner}!'
