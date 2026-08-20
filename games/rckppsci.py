import random

option = ("rock","paper","scissors")

running = True

while running:
# while player == computer:
    player = None
    computer = random.choice(option)
    while player not in option:
      player = input("Rock paper scissors ")
    # computer = input("Paper rock scissors ")

    print(f"player chose {player}")
    print(f"computer chose {computer}")

    if player == computer:
        print("Draw")
    elif player == "rock" and computer == "paper":
        print("You win")
    elif player == "paper" and computer == "scissors":
        print("You lose")
    elif player == "scissors" and computer == "rock":
        print("You win")
    elif player == "scissors" and computer == "paper":
        print("You lose")
    elif player == "paper" and computer == "rock":
        print("You win")
    elif player == "paper" and computer == "scissors":
        print("You lose")
    elif player == "scissors" and computer == "paper":
        print("You win")
    elif player == "scissors" and computer == "rock":
        print("You lose")
    elif player == "scissors" and computer == "paper":
        print("You win")
    elif player == "paper" and computer == "scissors":
        print("You lose")
    elif player == "paper" and computer == "rock":
        print("You win")
    elif player == "scissors" and computer == "paper":
        print("You lose")
    elif player == "scissors" and computer == "rock":
        print("You lose")
    elif player == "scissors" and computer == "paper":
        print("You win")
    else:
        print("You lose")
    if not input("play again ? (y/n)").lower() == "y":
        running = False
print("goodbye")