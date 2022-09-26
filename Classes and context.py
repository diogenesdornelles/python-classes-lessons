# https://www.youtube.com/watch?v=CtSX3dWqWBQ&list=PLAgbpJQADBGLo24x_xBwGtTDO-bjwrFb_&index=2
# Orientação a Objetos em Python — Classes e Contexto

class MyClass:
    def __init__(self, my_atribute=None, my_atribute_2=None) -> None:
        self.my_atribute = my_atribute
        self.my_atribute_2 = my_atribute_2

    def first_method(self) -> None:
        print(f'My atributes: {self.my_atribute} and {self.my_atribute_2}.')

    def second_method(self, arg_1: int, arg_2: int) -> None:
        print(f'{self.my_atribute}: {arg_1 + arg_2}')

    @staticmethod
    def third_method():
        print('I"m in the static method')

    @classmethod
    def forth_method(cls):
        print(cls.__dir__(cls))


print("Method accessible by object, in context 'self' (=obj). It's need instantiate an object to work.")
obj = MyClass()
obj.first_method()
print()
print("Method accessible by class, given object 'obj' (=self) as parameter.")
MyClass.first_method(obj)
print()
print("Method accessible by object, in context 'self' (=obj). It's need instantiate an object to work and give "
      "parameters.")
obj_2 = MyClass('One', 'Two')
obj_2.second_method(1, 2)
print()
print("Staticmethod: Method accessible by own class, but don't need the context it.")
MyClass.third_method()
print()
print("Classmethod: Method accessible by own class, but don't need it.")
MyClass.forth_method()
print()
