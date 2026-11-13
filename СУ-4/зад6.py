class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def print(self):
        print("Марка:", self.brand)
        print("Модел:", self.model)
        print("Година:", self.year)


v1 = Vehicle("BMW", "320d", 2020)
v2 = Vehicle("Audi", "A4", 2022)
v3 = Vehicle("Mercedes", "C-Class", 2021)

v1.print()
print()
v2.print()
print()
v3.print()