import random

player = int(input("What do you chose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))
print("")
if player >= 3 and player < 0:
    print("Enter a Valid input.")
else:
    cpu = random.randint(0,2)
    choices = ["Rock!", "Paper!", "Scissors!"]

    print("Player goes :"+ choices[player]+"\n")
    print("Computer goes :"+ choices[cpu]+"\n")

    if cpu == 0 and player == 1:
        print("You win!")
    elif cpu == 1 and player == 2:
        print("You win!")
    elif cpu == 2 and player == 0:
        print("You win!")
    elif cpu == int(player):
        print("Tie!")
