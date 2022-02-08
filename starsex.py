a=int(input("add no. of line u want to print"))
b=bool(int(input("if 1 true 'ascending order' and if 0 false 'descending order'")))
def star(a,b):
    if b==True:
        c=1
        while c<=a:
            print(c*"*")
            c=c+1

    else:
        while a>0:
            print(a*"*")
            a=a-1

star(a,b)