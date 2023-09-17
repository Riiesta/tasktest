import math

class Shape:
    def area(self):
        pass

    def is_right_triangle(self):
        return False

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = sorted([a, b, c])

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right_triangle(self):
        return math.isclose(self.a ** 2 + self.b ** 2, self.c ** 2)
