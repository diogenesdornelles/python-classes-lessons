# https://www.youtube.com/watch?v=CM-JPix8hcI&list=PLAgbpJQADBGLo24x_xBwGtTDO-bjwrFb_&index=5
# Orientação a Objetos em Python - SOLID (S) - Responsabilidade Única
# https://medium.com/xp-inc/os-princ%C3%ADpios-do-solid-srp-princ%C3%ADpio-da-responsabilidade-%C3%BAnica-7897c55694fe
# SRP single-responsibility principle:
# Each module or class must have responsibility for a single part of the functionality provided by the software.

class RegistrationSystem:
    def register(self, name: str, age: int) -> None:
        if self.__check_data(name, age):
            self.__store_user(name, age)
        else:
            self.__show_error()

    @classmethod
    def __check_data(cls, name: str, age: int) -> bool:
        if isinstance(name, str) and isinstance(age, int) and age >= 0:
            return True
        else:
            return False

    @classmethod
    def __store_user(cls, name: str, age: int):
        print('Accessing data bank...')
        print(f'Storing user "{name}", age {age}.')

    @classmethod
    def __show_error(cls):
        print('Invalid data')


person = RegistrationSystem()
person.register('Didi', 37)
