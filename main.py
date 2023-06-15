"""
In some cases, when you’re defining a function, you may not know beforehand
how many arguments you’ll want it to take. Suppose, for example, that you want
to write a Python function that computes the average of several values.
Python provides a way to pass a function a variable number of arguments 
with argument tuple packing and unpacking using the asterisk (*) operator
"""


def average(*args):
    return sum(args) / len(args)


print(average(1, 2, 3))

"""
Python has a similar operator, the double asterisk (**), which can be used
with Python function parameters and arguments to specify dictionary packing
and unpacking.
"""


def studentNumber(**kwargs):
    for key, val in kwargs.items():
        print(f"{key} -> {val}")


studentNumber(Ali="001", Hasan="002")

A0 = dict(zip(("a", "b", "c", "d", "e"), ("1", "2", "3", "4", "5")))
"Output will be a dictionary which a,b,c,d,e are keys and 1,2,3,4,5 are values"
A1 = range(10)
"Output wiil be a rang object that represents a sequence of numbers from 0 to 9"
A2 = [i for i in A1 if i in A0]
"Output will be empty a empty list, A0 keys are not in 0-to-9 sequence"
A3 = sorted(A0[i] for i in A0)
print(A3)
"Output will be a list that contains keys of A0 dictionary in ascending order"
A4 = [[i, i * i] for i in A1]
"""
Output will be list of lists, each inner list has 2 itmes like this :
[[0,0], [1,1], [2,4], ... [9,81]] the second items are the square of the first one
"""

All_items = dict(zip(("A0", "A1", "A2", "A3", "A4"), (A0, A1, A2, A3, A4)))

for key, val in All_items.items():
    print(f"{key} : {val}")

import math
import random


def IsInCircule(x, y):
    r = 0.5
    if (x - r) ** 2 + (y - r) ** 2 <= r**2:
        return True
    return False


def CalculatePi(n):
    num = [IsInCircule(random.random(), random.random()) for _ in range(n)]
    return 4 * num.count(True) / num.__len__()


def Find():
    n = 1
    while True:
        pi = CalculatePi(n)
        n += 1
        diff = abs(pi - math.pi)
        if diff / math.pi < 0.01:
            print(f"approximate pi : {pi:0.3f}")
            print(f"real pi : {math.pi:0.3f}")
            print(f"minimum number of points : {n}")
            break
    return n


Find()

from math import pi, cos, fabs


class CGaussSolver:
    def __init__(self, pf, a, b, n):
        self.m_Pf = pf
        self.m_A = a
        self.m_B = b
        self.m_N = n

    def Legendre(self, m_N, x):
        if m_N == 0:
            return 1
        elif m_N == 1:
            return x
        else:
            return ((2 * m_N - 1) / m_N) * x * self.Legendre(m_N - 1, x) - (
                (m_N - 1) / m_N
            ) * self.Legendre(m_N - 2, x)

    def DLegendre(self, m_N, x):
        return (m_N / (x * x - 1)) * (
            x * self.Legendre(m_N, x) - self.Legendre(m_N - 1, x)
        )


Input = list(map(int, input().split()))
Output = list()
for i in enumerate(Input):
    if i[0] % 6 == 5 and i[1] % 6 == 0:
        Output.append(i[1])
Output.sort()
print(*Output)

print(
    *sorted(
        [
            i[1]
            for i in enumerate(list(map(int, input().split())))
            if i[0] % 6 == 5 and i[1] % 6 == 0
        ]
    )
)
