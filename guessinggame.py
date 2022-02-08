n=10
print("game started")
nog=1
print("u have 5 guesses")

while (nog<=9):
    userno = int(input())
    if userno<10:
        print("guess the bigger no.")
    elif userno>10:
        print("guess the smaller no.")
    else:
        print("u won ")
        print(nog,"u took to win")
        break
    print(9-nog,"guesses left")
    nog = nog + 1

if (nog>9):
    print("game over")