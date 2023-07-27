from modules import Person
from modules import House

# In object-oriented programming, the term "bilateral association" typically refers to an association between two classes where both classes have a relationship with each other. 
# This means that both classes are aware of each other and can interact directly.
# There are two common types of bilateral associations:
# One-to-One Bilateral Association: In this type of association, each instance of one class is associated with exactly one instance of another class, and vice versa. 
# For example, consider two classes: Person and Passport. Each person can have only one passport, and each passport belongs to only one person. So, there's a one-to-one bilateral association between Person and Passport.
# One-to-Many Bilateral Association: In this type of association, each instance of one class is associated with multiple instances of another class, and vice versa. 
# For example, consider two classes: Department and Employee. A department can have many employees working for it, and each employee works in a single department. 
# So, there's a one-to-many bilateral association between Department and Employee.
# Bilateral associations can be established using instance variables, where one class holds a reference to the other class, or through method parameters and return values that allow communication between the classes.
# It's important to design and manage bilateral associations carefully, as they can introduce tighter coupling between classes, and changes in one class may impact the other class. 
# In some cases, it might be more appropriate to use unidirectional associations or event-based communication to reduce coupling and improve code maintainability.

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
