class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def print(self):
        print("Марка:", self.brand)
        print("Модел:", self.model)
        print("Година:", self.year)


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, engine_capacity):
        super().__init__(brand, model, year)
        self.engine_capacity = engine_capacity

    def print(self):
        super().print()
        print("Кубатура:", self.engine_capacity, "куб. см")


mc1 = Motorcycle("Yamaha", "MT-07", 2022, 689)
mc2 = Motorcycle("Honda", "CBR600RR", 2021, 600)

mc1.print()
print()
mc2.print()