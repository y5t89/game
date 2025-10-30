import tkinter as tk
import random

class RPSGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors")

        self.options = ["rock", "paper", "scissors"]
        self.player_score = 0
        self.computer_score = 0

        self.player_name = tk.StringVar()
        self.result_text = tk.StringVar()
        self.score_text = tk.StringVar(value="Score — You: 0 | Computer: 0")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Enter your name:").pack()
        tk.Entry(self.root, textvariable=self.player_name).pack()

        tk.Label(self.root, text="Choose your move:").pack()

        for option in self.options:
            tk.Button(self.root, text=option.title(), command=lambda o=option: self.play_round(o)).pack(pady=2)

        tk.Label(self.root, textvariable=self.result_text, font=("Arial", 12, "bold")).pack(pady=10)
        tk.Label(self.root, textvariable=self.score_text).pack()

    def play_round(self, player_choice):
        computer_choice = random.choice(self.options)
        winner = self.get_winner(player_choice, computer_choice)

        name = self.player_name.get() or "Player"
        if winner == "player":
            self.player_score += 1
            self.result_text.set(f"{name} chose {player_choice}, computer chose {computer_choice}. ✅ {name} wins!")
        elif winner == "computer":
            self.computer_score += 1
            self.result_text.set(f"{name} chose {player_choice}, computer chose {computer_choice}. ❌ Computer wins!")
        else:
            self.result_text.set(f"Both chose {player_choice}. 🤝 It's a tie!")

        self.score_text.set(f"Score — {name}: {self.player_score} | Computer: {self.computer_score}")

    def get_winner(self, player, computer):
        if player == computer:
            return "tie"
        elif (player == "rock" and computer == "scissors") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissors" and computer == "paper"):
            return "player"
        else:
            return "computer"

if __name__ == "__main__":
    root = tk.Tk()
    game = RPSGame(root)
    root.mainloop()
    