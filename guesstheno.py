n=10
print("game started")
nog=1
print("u have 5 guesses")

while (nog<=5) :
    userno = int(input())


    if userno<10:
        print("guess bigger no.")
    elif userno>10:
        print("guess smaller no.")
    else:
        print("u won congrats")
        print(nog,"u took in total to win the game")
        break
    print(5-nog,"guesses left now")
    nog = nog + 1

if nog>5:
    print("game over")



