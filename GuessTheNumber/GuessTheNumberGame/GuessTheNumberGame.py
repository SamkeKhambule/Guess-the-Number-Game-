import unittest
from unittest.mock import patch
import random
import tkinter as tk

import GuessTheNumber.GuessTheNumberGame.guess_the_number_text as guess_the_number_text

class TestGuessTheNumberGUI(unittest.TestCase):
    
    def setUp(self):
        self.root = tk.Tk()
        self.game = guess_the_number_text(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_initial_state(self):
        self.assertEqual(self.game.attempts, 0)
        self.assertEqual(self.game.max_attempts, 10)
        self.assertTrue(1 <= self.game.number_to_guess <= 100)

    def test_check_guess_correct(self):
        self.game.number_to_guess = 50
        self.game.guess_entry.insert(0, '50')
        with patch('tkinter.messagebox.showinfo'):
            self.game.check_guess()
        self.assertEqual(self.game.result_label['text'], "Congratulations! You've guessed the correct number in 1 attempts.")

    def test_check_guess_too_low(self):
        self.game.number_to_guess = 50
        self.game.guess_entry.insert(0, '25')
        self.game.check_guess()
        self.assertEqual(self.game.result_label['text'], "Too low! Try again.")
    
    def test_check_guess_too_high(self):
        self.game.number_to_guess = 50
        self.game.guess_entry.insert(0, '75')
        self.game.check_guess()
        self.assertEqual(self.game.result_label['text'], "Too high! Try again.")

    def test_check_guess_invalid_input(self):
        self.game.guess_entry.insert(0, 'abc')
        with patch('tkinter.messagebox.showerror') as mocked_error:
            self.game.check_guess()
            mocked_error.assert_called_with("Invalid Input", "Please enter a valid number.")

    def test_check_guess_out_of_range_input(self):
        self.game.guess_entry.insert(0, '150')
        with patch('tkinter.messagebox.showerror') as mocked_error:
            self.game.check_guess()
            mocked_error.assert_called_with("Invalid Input", "Please enter a number between 1 and 100.")

    def test_end_game(self):
        self.game.end_game()
        self.assertFalse(self.game.guess_entry['state'] == tk.NORMAL)
        self.assertFalse(self.game.guess_button['state'] == tk.NORMAL)
        self.assertTrue(self.game.replay_button['state'] == tk.NORMAL)

    def test_reset_game(self):
        self.game.reset_game()
        self.assertEqual(self.game.attempts, 0)
        self.assertTrue(1 <= self.game.number_to_guess <= 100)
        self.assertEqual(self.game.result_label['text'], "")
        self.assertTrue(self.game.guess_entry['state'] == tk.NORMAL)
        self.assertTrue(self.game.guess_button['state'] == tk.NORMAL)
        self.assertFalse(self.game.replay_button['state'] == tk.NORMAL)

if __name__ == '__main__':
    unittest.main()