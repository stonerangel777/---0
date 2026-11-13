class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


r1 = Rectangle(5, 4)
r2 = Rectangle(6, 3)

c1 = Circle(3)
c2 = Circle(5)

print("Лице на правоъгълник 1:", r1.area())
print("Лице на правоъгълник 2:", r2.area())

print("Лице на кръг 1:", c1.area())
print("Лице на кръг 2:", c2.area())