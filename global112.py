l=10 #global variable can be used by program anywhere and global variable cannot be changed by global keyword we can cahnge but in defined function
def function1(n):
    m=6 #local variable only usable in defined function
    a=5 ##local variable only usable in defined function
    # global l #gave permission to cahnge global variable value
    # l=456
    print(l,m,a)
    print(n,"I have printed this")
function1("This is me")
#print(l)


