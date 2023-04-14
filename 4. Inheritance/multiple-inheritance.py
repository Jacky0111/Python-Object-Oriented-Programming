"""
This code defines a class hierarchy for shapes and colors. The Shape class has a method for computing the area,
while the Color class has an attribute for storing the color. The ColoredShape class is a combination of Shape and
Color, and has a method for describing the shape with its color and area. Finally, the Square class is a specific
type of ColoredShape that computes its area based on its side length.

The code creates a Square instance with side length 5 and color "red", and calls its describe() method to print out
its description, including its area. The output is "This is a red square with an area of 25.
"""


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass


class Color:
    def __init__(self, color):
        self.color = color


class ColoredShape(Shape, Color):
    def __init__(self, name, color):
        Shape.__init__(self, name)
        Color.__init__(self, color)

    def describe(self):
        print(f"This is a {self.color} {self.name} with an area of {self.area()}.")


class Square(ColoredShape):
    def __init__(self, side_length, color):
        super().__init__("square", color)
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2


square = Square(5, "red")
square.describe()

'''
Output
------
This is a red square with an area of 25.
'''
