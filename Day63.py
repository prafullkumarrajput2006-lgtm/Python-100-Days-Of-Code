# # Exercise 5... Solution... "Snake Water Gun" Game... 


# Snake, Water and Gun is a variation of the children's game like "Rock-Paper-Scissors" where players use hand gesture to represents a Snake, Water or Gun. The Gun beats the snake, the Water beats the Gun and the Snake beats the Water.
# Write a python code program to create a snake Water Gun game in Python using if-else statement. Use proper function to check for win.









import random


def check_winner(player, computer):

    if player == computer:
        return "It's a Draw! Because both chose the same option."

    elif player == "S" and computer == "W":
        return "You Won! Because Snake drinks Water."

    elif player == "W" and computer == "G":
        return "You Won! Because Water damages the Gun."

    elif player == "G" and computer == "S":
        return "You Won! Because Gun kills the Snake."

    elif computer == "S" and player == "W":
        return "You Lost! Because Snake drinks Water."

    elif computer == "W" and player == "G":
        return "You Lost! Because Water damages the Gun."

    elif computer == "G" and player == "S":
        return "You Lost! Because Gun kills the Snake."


choices = ["S", "W", "G"]

names = {
    "S": "Snake",
    "W": "Water",
    "G": "Gun"
}

print("===== SNAKE, WATER, GUN GAME =====")
print("S - Snake")
print("W - Water")
print("G - Gun")

player = input("\nEnter your choice (S/W/G): ").strip().upper()

if player not in choices:
    print("Invalid Choice! Please enter S, W, or G.")

else:
    computer = random.choice(choices)

    print("\nYou chose:", names[player])
    print("Computer chose:", names[computer])

    result = check_winner(player, computer)

    print("\n===== GAME RESULT =====")
    print(result)