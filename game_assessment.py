import random

def play():
    options = ["rock", "paper", "scissors"]
    computer = random.choice(options)
    player = input("Choose rock, paper, or scissors: ").lower()

    if player not in options:
        print("Invalid choice. Try again.")
        return

    print(f"You chose {player}, computer chose {computer}.")

    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("You lose!")

if __name__ == "__main__":
    while True:
        play()
        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            break
