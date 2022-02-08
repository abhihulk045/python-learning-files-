print("enter num 1")
num1 = input()
print("enter num 2")
num2 = input()

try:
    print("sum of these num's is", int(num1) + (num2))
except Exception as e:
    print(e)

print("This is important and needed to be print no matter what.")