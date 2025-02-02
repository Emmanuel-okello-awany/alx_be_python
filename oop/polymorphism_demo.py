import math

# Base class Shape
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Derived class Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width  # Rectangle area formula

# Derived class Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)  # Circle area formula using pi

