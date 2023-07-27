from shopp_models import ShoppingCart
from shopp_models.goods import Good

# CHATGPT
# Aggregation is an association relationship between two classes in object-oriented programming, where one class represents a whole object (the container) and contains or is composed of other objects 
# (the components or parts). The relationship implies that the container class has a "has-a" relationship with the component class. Aggregation is a weaker form of association compared to composition, 
# as it allows the component objects to exist independently outside the container.
# In aggregation, the lifecycle of the component objects is not necessarily tied to the lifecycle of the container. If the container is destroyed, 
# the component objects can still exist and be associated with other containers. This characteristic differentiates aggregation from composition, 
# where the component objects are exclusively part of the container's lifecycle and cannot exist independently.
# In UML (Unified Modeling Language), aggregation is often represented by a diamond-shaped arrowhead on the side of the container class pointing towards the component class.

# https://www.youtube.com/watch?v=-vEke_Ssils&list=PLAgbpJQADBGLo24x_xBwGtTDO-bjwrFb_&index=21
# Orientação a Objetos em Python — Agregação de Classes

# Add objects from another class to a class. Ordinary, a list is an attribute of class that are aggregate other.

banana = Good('banana', 5, 3)
mamao = Good('papaya', 10, 2)
apple = Good('apple', 4, 3)

basket = ShoppingCart()

basket.add(banana)
basket.add(mamao)
basket.add(apple)

basket.remove(banana)

print(basket.finalize())
