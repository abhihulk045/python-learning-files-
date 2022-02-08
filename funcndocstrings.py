#a=10
#b=5
#c=sum((a,b)) #built in function
#print(c)

def function1(a,b):
    print("hello u r in function1",a+b)

def func2(a,b):
    """this is fuction which carries out average for the two numbers"""
    average = (a+b)/2
    #print(average)
    return average

v=func2(5,7)
print(v)
print(func2.__doc__)




