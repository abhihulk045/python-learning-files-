# file IO basics
"""
"r" - open file for reading
"w" - open file for writing
"x" - creates file if not exists
"a" - add more content to file
"t" - text mode
"b" - binary mode
"+" - read and write mode
"""

#question of the day
def func1(a,b):
    """this is how to print docstring"""
    print(func1.__doc__)
    addition = a + b
    return addition
v=func1(2,3)
print(v)
