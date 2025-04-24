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


def check_resources(beverage_type: str) -> str:
    beverage = MENU[beverage_type]
    if beverage["ingredients"]["water"] > res["water"]:
        return f"Sorry, there is not enough water to make {beverage}."
    elif beverage["ingredients"]["milk"] > res["milk"]:
        return f"Sorry, there is not enough milk to make {beverage}."
    elif beverage["ingredients"]["coffee"] > res["coffee"]:
        return f"Sorry, there is not enough coffee to make {beverage}."
    else:
        return f"Preparing your {beverage_type} now..."
    
def prepare_drink(drink_name: str) -> None:
    drink = MENU[drink_name]
    check_resources(beverage_type=drink_name)

def coffee_machine() -> None:
    while True:
        user_selection = input("What would you like? (1-espresso/2-latte/3-cappuccino):\n")
        if user_selection == "off":
            print("Machine turning off...")
            return
        elif user_selection == "report":
            report()
            continue
        elif user_selection == "1":
            user_selection = "espresso"
            # More code
        elif user_selection == "2":
            user_selection = "latte"
            # More code
        elif user_selection == "3":
            user_selection = "cappuccino"
            # More code  
        else:
            print("Input error...Try again")
            continue


# TODO-4: When the user chooses a drink, the program should check if there are enough
# resources to make that drink.


# TODO-5: If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.


# TODO-6: Check that the user has inserted enough money to purchase the drink they selected.


# TODO-7: Deduct the required ingredients from the coffee machine resources after a successful transaction.


# py main.py