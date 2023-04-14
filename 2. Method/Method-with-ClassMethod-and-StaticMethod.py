"""
The code defines a Person class with two attributes and two methods: a constructor (init), a class method
(from_birth_year), and a static method (get_age). The class method creates a new instance of the Person class based on
a birth year input, while the static method calculates the age based on the current year and the birth year input.
The code creates two instances of the Person class and prints their names and ages. The code is well-written and uses
class methods and static methods effectively but could benefit from additional methods and error handling.
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = cls.get_age(birth_year)
        return cls(name, age)

    @staticmethod
    def get_age(birth_year):
        current_year = 2023
        return current_year - birth_year


person1 = Person("Alice", 25)
print(f"{person1.name} is {person1.age} years old")

person2 = Person.from_birth_year("Bob", 1990)
print(f"{person2.name} is {person2.age} years old")

'''
Output
------
Alice is 25 years old
Bob is 33 years old
'''
