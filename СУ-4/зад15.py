class Person:
    def __init__(self, name, family, age, nationality):
        self.name = name
        self.family = family
        self.age = age
        self.nationality = nationality

    def print(self):
        print("Име:", self.name)
        print("Фамилия:", self.family)
        print("Възраст:", self.age)
        print("Националност:", self.nationality)


class Student(Person):
    def __init__(self, name, family, age, nationality,
                 university, yearofstudy):
        super().__init__(name, family, age, nationality)
        self.university = university
        self.yearofstudy = yearofstudy

    def print(self):
        super().print()
        print("Университет:", self.university)
        print("Година на обучение:", self.yearofstudy)


class Lecturer(Person):
    def __init__(self, name, family, age, nationality,
                 university, experience):
        super().__init__(name, family, age, nationality)
        self.university = university
        self.experience = experience

    def print(self):
        super().print()
        print("Университет:", self.university)
        print("Преподавателски стаж:", self.experience, "години")


# Създаване на обекти
p1 = Person("Иван", "Иванов", 30, "Българин")

s1 = Student("Мария", "Петрова", 20, "Българка",
             "Софийски университет", 2)

s2 = Student("Петър", "Димитров", 22, "Българин",
             "Технически университет", 3)

l1 = Lecturer("Георги", "Георгиев", 45, "Българин",
              "Софийски университет", 20)

l2 = Lecturer("Елена", "Иванова", 40, "Българка",
              "Технически университет", 15)


# Списък с обекти от различни класове
people = [p1, s1, s2, l1, l2]


# Извикване на print() чрез цикъл
for person in people:
    print("----------------------")
    person.print()