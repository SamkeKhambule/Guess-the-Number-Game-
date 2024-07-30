import tkinter as tk
from tkinter import messagebox
import random

class GuessTheNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number Game")

        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.max_attempts = 10

        self.create_widgets()

    def create_widgets(self):
        # Instructions Label
        self.instructions = tk.Label(self.root, text="I have selected a number between 1 and 100. Can you guess what it is?")
        self.instructions.pack()

        # Input Entry
        self.guess_entry = tk.Entry(self.root)
        self.guess_entry.pack()

        # Guess Button
        self.guess_button = tk.Button(self.root, text="Guess", command=self.check_guess)
        self.guess_button.pack()

        # Attempts Label
        self.attempts_label = tk.Label(self.root, text=f"Attempts: {self.attempts}/{self.max_attempts}")
        self.attempts_label.pack()

        # Result Label
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

        # Replay Button
        self.replay_button = tk.Button(self.root, text="Play Again", command=self.reset_game)
        self.replay_button.pack()
        self.replay_button.config(state=tk.DISABLED)

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())

            if guess < 1 or guess > 100:
                messagebox.showerror("Invalid Input", "Please enter a number between 1 and 100.")
                return

            self.attempts += 1
            self.attempts_label.config(text=f"Attempts: {self.attempts}/{self.max_attempts}")

            if guess < self.number_to_guess:
                self.result_label.config(text="Too low! Try again.")
            elif guess > self.number_to_guess:
                self.result_label.config(text="Too high! Try again.")
            else:
                self.result_label.config(text=f"Congratulations! You've guessed the correct number in {self.attempts} attempts.")
                self.end_game()

            if self.attempts >= self.max_attempts and guess != self.number_to_guess:
                self.result_label.config(text=f"Sorry, you've used all {self.max_attempts} attempts. The number was {self.number_to_guess}.")
                self.end_game()

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

    def end_game(self):
        self.guess_entry.config(state=tk.DISABLED)
        self.guess_button.config(state=tk.DISABLED)
        self.replay_button.config(state=tk.NORMAL)

    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.attempts_label.config(text=f"Attempts: {self.attempts}/{self.max_attempts}")
        self.result_label.config(text="")
        self.guess_entry.config(state=tk.NORMAL)
        self.guess_entry.delete(0, tk.END)
        self.guess_button.config(state=tk.NORMAL)
        self.replay_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessTheNumberGame(root)
    root.mainloop()
