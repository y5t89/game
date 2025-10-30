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

def get_computer_choice(difficulty, last_player_choice):
    options = ["rock", "paper", "scissors"]
    if difficulty == "easy" or last_player_choice is None:
        return random.choice(options)
    # Hard mode: counter the player's last move
    counter = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
    return counter[last_player_choice]

def play_game():
    options = ["rock", "paper", "scissors"]
    print("🎮 Welcome to Rock, Paper, Scissors!")
    player_name = input("Enter your name: ").strip().title()

    difficulty = input("Choose difficulty (easy/hard): ").lower()
    while difficulty not in ["easy", "hard"]:
        difficulty = input("Invalid choice. Choose 'easy' or 'hard': ").lower()

    rounds = input(f"Hi {player_name}, how many rounds would you like to play? ")
    while not rounds.isdigit() or int(rounds) <= 0:
        rounds = input("Please enter a valid positive number: ")
    rounds = int(rounds)

    player_score = 0
    computer_score = 0
    history = []
    last_player_choice = None

    for round_num in range(1, rounds + 1):
        print(f"\n--- Round {round_num} ---")
        player = input(f"{player_name}, choose rock, paper, or scissors: ").lower()
        if player not in options:
            print("Invalid choice. Try again.")
            continue

        computer = get_computer_choice(difficulty, last_player_choice)
        last_player_choice = player

        print(f"{player_name} chose {player}, computer chose {computer}.")
        winner = get_winner(player, computer)

        if winner == "player":
            print(f"✅ {player_name} wins this round!")
            player_score += 1
            history.append(f"Round {round_num}: {player_name} won")
        elif winner == "computer":
            print("❌ Computer wins this round!")
            computer_score += 1
            history.append(f"Round {round_num}: Computer won")
        else:
            print("🤝 It's a tie!")
            history.append(f"Round {round_num}: Tie")

        print(f"Score — {player_name}: {player_score} | Computer: {computer_score}")

    print("\n🏁 Game Over!")
    print("📜 Game History:")
    for entry in history:
        print(entry)

    print(f"\nFinal Score — {player_name}: {player_score} | Computer: {computer_score}")
    if player_score > computer_score:
        print(f"🎉 Congratulations {player_name}, you won the game!")
    elif computer_score > player_score:
        print(f"💻 Sorry {player_name}, the computer wins this time.")
    else:
        print(f"😐 It's a draw, {player_name}!")

    replay = input("\nWould you like to play again? (y/n): ").lower()
    if replay == 'y':
        play_game()
    else:
        print(f"Thanks for playing, {player_name}! 👋")

if __name__ == "__main__":
    play_game()

