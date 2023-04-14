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