from modules import Person
from modules import House

# https://www.youtube.com/watch?v=OXu-Q2NoS-Y&list=PLAgbpJQADBGLo24x_xBwGtTDO-bjwrFb_&index=12
# Orientação a Objetos em Python — Associação Bilateral
# Instantiate objects.

joanas_house = House()
pedros_house = House('September 7th Street')
joana = Person('Joana')
pedro = Person('Pedro')

# Check your atributes.
print(joanas_house)
print(pedros_house)
print(joana)
print(pedro)
print()


# For both classes understand the association, set owner and house in both through method setters (by @property):
joana.local = joanas_house
pedro.local = pedros_house
joanas_house.owner = joana
pedros_house.owner = pedro
# joanas_house.owner = 'joana' # raise TypeError
# Check your new atributes.
print(joanas_house)
print(pedros_house)
print(joana)
print(pedro)
print()
# testing methods:
print(joana.present_yourself())
print(joana.present_local())
print(joana.enter_the_place(joanas_house))
print()
print(pedro.present_yourself())
# Pedro can"t turn on lights on Joanas house:
print(pedro.enter_the_place(joanas_house))  # Another person can"t turn on lights a house that is not yours.
print(pedro.enter_the_place(pedros_house))  # correct operation.
print(pedros_house.turn_on_lights())  # Owner can turn lights of your own home.
