from game_data import data
import random
from art import logo, vs
 # Jay is the man!

def is_higher(u_selection: dict, c_selection: dict) -> bool | None:
    if u_selection["follower_count"] > c_selection["follower_count"]:
        return True
    elif u_selection["follower_count"] < c_selection["follower_count"]:
        return False
    else:
        return None


def higher_lower_game():
    print(logo)
    profile_1 = random.choice(data)
    profile_2 = random.choice(data)
    print(f"\nCompare A: {profile_1["name"]}, a {profile_1["description"]}, from {profile_1["country"]}.")
    print(vs)
    print(f"\nAgainst B: {profile_2["name"]}, a {profile_2["description"]} from {profile_2["country"]}.")

    user_selection = input("Who has more followers? Type 'A' or 'B': ").lower()

    while user_selection != "a" and user_selection != "b":
        print("Invalid input")
        user_selection = input("Who has more followers? Type 'A' or 'B': ").lower()

    if user_selection == "a":
        user_selection = profile_1
    elif user_selection == "b":
        user_choice = profile_2
    else:
        print("Invalid input. Try again.")


higher_lower_game()
