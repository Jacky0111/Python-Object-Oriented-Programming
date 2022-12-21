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
