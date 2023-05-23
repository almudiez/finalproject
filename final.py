from random import randint

t = ["Rock", "Paper", "Scissors"]

machine = t[randint(0,2)]

player = False

while player == False:

    player = input("Rock, Paper, Scissors?")
    if player == machine:
        print("No winner")
    elif player == "Rock":
        if machine == "Paper":
            print("You lose!", machine, "covers", player)
        else:
            print("You win!", player, "smashes", machine)
    elif player == "Paper":
        if machine == "Scissors":
            print("You lose!", machine, "cut", player)
        else:
            print("You win!", player, "covers", machine)
    elif player == "Scissors":
        if machine == "Rock":
            print("You lose...", machine, "smashes", player)
        else:
            print("You win!", player, "cut", machine)
    else:
        print("I did not understand you, please check your spelling!")

    player = False
    machine = t[randint(0,2)]