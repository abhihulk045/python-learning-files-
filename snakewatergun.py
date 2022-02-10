import random
lst= ['s','w','g']

chance = 10
no_of_chance = 0
computer_point = 0
human_point = 0

print("Game - Snake, Water, Gun")
print(" s for snake \n w for water \n g for gun")
print("GAME STARTED")

#making game is while loop

while no_of_chance < chance:
    print("Enter your choice as 's', 'w', 'g'")
    _input = input('snake, water, gun')
    _random = random.choice(lst)

    if _input == _random:
        print("Tie - 0 point to each")

    #if user enter s
    elif _input == "s" and _random == "g":
        computer_point = computer_point + 1
        print(f"ur choice is {_input} and computer choice is {_random} \n")
        print("computer wins 1 point \n")
        print(f"ur points are {human_point} and computer points are {computer_point} \n")

    elif _input == "s" and _random == "w":
        human_point = human_point + 1
        print(f"ur choice is {_input} and computer choice is {_random} \n")
        print("human wins 1 point \n")
        print(f"ur points are {human_point} and computer points are {computer_point} \n")

    elif _input == "w" and _random == "s":
        computer_point = computer_point + 1
        print(f"ur choice is {_input} and computer choice is {_random} \n")
        print("computer wins 1 point \n")
        print(f"ur points are {human_point} and computer points are {computer_point} \n")

    elif _input == "w" and _random == "g":
        human_point = human_point + 1
        print(f"ur choice is {_input} and computer choice is {_random} \n")
        print("human wins 1 point \n")
        print(f"ur points are {human_point} and computer points are {computer_point} \n")

    elif _input == "g" and _random == "s":
        human_point = human_point + 1
        print(f"ur choice is {_input} and computer choice is {_random} \n")
        print("human wins 1 point \n")
        print(f"ur points are {human_point} and computer points are {computer_point} \n")

    elif _input == "g" and _random == "w":
        computer_point = computer_point + 1
        print(f"ur choice is {_input} and computer choice is {_random} \n")
        print("computer wins 1 point \n")
        print(f"ur points are {human_point} and computer points are {computer_point} \n")

    else:
        print("Please give valid input 's','w','g'")

no_of_chance = no_of_chance + 1
print(f"{chance-no_of_chance} is left out of {chance} \n")

print("GAME OVER")

if computer_point == human_point:
    print("TIE")

elif computer_point < human_point:
    print("YOU WON")

else:
    print("COMPUTER WON")

print(f"your points are {human_point} and computer points are {computer_point}")



