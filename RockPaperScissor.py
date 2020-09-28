import random

print("Instructions:")
print("The first Player to touch the score of 5 wins.")
print("Rules:")
print("Rock Beats Scissor!")
print("Scissor Beats Paper!")
print("Paper Beats Rock!")
print("Have Fun! ;)")
print()

def PlayerOption():
    global PlayerChoice
    PlayerChoice=input("Choose one from Rock, Paper or Scissor\n")
    if PlayerChoice in ["Rock","r","R","ROCK","rock"]:
        PlayerChoice="r"
        print("Player Choice(r for Rock)= ",PlayerChoice)
    elif PlayerChoice in ["Paper","p","P","PAPER","paper"]:
        PlayerChoice="p"
        print("Player Choice(p for Paper)= ",PlayerChoice)
    elif PlayerChoice in ["scissor","Scissor","SCISSOR","s","S"]:
        PlayerChoice="s"
        print("Player Choice(s for Scissor)= ",PlayerChoice)
    else:
        PlayerChoice=False
        print("Please enter valid option")

def CompOption():
    global CompChoice
    CompChoice=random.randrange(1,3)
    if CompChoice== 1:
        CompChoice="r"
        print("Computer Choice(r for Rock)= ",CompChoice)
    elif CompChoice==2:
        CompChoice="p"
        print("Computer Choice(p for Paper)= ",CompChoice)
    elif CompChoice==3:
        CompChoice="s"
        print("Computer Choice(s for Scissor)= ",CompChoice)

PlayerWins = 0
print("Player Score: ", PlayerWins)
CompWins = 0
print("Computer Score: ", CompWins)

while PlayerWins<5 and CompWins<5:
    PlayerOption()
    CompOption()
    if PlayerChoice=="r":
        if CompChoice=="r":
            print("Try Again! You have a Tie.\n" + "Computer Score(s): ", CompWins, "    Player Score(s): ", PlayerWins)
        elif CompChoice=="p":
            CompWins+=1
            print("Computer Wins! Paper Beats Rock.\n"+ "Computer Score(s): ",CompWins,"    Player Score(s): ",PlayerWins)
        elif CompChoice=="s":
            PlayerWins+=1
            print("Player Wins! Rock Beats Scissor.\n" + "Computer Score(s): ", CompWins , "    Player Score(s): ", PlayerWins)

    elif PlayerChoice=="s":
        if CompChoice=="s":
            print("Try Again! You have a Tie.\n"+ "Computer Score(s): ", CompWins, "   Player Score(s): ", PlayerWins)
        elif CompChoice=="p":
            PlayerWins+=1
            print("Player Wins! Scissor Beats Paper.\n"+ "Computer Score(s): ",CompWins,"   Player Score(s): ",PlayerWins)
        elif CompChoice=="r":
            CompWins+=1
            print("Player Wins! Rock Beats Scissor.\n" + "Computer Score(s): ", CompWins, "    Player Score(s): ", PlayerWins)

    elif PlayerChoice=="p":
            if CompChoice=="p":
                print("Try Again! You have a Tie.\n"+ "Computer Score(s): ", CompWins, "   Player Score(s): ", PlayerWins)
            elif CompChoice=="s":
                CompWins+=1
                print("Computer Wins! Scissor Beats Paper.\n"+ "Computer Score(s): ",CompWins,"   Player Score(s): ",PlayerWins)
            elif CompChoice=="r":
                PlayerWins+=1
                print("Player Wins! Paper Beats Rock.\n" + "Computer Score(s): ", CompWins, "    Player Score(s): ", PlayerWins)

