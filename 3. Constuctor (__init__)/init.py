"""
The code defines a Counter class with a constructor (init method) that initializes the count variable to zero and
a method (increment) that increments the count variable by 1. The code creates an instance of the Counter class,
increments the count variable twice, and prints the initial and updated values of the count variable. The code is
well-written but could benefit from additional methods and error handling.
"""


class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1


counter = Counter()
print(counter.count)

counter.increment()
counter.increment()
print(counter.count)

'''
Output
------
0
1
'''
