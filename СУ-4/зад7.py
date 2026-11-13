class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def print(self):
        print("Марка:", self.brand)
        print("Модел:", self.model)
        print("Година:", self.year)


class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors

    def print(self):
        super().print()
        print("Брой врати:", self.doors)


c1 = Car("BMW", "320d", 2020, 4)
c2 = Car("Audi", "A3", 2022, 5)

c1.print()
print()
c2.print()