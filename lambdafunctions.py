# Lmambda functions or anonymous functions
# def add(a,b):
#     return a+b
# minus=lambda x, y: x-y #lambda is 1liner function
# print(minus(9,4))
# def a_first(a):
#     return a[1] no need to write this when we use LAMBDA function now see belwo
a = [[1,14],[5,6],[8,23]]
a.sort(key=lambda x:x[1])
print(a)
