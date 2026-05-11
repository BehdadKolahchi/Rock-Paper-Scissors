import random 

print("Welcome to Rock/Paper/Scissors in Python!")
print("This game is Coded by Behdad Kolahchi.\n\
e-mail: kolahchibehdad@gmail.com")

def StartGame():
    UserChoice = input("Enter your Choice (R/P/S): ").upper()
    ChoicesList = ["Rock", "Paper", "Scissors"]
    ComputerChoice = random.choice(ChoicesList)

    # Validate input
    while UserChoice not in ["R", "P", "S"]:
        UserChoice = input("Please enter the correct Choice (R/P/S): ").upper()

    print(f"The computer chose: {ComputerChoice}")

    # Rock
    if ComputerChoice == "Rock" and UserChoice == "S":
        print("You lost!")
    elif ComputerChoice == "Rock" and UserChoice == "P":
        print("You Won!")
    elif ComputerChoice == "Rock" and UserChoice == "R":
        print("A Draw!")

    # Paper
    elif ComputerChoice == "Paper" and UserChoice == "S":
        print("You Won!")
    elif ComputerChoice == "Paper" and UserChoice == "P":
        print("A Draw!")
    elif ComputerChoice == "Paper" and UserChoice == "R":
        print("You Lost!")

    # Scissors
    elif ComputerChoice == "Scissors" and UserChoice == "S":
        print("A Draw!")
    elif ComputerChoice == "Scissors" and UserChoice == "P":
        print("You Lost!")
    elif ComputerChoice == "Scissors" and UserChoice == "R":
        print("You Won!")

def Intro():
    GameStarting = input("Do you want to Continue? (y/n): ").lower()

    # Validate input
    while GameStarting not in ["y", "n"]:
        GameStarting = input("Please enter the correct Choice (y/n): ").lower()

    if GameStarting == "y":
        StartGame()
        return True
    else:  # gameStarting == "n"
        print("Thanks for playing! Goodbye!")
        return False

# Main game loop
while True:
    if not Intro():
        break
