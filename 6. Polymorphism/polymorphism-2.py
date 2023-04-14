"""
The code defines three classes, Triangle, Rectangle, and Circle, that inherit from the Shape class, which contains
an abstract method. Each subclass implements the area method based on their specific shape. The code creates
instances of the subclasses, stores them in a list, and iterates through the list, calling the area method of each
instance and printing the name of the shape and its area. The code is well-written and uses inheritance to define
different shapes with their respective area calculation methods, but it could benefit from error handling for
negative input values or invalid shapes.
"""


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("triangle")
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)


shapes = [Triangle(4, 6), Rectangle(3, 5), Circle(2)]

for shape in shapes:
    print(f"The area of the {shape.name} is {shape.area()}.")

'''
Output
------
The area of the triangle is 12.0.
The area of the rectangle is 15.
The area of the circle is 12.56.
'''
