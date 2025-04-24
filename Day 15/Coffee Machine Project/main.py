from coffee_data import MENU, resources as res
from art import mug

# TODO-1: Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
user_selection = input("What would you like? (1-espresso/2-latte/3-cappuccino):\n")

# TODO-2: Turn off the Coffee Machine by entering “ off ” to the prompt.


# TODO-3: When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values.


def report() -> None:
    for key, val in res.items():
        if key == "water" or key == "milk":
            print(f"{key.capitalize()}: {val}ml")
        elif key == "coffee":
            print(f"{key.capitalize()}: {val}g")
        else:
            print(f"{key.capitalize()}: ${val:.2f}")
        

report()

# TODO-4: When the user chooses a drink, the program should check if there are enough
# resources to make that drink.


# TODO-5: If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.


# TODO-6: Check that the user has inserted enough money to purchase the drink they selected.


# TODO-7: Deduct the required ingredients from the coffee machine resources after a successful transaction.

# py main.py