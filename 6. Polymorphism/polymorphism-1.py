"""
The code defines a Fruit class with an abstract method eat and two subclasses, Apple and Banana, which implement
their own eating behavior. It also defines a function eat_fruit that takes a fruit object and calls its eat method.
The code creates instances of the Apple and Banana classes and passes them as arguments to the eat_fruit function,
which calls their respective eat methods and prints their eating behavior.

Overall, the code demonstrates the use of inheritance and polymorphism to define a general class with specific
behavior for its subclasses. However, the code could be improved by adding error handling for invalid input values.
"""


class Fruit:
    def __init__(self, name):
        self.name = name

    def eat(self):
        pass


class Apple(Fruit):
    def eat(self):
        return "Crunch!"


class Banana(Fruit):
    def eat(self):
        return "Peel and eat!"


def eat_fruit(fruit):
    print(fruit.eat())


apple = Apple("Honeycrisp")
banana = Banana("Cavendish")

eat_fruit(apple)
eat_fruit(banana)

'''
Output
------
Crunch!
Peel and eat!
'''
