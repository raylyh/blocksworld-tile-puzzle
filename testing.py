# test execution time (example)
import timeit
import numpy as np

setup = """
from operator import add
import numpy as np
a = [1 , 2, 3]
c = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0], [0, 2, 0, 3], [0, 2, 0, 3], [0, 2, 0, 3], [0, 2, 0, 3], [0, 2, 0, 3], [0, 2, 0, 3], [0, 2, 0, 3], [0, 2, 0, 3], [0, 2, 0, 3], [0, 2, 0, 3], [0, 2, 0, 3]])
"""

test1 = """
x1, y1 = np.where((c == 1) | (c == 2) |(c == 3))
"""
test2 = """
x1, y1 = np.where((c == 1))
x2, y2 = np.where((c == 2))
x3, y3 = np.where((c == 3))
"""
test3 = """
[i + j for i, j in zip(a, b)]
"""
test4 = """
np.array(a) + np.array(b)
"""
a = np.array([1, 3, 3])
b = np.array([4, 5, 6])
c = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0], [0, 2, 0, 3]])
d = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 2, 3, 0]])
print(a - b)
print((c == d).all())
print(np.array_equal(c, d))
print(np.array([1,2,3,'R']).dtype)


x1, y1 = np.where(c == 1)
x2, y2 = np.where(d == 1)

print(x1)
print(y1)
print(x2)
print(y2)
print(abs(sum(x1-x2)))

print(min(timeit.repeat(stmt=test1, setup=setup, repeat=20, number=10000)))
print(min(timeit.repeat(stmt=test2, setup=setup, repeat=20, number=10000)))
# print(min(timeit.repeat(stmt=test3, setup=setup, repeat=20, number=10000)))
# print(min(timeit.repeat(stmt=test4, setup=setup, repeat=20, number=10000)))
