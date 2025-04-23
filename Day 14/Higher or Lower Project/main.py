import random
from game_data import data
from art import logo, vs


def is_higher(u_selection: dict, c_selection: dict) -> bool | None:
    if u_selection["follower_count"] > c_selection["follower_count"]:
        return True
    elif u_selection["follower_count"] < c_selection["follower_count"]:
        return False
    else:
        return None


def higher_lower_game():
    computer_selection = 0
    user_selection = 0
    points = 0
    proceed = True
    while proceed:
        profile_1 = random.choice(data)
        profile_2 = random.choice(data)
        print(logo)
        print(f"\nCompare A: {profile_1["name"]}, a {profile_1["description"]}, from {profile_1["country"]}.")
        print(vs)
        print(f"\nAgainst B: {profile_2["name"]}, a {profile_2["description"]} from {profile_2["country"]}.")

        user_selection = input("Who has more followers? Type 'A' or 'B': ").lower()

        while user_selection != "a" and user_selection != "b":
            print("Invalid input")
            user_selection = input("Who has more followers? Type 'A' or 'B': ").lower()

        if user_selection == "a":
            user_selection = profile_1
            computer_selection = profile_2
        elif user_selection == "b":
            user_selection = profile_2
            computer_selection = profile_1
        else:
            print("Invalid input. Try again.")
        
        if is_higher(u_selection=user_selection, c_selection=computer_selection):
            print("Correct!")
            points += 1
            print(f"Your current score is: {points}")
        else:
            print("Sorry. You lose.")
            proceed = False


higher_lower_game()

# py main.py
# py solution.py
