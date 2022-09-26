from shopp_models import ShoppingCart
from shopp_models.goods import Good

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
