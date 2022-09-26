from module import Penguin, Falcon, Chicken, Observer, Observer2, Penguin2, Falcon2, Chicken2

# https://www.youtube.com/watch?v=AjafIJw-OAg&list=PLAgbpJQADBGLo24x_xBwGtTDO-bjwrFb_&index=19
# Orientação a Objetos em Python - SOLID (I) - Princípio da Segregação de Interface

# Interface Segregation Principle ISP

# This principle advises to avoid depending on thing that they don't use.

observer = Observer('Dio')
falcon = Falcon(observer)
penguin = Penguin(observer)
chicken = Chicken(observer)

print(falcon.fly())
print(penguin.eat())
print(chicken.eat())

falcon2 = Falcon2()
penguin2 = Penguin2()
chicken2 = Chicken2()

observer2 = Observer2('Dio')

print(observer2.note_scream(falcon2))
print(observer2.note_fly(penguin2))
print(observer2.note_fly(falcon2))
print(observer2.note_eat(chicken2))
print(observer2.note_scream(chicken2))
print(observer2.note_scream(penguin2))
print(observer2.note_eat(falcon2))
print(observer2.note_eat(penguin2))
