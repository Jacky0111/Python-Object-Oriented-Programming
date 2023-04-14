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