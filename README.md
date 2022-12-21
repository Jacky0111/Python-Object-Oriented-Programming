# Python-Object-Oriented-Programming

0. [Introduction to OOP](https://github.com/Jacky0111/Python-Object-Oriented-Programming#0-introduction-to-oop)
1. [Class](https://github.com/Jacky0111/Python-Object-Oriented-Programming#1-class)
2. [Method](https://github.com/Jacky0111/Python-Object-Oriented-Programming#2-method)
3. [Constructor (__init)](https://github.com/Jacky0111/Python-Object-Oriented-Programming#3-onstructor-(__init))
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

## 2 Method
### 2.1 What is Method?
### Difference between Class and Method

## 3 Constructor (__init)

## 4 Inheritance

## 5 Encapsulation

## 6 Polymorphism

