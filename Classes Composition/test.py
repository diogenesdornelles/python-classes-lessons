import os


########################################################################################################################
# ______________________________________________________________________________________________________________________
# - return tuple - #
def foo(*args):  # parameter are packaged in args, in tuple type. So that, args is a tuple.
    a = args
    return a


print(foo(1, 2, 3))  # three parameters literally informed. Return tuple (1, 2, 3)
print()
print('==' * 10)


# ______________________________________________________________________________________________________________________

# - return tuple - #
def foo(*args):  # parameter are packaged in args, in tuple type. So that, args is a tuple.
    a, *b = args  # unpack values in two variables. First receives args[0], while second list with others.
    return a, b  # return tuple (1, [2, 3])


print(foo(1, 2, 3))  # three parameters literally informed. Return tuple (1, 2, 3)
print()
print('==' * 10)


# ______________________________________________________________________________________________________________________
# - return tuple - #
def foo(*args):  # parameter are packaged in args, in tuple type. So that, args is a tuple.
    a = args
    return a


rol = 1, 2, 3
print(foo(rol))  # One parameter as tuple. Return # ((1, 2, 3),).
print()
print('==' * 10)


# ______________________________________________________________________________________________________________________
# - return tuple - #
def foo(*args):
    a = args
    return a


rol = [1, 2, 3], [4, 5, 6]
print(foo(rol))  # One parameter as tuple, this formed by lists. Return (([1, 2, 3], [4, 5, 6]),). Note that last
# element is empty.
print()
print('==' * 10)


# ______________________________________________________________________________________________________________________
# - return tuple - #
def foo(*args):
    a = args
    return a


rol = [1, 2, 3], [4, 5, 6]
print(foo(*rol))  # One parameter as tuple unpacked, so that the parameter are formed, in fact, by two lists.
# Return ([1, 2, 3], [4, 5, 6]).
# Note that last element is not empty, due to unpacked.
########################################################################################################################
print()
# current_dir = os.getcwd()
# go_dir_databases = current_dir + '\methods\databases'
# os.chdir(go_dir_databases)
# path_databases = 'all_databases'
# os.mkdir('all_databases')
# go_dir_all_databases = go_dir_databases + path_databases
# os.chdir(go_dir_all_databases)


########################################################################################################################
print()

b = ['a', 'b', 'c', 'd', 'e']
a = range(len(b) + 1)
a = [f'n. {n}' for n in a]

c = dict(zip(a, b))
print(c)

# dict comprehension
d = {f'{key}{value}': f'{value}{key}' for (key, value) in c.items()}
print(d)

e = 'en. 4' in d.values()  # search by values
print(e)

f = 'n. 4e' in d  # search by keys
print(f)

g = d.get('n. 3d')  # parameter key: return value, else, None.
print(g)

h = d.pop('n. 4e')  # del key and value
print(d)

i = d.popitem()  # remove last key/value and return them as tuple.
print(i)
print(d)


def foo(l1, l2):

    for k, n in zip(l1, l2):
        yield k + n, n + k


l3 = 1
l1 = ['cat', 'dog', 'pig']
l2 = ['1', '2', '3']
l4 = foo(l1, l2)

# print(next(l4))
# print(next(l4))
# print(next(l4))



[print(next(l4)) for n in l2]
[print(f'{pet}') for pet in l1]

# for n in range(len(l1)):
#     j = d.fromkeys(next(l4)[0], next(l4)[0])  # {'cat': ['1', '2', '3'], 'dog': ['1', '2', '3'], 'pig': ['1', '2', '3']}
# print(j)
########################################################################################################################
