#Recursions - implementing functions into functions
# def print2(str1):
#     print2(str1)
#     print("This is "+str1)
# print2("Abhi")



# n! = n * n-1 * n-2 * n-3 * n-4 * ........ 1
# n! = n * (n-1)!

# def factorial_iterative(n):
#     """
#     :param n:Integer
#     :return:n * n-1 * n-2 * n-3 * n-4 * ........ 1
#     """
#     fac = 1
#     for i in range(n):
#         fac = fac * (i+1)
#     return fac
#
# def factorial_recursive(n):
#     """
#     :param n:Integer
#     :return:n * n-1 * n-2 * n-3 * n-4 * ........ 1
#     """
#     if n==1:
#         return 1
#     else:
#         return n * factorial_recursive(n-1)
# number = int (input("Enter the number"))
# print("factorial using iterative method 1 by 1",factorial_iterative(number))
# print("factorial using recursive method",factorial_recursive(number))

def fibbonaci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibbonaci(n-1)+fibbonaci(n-2)
number = int (input("enter ur number"))
print(fibbonaci(number))