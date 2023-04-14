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