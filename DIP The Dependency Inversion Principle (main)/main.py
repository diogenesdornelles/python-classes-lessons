from user import User
from user.databases import MySqlRepository, MongoRepository

# https://www.youtube.com/watch?v=OHmTpOD_AdI&list=PLAgbpJQADBGLo24x_xBwGtTDO-bjwrFb_&index=20
# Orientação a Objetos em Python - SOLID (D) - Princípio da Inversão da Dependência

# The Dependency Inversion Principle (DIP) states that high-level modules should not depend on low-level modules; both
# should depend on abstractions. Abstractions should not depend on details. Details should depend upon abstractions.

user1 = User(MySqlRepository())
user2 = User(MongoRepository())
# user3 = User(Repository())  #cant instantiate an object os abstract class.
print(user1.store_data('23'))
print(user1.remove_data('11'))
print(user2.store_data('23'))
print(user2.remove_data('11'))
