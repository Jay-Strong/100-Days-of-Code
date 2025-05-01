import random
from game_data import data
from art import logo, vs


def format_data(account: dict) -> str:
    """Accepts a user account as an argument
       and returns a formatted sentence with the account data"""

    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name} a {account_desc} from {account_country}."


def is_higher(guess: str, u_followers: int, c_followers: int) -> bool:
    """Accepts user guess, and the number of followers
       for each account and returns bool which determines if a user is correct or not"""

    if u_followers > c_followers:
        return guess == "a"
    else:
        return guess == "b"


def higher_lower_game() -> None:
    print(logo)

    # Select a random profile from game data
    profile_2 = random.choice(data)
    points = 0
    proceed = True

    # Make the game repeatable if the user continues to win.
    while proceed:

        # Shuffle the profiles and select another random profile 
        profile_1 = profile_2
        profile_2 = random.choice(data)

        # If the profiles are identical then profile 2 gets randomized again
        if profile_1 == profile_2:
            profile_2 = random.choice(data)

        # Save the number of followers for the profiles to variables
        follower_count_1 = profile_1["follower_count"]
        follower_count_2 = profile_2["follower_count"]

        # Save the output for the profile data to variables
        data_line_1 = format_data(account=profile_1)
        data_line_2 = format_data(account=profile_2)

        # Display profile comparisons
        print(f"Compare A: {data_line_1}")
        print(vs)
        print(f"\nAgainst B: {data_line_2}")

        # User makes a guess
        user_selection = input("Who has more followers? Type 'A' or 'B': ").lower()
        
        # Verify user input
        while user_selection != "a" and user_selection != "b":
            print("Invalid input")
            user_selection = input("Who has more followers? Type 'A' or 'B': ").lower()

        # Clear the console
        print("\n" * 20)

        # Decide if the user guessed correctly.
        # Continue if user guessed correctly. End game otherwise.
        if is_higher(guess=user_selection, u_followers=follower_count_1, c_followers=follower_count_2):
            points += 1
            print(f"\nCorrect! Your current score is: {points}")
        else:
            print(f"\nSorry. You lose. Final score: {points}\n")
            proceed = False


higher_lower_game()

# py main.py
# py solution.py
