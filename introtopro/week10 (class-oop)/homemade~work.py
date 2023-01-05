#1
def ex1():
    import math

    class circlconstr:
        def __init__(self, radiu):
            self.radius = radiu

        def getArea(self):
            return self.radius ** 2 * math.pi

        def getPerimeter(self):
            return self.radius * 2 * math.pi

    circy = circlconstr(4.44)
    circx = circlconstr(11)
    print(circy.getPerimeter())
    print(circx.getPerimeter())


def ex2():
    class Student:
        def __init__(self, name, age, GPA):
            self.name = name
            self.age = age
            self.GPA = GPA

        def set_GPA(self, new_GPA):
            self.GPA = new_GPA

        def set_name(self, new_name):
            self.name = new_name

        def __str__(self):
            return f"Student name:{self.name}, age:{self.age}, GPA:{self.GPA}"

    stud = Student("Jessa", 20, 3.2)
    print(stud)

    stud.set_GPA(2.9)
    print(stud)

    stud.set_name("Jessia")
    print(stud)


class School:
    target = 0.99

    def __init__(self, capital):
        self.budget = capital

    def max_expenditure(self):
        return self.budget * School.target

d
print(School.target)
s = School(100000)
print(s.budget)
print(s.max_expenditure())