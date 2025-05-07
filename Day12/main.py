import random
from art import logo

def start_game():
    computer_guess = random.randint(1, 100)
    attempts = 0
    print(logo)
    print("I'm thinking of a number between 1 and 100.")

    while True:
        difficulty_level = input("Choose difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty_level == 'easy':
            attempts = 10
            break
        elif difficulty_level == 'hard':
            attempts = 5
            break
        print("Invalid input. Please try again.")

    print(f"You have {attempts} attempts to guess the number.")

    while attempts > 0:
        try:
            user_guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if user_guess > computer_guess:
            attempts -= 1
            print(f"Too high! Attempts left: {attempts}")
        elif user_guess < computer_guess:
            attempts -= 1
            print(f"Too low! Attempts left: {attempts}")
        else:
            print(f"Congratulations! You guessed the number {computer_guess}!")
            return

    print(f"\nYou've run out of attempts. The number was {computer_guess}. Game over!")

start_game()