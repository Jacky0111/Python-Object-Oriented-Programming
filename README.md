# Python-Object-Oriented-Programming

0. [Introduction to OOP](https://github.com/Jacky0111/Python-Object-Oriented-Programming#0-introduction-to-oop)
1. [Class](https://github.com/Jacky0111/Python-Object-Oriented-Programming#1-class)
2. [Method](https://github.com/Jacky0111/Python-Object-Oriented-Programming#2-method)
3. [Constructor (__init__)](https://github.com/Jacky0111/Python-Object-Oriented-Programming#3-constructor-(__init__))
4. [Inheritance](https://github.com/Jacky0111/Python-Object-Oriented-Programming#4-inheritance)
5. [Encapsulation](https://github.com/Jacky0111/Python-Object-Oriented-Programming#5-encapsulation)
6. [Polymorphism](https://github.com/Jacky0111/Python-Object-Oriented-Programming#6-polymorphism)

## 0 Introduction to OOP
### 0.1 What is OOP?
<p align="justify">
The concept of object-oriented programming (OOP) is primarily intended for large-scale and complex software. OOP makes a programme more extendable and readable, thereby reducing programming to the level of building blocks. Secondly, OOP encapsulates data and methods related to operating data into objects, as well as the way of organizing code and data is closer to human thinking, thus greatly enhancing the efficiency of programming. Python fully adopts the concept of object-oriented which is a real OOP language. Subsequently, completely supports object-oriented fundamental features, such as inheritance, polymorphism, encapsulation, etc.
</p>

### 0.2 Difference between Procedure-Oriented and Object-Oriented
| Procedure-Oriented                                                  | Differences  | Object-Oriented                                           |
|---------------------------------------------------------------------|:------------:|-----------------------------------------------------------|
| Divides into methods                                                |   Division   | Divides into classes and objects                          |
| Appropriate for simple program                                      | Application  | Appropriate for complex program                           |
| Does not allow overloading                                          | Overloading  | Allows operator overloading and function overloading      |
| Data is not hidden and can be passed globally from method to method | Data Hiding  | Data is hidden and cannot be accessed by external methods |
| Difficult to add new data and method                                |  Expansion   | Easy to add new data and method.                          |
| Algorithm                                                           | Dealing with | Data                                                      |
| Less secure                                                         |   Security   | More secure                                               |
| Top-down                                                            |   Approach   | Bottom-up                                                 |
| Low                                                                 | Productivity | High                                                      |

### 0.3 Evolution of OOP
<p align="justify">
With the evolution of programming language, it has become more and more sophisticated in order to resolve real-life issue. "Array" has been defined along with the expansion of data. Following by the complexity of data type, "Structure" has been defined for complicated data type maintenance. Subsequently, "Object" has been defined for handling huge project in real-life where it helps in enhancing logic of data processing and making it more manageable.
</p>

1. **Simple Data** - Refers to numbers, alphabets at the beginning phase.
* 4, 50, 2.43, 11
2. **Array** - Refers to group data of the same data type.
* Integer array: [10, 20, 30]
* Floating point array: [40.7, 123.45, 3.14157]
* String array: ['a', 'bc', 'def', 'Hello']
3. **Structure** - Combination of several data types.
* Example from C language:
```
struct Employee
{
	char emp_id[4];
	char name[20];
	int age;
	double salary
	char department[15];
};
```
4. **Object** - Combination of several data types and several methods:
* Example from Python language:
```
class Employee:
    emp_id = 'A123'     # Class Attribute
    age = 0         
    salary = 0      
    
    def __init__(self, emp_id, age, salary):
        self.emp_id = emp_id    # Instance Attribute
        self.age = age
        self.salary = salary
        
    def employeeInfo(self):  # Instance Method
        print('Employee ID: ' + self.emp_id)
        print('Age: ' + self.age)
        print('Salary: ' + self.salary)
```

## 1 Class
### 1.1 What is Class?
A class in object-oriented programming is a blueprint or a template for creating objects that have similar attributes and behaviors. It is a fundamental concept in object-oriented programming that allows you to define your own data type.

In Python, you can define a class using the class keyword followed by the name of the class. Here's an example:
```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is", self.name, "and I am", self.age, "years old.")
```
In the above example, we have defined a class named Person that has two attributes, name and age, and a method greet() that prints out a greeting message. 

Once a class has been defined, you can create objects or instances of that class by calling the class constructor. Here's an example:

```
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

person1.greet() # Output: Hello, my name is Alice and I am 25 years old.
person2.greet() # Output: Hello, my name is Bob and I am 30 years old.
```

## 2 Method
### 2.1 What is Method?
In Python, a method is a function that belongs to an object. It is defined within the class and can be called on an instance of the class. The first argument of the method is usually self, which refers to the instance of the class that is calling the method. Here is an example:

```
class myClass():
    def method1(self):
        print('This is method 1")
        
    def method2(self):
        print('This is method 2")
```

In this example, `method1` and `method2` are methods of the `myClass` class.

### 2.2 Class Method

A class method is a method that is bound to the class and not the instance of the class. It takes the class as its first argument, usually named cls, instead of self. It can be defined using the `@classmethod` decorator. Here is an example:

```
@classmethod
def method1(cls, age):
    print('This is method 1 and the age is', age)
```

In this example, `method1` is a static method of the `myClass` class that takes an argument `age`.

### 2.3 Static Method
```
@staticmethod
def method2(age):
    print('This is method 2 and the age is', age)
```

In this example, `method2` is a static method of the `myClass` class that takes an argument `age`.

## 3 Constructor (`__init__`)

The `__init__` method is a special method in Python classes that is called when an object is created from the class and it initializes the object's attributes. The `__init__` method has a `self` parameter which refers to the object being created and allows the object to access its own attributes and methods. Here is an example of a class with an `__init__` method:

```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
```

In the example above, the `__init__` method takes two arguments, `name` and `age`, which are used to initialize the `name` and `age` attributes of the `Person` object. The `greet` method can be called on a `Person` object to print a greeting message that includes the `name` and `age` attributes of the object.

## 4 Inheritance

Inheritance is a way to create a new class that is a modified version of an existing class. The new class is called a **subclass** or **derived class**, and the original class is called the **superclass** or **base class**. The subclass inherits all the attributes and methods of the superclass, and can also add its own attributes and methods.

```
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")
```

In this example, `Dog` is a subclass of `Animal`. It inherits the `__init__` method from `Animal`, which initializes the `name` attribute. It also inherits the `eat` method, which prints that the animal is eating. However, it adds its own method, `bark`, which prints that the dog is barking.

## 5 Encapsulation

Encapsulation is the idea of bundling data and methods that operate on that data within a single unit, called a **class**. The data is hidden from the outside world and can only be accessed through methods that are defined in the class. This helps to ensure that the data is used correctly and consistently.

```
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")
    
    def get_balance(self):
        return self.__balance
```

In this example, `BankAccount` is a class that encapsulates the data of a bank account. The `balance` attribute is marked as private by adding two underscores before the name. This means that it can only be accessed from within the class, and not from outside. The `deposit`, `withdraw`, and `get_balance` methods are defined to operate on the `balance` attribute. They are the only way to modify or access the `balance` attribute, ensuring that it is used correctly and consistently.

## 6 Polymorphism
Polymorphism is the ability of an object to take on many forms. In Python, this is often implemented through "duck typing", where the type of an object is determined by the methods it has, rather than its class or type. This allows different objects to be used interchangeably in code, as long as they have the same methods.

```
class Cat:
    def sound(self):
        print("Meow")
    
class Dog:
    def sound(self):
        print("Woof")

def make_sound(animal):
    animal.sound()

cat = Cat()
dog = Dog()

make_sound(cat)  # Output: "Meow"
make_sound(dog)  # Output: "Woof"
```

In this example, `Cat` and `Dog` are two different classes with the same method name, `sound`. The `make_sound` function takes an object as an argument and calls its `sound` method. It doesn't matter whether the object is a `Cat` or a `Dog` – as long as it has a `sound` method, it can be passed to the function. This is an example of polymorphism, where different objects can be used interchangeably as long as they have the same methods.

