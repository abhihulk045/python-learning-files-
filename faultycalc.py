
print("faulty calculator")
print("enter ur 1st number")
num1=int (input())
print("select ur operation")
print("+","-","*","/")
opt=input()
print("enter ur 2nd number")
num2=int (input())
if opt=="+":
 if  num1==56 and num2==4:
    print("77")
 elif num1==4 and num2==56:
    print("77")
 else:
    print (num1+num2)

if opt=="-":
 #if num1-num2:
    print(num1-num2)
 #else:
    #print("u r answer is")

if opt=="*":
 if num1==77 and num2==8:
    print("566")
 elif num1==8 and num2==77:
    print("566")
 else:
    print(num1*num2)

if opt=="/":
 if num1==56 and num2==6:
    print("4")
 else:
     print(num1/num2)
     print("thanku")