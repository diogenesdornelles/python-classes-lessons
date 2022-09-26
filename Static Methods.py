# https://www.youtube.com/watch?v=T63J-vQi044&list=PLAgbpJQADBGLo24x_xBwGtTDO-bjwrFb_&index=7
# Orientação a Objetos em Python — Métodos Estáticos

class Error:

    @staticmethod
    def protocol() -> None:
        print('Protocol error')

    @staticmethod
    def https() -> None:
        print('Https error')

    @staticmethod
    def input() -> None:
        print('Input error')


# Staticmethod doesn't have context defined. Sometimes we don't need to declare an object, just use the class itself.
# It can be conceptualized as a collection of contexts that do not need an object

obj = Error()
obj.protocol()
# OR
Error.input()

