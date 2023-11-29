import random
list = [2,5,8,9,12]
print ("random.sample() ",random.sample(list,3))
list = [20, 30, 40, 50 ,60, 70, 80, 90]
print(random.choices(list, k=9))
random.shuffle(list)
print(list)
print("here",random.randint(1,9))
print(random.uniform(1,7))

import numpy
print(numpy.random.normal())
print(numpy.random.normal(size=4))
print(numpy.random.uniform(size=4))
print(numpy.random.randint(low=90, high=100, size=(4,3)))


