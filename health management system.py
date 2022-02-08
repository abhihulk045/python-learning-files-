import datetime
def gettime():
    return datetime.datetime.now()
def take(k):
    if k==1:
        c=int(input("enter 1 for exercise and 2 for diet"))
        if (c==1):
            action=input("\n")
            with open("harry-ex.txt","a") as f:
                f.write(str([str(gettime())]) + ":" + action + "\n")
                print("successfully written")
        elif (c==2):
            action=input("\n")
            with open("harry-diet.txt","a") as f:
                f.write(str([str(gettime())])+ ":" + action+"\n")
                print("successfully written")

    if k==2:
        c=int(input("enter 1 for exercise and 2 for diet"))
        if (c==1):
            action=input("\n")
            with open("rohan-ex.txt","a") as f:
                f.write(str([str(gettime())]) + ":" + action + "\n")
                print("successfully written")
        elif (c==2):
            action=input("\n")
            with open("rohan-diet.txt","a") as f:
                f.write(str([str(gettime())])+ ":" + action+"\n")
                print("successfully written")

    if k==3:
        c=int(input("enter 1 for exercise and 2 for diet"))
        if (c==1):
            action=input("\n")
            with open("hammad-ex.txt","a") as f:
                f.write(str([str(gettime())]) + ":" + action + "\n")
                print("successfully written")
        elif (c==2):
            action=input("\n")
            with open("hammad-diet.txt","a") as f:
                f.write(str([str(gettime())])+ ":" + action+"\n")
                print("successfully written")

        else:
            print("give valid input (1=harry , 2=rohan , 3=hammad")

def retrieve(k):
    if k==1:
        c = int(input("enter 1 for exercise and 2 for diet"))
        if (c==1):
            with open("harry-ex.txt") as f:
                for i in f:
                    print(i,end="")
        elif (c==2):
            with open("harry-food.txt") as f:
                for i in f:
                    print(i,end="")
    elif k==2:
        c = int(input("enter 1 for exercise and 2 for diet"))
        if (c==1):
            with open("rohan-ex.txt") as f:
                for i in f:
                    print(i,end="")
        elif (c==2):
            with open("rohan-food.txt") as f:
                for i in f:
                    print(i,end="")
    elif k==3:
        c = int(input("enter 1 for exercise and 2 for diet"))
        if (c==1):
            with open("hammad-ex.txt") as f:
                for i in f:
                    print(i,end="")
        elif (c==2):
            with open("hammad-food.txt") as f:
                for i in f:
                    print(i,end="")

    else:
        print("give valid input (1=harry , 2=rohan , 3=hammad")

print("healt management system")

a=int(input("1 for log 2 for retrieve"))

if a==1:
    b=int(input("press 1 for harry 2 for rohan 3 for hammad"))
    take(b)
else:
    b=int(input("press 1 for harry 2 for rohan 3 for hammad"))
    retrieve(b)

