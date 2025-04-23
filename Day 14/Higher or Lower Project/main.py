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


def is_higher(guess: str, u_followers: int, c_followers: int) -> bool | None:
    """Accepts user guess, and the number of followers
       for each account and returns bool which determines if a user is correct or not"""

    if u_followers > c_followers:
        return guess == "a"
    else:
        return guess == "b"


def higher_lower_game() -> None:
    print(logo)

    computer_selection = 0
    user_selection = 0
    points = 0
    profile_2 = random.choice(data)
    proceed = True

    while proceed:

        profile_1 = profile_2
        profile_2 = random.choice(data)
        if profile_1 == profile_2:
            profile_2 = random.choice(data)

        follower_count_1 = profile_1["follower_count"]
        follower_count_2 = profile_2["follower_count"]

        data_line_1 = format_data(account=profile_1)
        data_line_2 = format_data(account=profile_2)

        print(f"Compare A: {data_line_1}")
        print(vs)
        print(f"\nAgainst B: {data_line_2}")

        user_selection = input("Who has more followers? Type 'A' or 'B': ").lower()

        while user_selection != "a" and user_selection != "b":
            print("Invalid input")
            user_selection = input("Who has more followers? Type 'A' or 'B': ").lower()

        print("\n" * 20)

        if is_higher(guess=user_selection, u_followers=follower_count_1, c_followers=follower_count_2):
            points += 1
            print(f"\nCorrect! Your current score is: {points}")
        else:
            print(f"\nSorry. You lose. Final score: {points}\n")
            proceed = False


higher_lower_game()

# py main.py
# py solution.py
