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
