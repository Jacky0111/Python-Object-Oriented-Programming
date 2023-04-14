"""
This program defines a class hierarchy with two classes: Animal and Cat. The Cat class is a subclass of Animal and
overrides the speak method to print the sound a cat makes. An instance of the Cat class is created with the name
"Fluffy" and its speak method is called, resulting in the output "Fluffy meows."
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print(f"{self.name} meows.")


cat = Cat("Fluffy")
cat.speak()

'''
Output
------
Fluffy meows.
'''
