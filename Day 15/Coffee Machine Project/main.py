from data import MENU, COINS , resources as res
from art import mug
print(mug)


def report() -> None:
    for key, val in res.items():
        if key == "water" or key == "milk":
            print(f"{key.capitalize()}: {val}ml")
        elif key == "coffee":
            print(f"{key.capitalize()}: {val}g")
        else:
            print(f"{key.capitalize()}: ${val:.2f}")


def is_resources(drink: dict) -> bool:
    if drink["ingredients"]["water"] > res["water"]:
        return False
    elif drink["ingredients"]["milk"] > res["milk"]:
        return False
    elif drink["ingredients"]["coffee"] > res["coffee"]:
        return False
    else:
        return True
    



def coffee_machine() -> None:
    user_selection = input("What would you like? (1-espresso/2-latte/3-cappuccino):\n")
    if user_selection == "off":
        print("Machine turning off...")
        return


# TODO-4: When the user chooses a drink, the program should check if there are enough
# resources to make that drink.


# TODO-5: If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.


# TODO-6: Check that the user has inserted enough money to purchase the drink they selected.


# TODO-7: Deduct the required ingredients from the coffee machine resources after a successful transaction.


# py main.py