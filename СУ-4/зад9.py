class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sound(self):
        print("Животното издава звук.")


class Dog(Animal):
    def sound(self):
        print(self.name, "казва: Бау-бау!")


class Cat(Animal):
    def sound(self):
        print(self.name, "казва: Мяу-мяу!")


dog1 = Dog("Рекс", 3)
dog2 = Dog("Макс", 5)

cat1 = Cat("Мици", 2)
cat2 = Cat("Пухи", 4)

dog1.sound()
dog2.sound()

cat1.sound()
cat2.sound()