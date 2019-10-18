# test execution time (example)
import timeit

setup = """
import numpy as np
a = (1,2,3)
b = (4,5,6)
"""

test1 = """
np.subtract(a, b)
"""
test2 = """
(a[0]-b[0], a[1]-b[1], a[2]-b[2])
"""
test3 = """
pass
"""
a = [1, 2, 3]
a += []
print(a)

print(min(timeit.repeat(stmt=test1, setup=setup, repeat=10, number=10000)))
print(min(timeit.repeat(stmt=test2, setup=setup, repeat=10, number=10000)))
print(min(timeit.repeat(stmt=test3, setup=setup, repeat=10, number=10000)))
