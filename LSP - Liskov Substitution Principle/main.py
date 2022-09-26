from dataclasses import dataclass


# https://www.youtube.com/watch?v=mv45FEbqGlY&list=PLAgbpJQADBGLo24x_xBwGtTDO-bjwrFb_&index=15
# Orientação a Objetos em Python - SOLID (L) - Princípio da Substituição de Liskov

# Simply put, the Liskov Substitution Principle (LSP) states that objects of a superclass should be replaceable with
# objects of its subclasses without breaking the application. In other words, what we want is to have the objects of,
# our subclasses behaving the same way as the objects of our superclass.

# Liskov's notion of a behavioural subtype defines a notion of substitutability for objects; that is, if S is a subtype
# of T, then objects of type T in a program may be replaced with objects of type S without altering any of the
# desirable properties of that program (e.g. correctness).

@dataclass
class PersonA:
    def present_yourself(self):
        print('Hello, Im the person A')


@dataclass
class PersonB(PersonA):
    def present_yourself(self):
        print('Hello, Im the person B! Changed method!')

# breaking the liskov principle, the subclass change method statemented on superclass. That is, they do not behave in
# the same way. The same method should have the same behavior/functionality for both classes.


person_1 = PersonA()  # Hello, I'm the person A
person_1.present_yourself()  # Hello, I'm the person B
person_2 = PersonB()
person_2.present_yourself()


def present():
    print('Hello, Im the person C')


person_1.present_yourself = present
person_1.present_yourself()  # Hello, I'm the person C
person_2.present_yourself()  # Hello, I'm the person ! Changed method! (Again!)
