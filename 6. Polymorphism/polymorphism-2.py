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
