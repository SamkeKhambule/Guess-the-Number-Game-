import random

def guess_the_number():
    while True:
        number_to_guess = random.randint(1, 100)
        guess = None
        attempts = 0
        max_attempts = 10
        
        print("\nWelcome to the Guess the Number Game!")
        print("I have selected a number between 1 and 100. Can you guess what it is?")
        print(f"You have {max_attempts} attempts to guess the correct number.")
        
        while guess != number_to_guess and attempts < max_attempts:
            try:
                guess = int(input("Enter your guess: "))
                
                if guess < 1 or guess > 100:
                    print("Please enter a number between 1 and 100.")
                    continue
                
                attempts += 1

                if guess < number_to_guess:
                    print("Too low! Try again.")
                elif guess > number_to_guess:
                    print("Too high! Try again.")
                else:
                    print(f"Congratulations! You've guessed the correct number in {attempts} attempts.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        if guess != number_to_guess:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye.")
            break

guess_the_number()
