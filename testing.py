# test execution time (example)
import timeit
import numpy as np

setup = """
from operator import add
import numpy as np
a = [1 , 2, 3]
c = np.ones((10, 10))
d = np.zeros((10, 10))
"""

test1 = """
(c == d).all()
"""
test2 = """
np.array_equal(c, d)
"""
test3 = """
[i + j for i, j in zip(a, b)]
"""
test4 = """
np.array(a) + np.array(b)
"""
a = np.array([1, 3, 3])
b = np.array([4, 5, 6])
c = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 2, 1, 0]])
d = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 2, 3, 0]])
print(a - b)
print((c == d).all())
print(np.array_equal(c, d))
print(np.array([1,2,3,'R']).dtype)

print(min(timeit.repeat(stmt=test1, setup=setup, repeat=20, number=10000)))
print(min(timeit.repeat(stmt=test2, setup=setup, repeat=20, number=10000)))
# print(min(timeit.repeat(stmt=test3, setup=setup, repeat=20, number=10000)))
# print(min(timeit.repeat(stmt=test4, setup=setup, repeat=20, number=10000)))
