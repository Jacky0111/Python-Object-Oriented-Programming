"""
The initial value of score is 100, which is the class attribute. When an instance of the Student class is created
and its score attribute is accessed, the value of the class attribute (100) is returned.

When the setScore method of the instance s is called, it sets the score attribute of that instance to 99, which is an
instance attribute. When the score attribute of s is accessed again, it returns the value of the instance attribute,
which is 99.
"""


class Student:
    score = 100  # Class Attribute

    def setScore(self):
        self.score = 99  # Instance Attribute


s = Student()
print(s.score)

s.setScore()
print(s.score)

'''
Output
------
100
99
'''
