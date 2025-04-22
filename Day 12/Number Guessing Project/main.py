import random
from art import logo

HARD_LEVEL = 5
EASY_LEVEL = 10


def difficulty_level() -> int:
    user_selection = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()
    while user_selection != "easy" and user_selection != "hard":
        print("Invalid input.")
        user_selection = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if user_selection == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL


def evaluate_guess(user_guess: int, actual_number: int, turns: int) -> int:
    if turns == 1:
        return -2
    if user_guess > actual_number:
        print("\nToo high.\n")
        return turns - 1
    elif user_guess < actual_number:
        print("\nToo low.\n")
        return turns - 1
    else:
        print(f"\nYou win! The answer is {actual_number}.\n")
        return -1


def game() -> None:
    print(logo)
    print("Welcome to the number guessing game!")
    target_number = random.randint(1, 100)
    num_guesses = difficulty_level()
    print(f"Number of guesses: {num_guesses}")
    print(f"The answer is: {target_number}")
    guess = 0
    while guess != target_number:
        guess = int(input("Guess a number between 1 and 100: "))
        while guess not in range(1, 101):
            print("Invalid input.")
            guess = int(input("Guess a number between 1 and 100: "))
        if num_guesses != 0:
            num_guesses = evaluate_guess(guess, target_number, num_guesses)
            if num_guesses == -2:
                print(f"\nYou have run out of guesses. The correct guess was {target_number}.")
                return None
            elif num_guesses == -1:
                return None
            elif num_guesses == 1:
                print(f"You have {num_guesses} attempt remaining.")
            else:
                print(f"You have {num_guesses} attempts remaining.")
    return None


proceed = True
while proceed:
    user_choice = input("Do you want to play? Type 'y' or 'n' ").lower()
    while user_choice != "y" and user_choice != "n":
        print("Invalid input.")
        user_choice = input("Do you want to play? Type 'y' or 'n' ").lower()
    if user_choice == "y":
        print("\n" * 100)
        game()
    else:
        print("Goodbye! 👋")
        break
