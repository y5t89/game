import random

def get_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "player"
    else:
        return "computer"

def play_game():
    options = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0
    rounds = 5

    print("🎮 Welcome to Rock, Paper, Scissors!")
    print(f"First to win {rounds} rounds wins the game.\n")

    for round_num in range(1, rounds + 1):
        print(f"--- Round {round_num} ---")
        player = input("Choose rock, paper, or scissors: ").lower()
        if player not in options:
            print("Invalid choice. Try again.\n")
            continue

        computer = random.choice(options)
        print(f"You chose {player}, computer chose {computer}.")

        winner = get_winner(player, computer)
        if winner == "player":
            print("✅ You win this round!\n")
            player_score += 1
        elif winner == "computer":
            print("❌ Computer wins this round!\n")
            computer_score += 1
        else:
            print("🤝 It's a tie!\n")

    print("🏁 Game Over!")
    print(f"Final Score — You: {player_score} | Computer: {computer_score}")
    if player_score > computer_score:
        print("🎉 Congratulations! You won the game!")
    elif computer_score > player_score:
        print("💻 The computer wins this time. Better luck next round!")
    else:
        print("😐 It's a draw!")

if __name__ == "__main__":
    play_game()

