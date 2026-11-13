class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def print(self):
        print("Име:", self.name)
        print("Длъжност:", self.position)
        print("Заплата:", self.salary, "лв.")


class Manager(Employee):
    def __init__(self, name, position, salary, department):
        super().__init__(name, position, salary)
        self.department = department

    def print(self):
        super().print()
        print("Отдел:", self.department)


m1 = Manager("Иван", "Мениджър", 4000, "ИТ отдел")
m2 = Manager("Мария", "Мениджър", 3500, "Маркетинг")

m1.print()
print()
m2.print()