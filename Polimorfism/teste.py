from collections import namedtuple, OrderedDict

########################################################################################################################

# def foo(a, b, /, c, d, *, e, f):
#     #  'a' and 'b' are positional.
#     #  'c' and 'd' are positional or kw_only.
#     #  'e' and 'f' are kw_only
#     return a + b, c + d, e + f
#
#
# result = foo(1, 2, 3, d=4, e=5, f=6)
# print(result)
#

########################################################################################################################
# Accept parameters str | str
# Person = namedtuple('Person', 'name last_name job marital_status')  # Point is an <class '__main__.Person'>
# print(Person)  # Person is an <class '__main__.Person'>
# print(Person.__name__)  # Return namedtuple first parameter 'Person'
# print(Person.job)  # _tuplegetter(1, 'Alias for field number 1')
# print(Person.last_name)  # _tuplegetter(0, 'Alias for field number 1')
#
# person = Person(name='Diógenes', last_name='Dornelles', job='Servidor', marital_status='União estável')
# print(person._asdict())  # convert to dict
########################################################################################################################

# Accept parameters str | list | tuple | set
Point = namedtuple('Point', ['x', 'y', 'z'])
print(Point)
p1 = Point(2, 3, 4)
print(p1)
p2 = Point(5, 6, 7)
print(type(p1))
print(p1.x * p1.y)
# p.x = 3  # Don't accept directly assignment - AttributeError: can't set attribute.
p1._replace(x=2, y=100, z=1000)
print(p1)
print(p1.x * p1.y)


print(p1 + p2)  # return tuple: (2, 3, 4, 5, 6, 7)
print(p1.x + p2.x)  # return 7


########################################################################################################################
# def func() -> tuple:
#     lista_descricao = []
#     nome_produto = input('Informe o nome do produto: ')
#     looping_secundario = True
#     while looping_secundario:
#         descricao = input('Informe a especificação do produto que pretende inserir no sistema: ')
#         lista_descricao.append(descricao)
#         opcao = input('Deseja informar outra especificação (digite enter para não): ')
#         if opcao == '':
#             break
#     return nome_produto, lista_descricao
#
#
# looping_principal = True
# while looping_principal:
#     item, descricoes = func()
#     Product = namedtuple(item, [*descricoes])
#     valores = []
#     for descricao in descricoes:
#         valor = input(f'Informe o valor da especificação {descricao}: ')
#         valores.append(valor)
#     produto = Product(*valores)
#     as_dict = {item: produto._asdict()}
#     print(as_dict)
