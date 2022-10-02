#!/usr/bin/python
class Employee:

    def __init__(self, firstname, lastname, salary, position):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        self.position = position
        self.email = self.firstname + "." + self.lastname + "@gmail.com"

    def give_raise(self, salary):
        self.salary = salary

    def promote(self, position):
        self.position = position


class Developer(Employee):
    def __init__(self, firstname, lastname, salary, position, programming_languages):
        super().__init__(firstname, lastname, salary, position)
        self.pro_langs = programming_languages

    def addLanguage(self, pro_langs):
        self.pro_langs = pro_langs


Employee1 = Employee("John", "Smith", 80000, 'Developer')
print(Employee1.salary)
Employee1.give_raise(10000)
print(Employee1.salary)
Employee1.promote("Project Manager")
print(Employee1.firstname+":"+ Employee1.position)

dev1 = Developer("John", "Montana", 10000, 'Solution Architect', ["Python", "C"])
print(dev1.salary)
dev1.give_raise(12500)
dev1.addLanguage("Java")
dev1.addLanguage("React")
print(dev1.salary)
print(dev1.pro_langs)
print(dev1.firstname+" "+ dev1.lastname+":"+dev1.position)
