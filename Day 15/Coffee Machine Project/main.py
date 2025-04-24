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


def check_resources(beverage_type: str) -> str | None:
    beverage = MENU[beverage_type]
    if beverage["ingredients"]["water"] > res["water"]:
        return f"Sorry, there is not enough water to make {beverage_type}."
    elif beverage["ingredients"]["milk"] > res["milk"]:
        return f"Sorry, there is not enough milk to make {beverage_type}."
    elif beverage["ingredients"]["coffee"] > res["coffee"]:
        return f"Sorry, there is not enough coffee to make {beverage_type}."
    else:
        return
    
def accept_payment(beverage_type: str) -> None:
    beverage = MENU[beverage_type]
    payment = 0.0
    while payment < beverage["cost"]:
        input("Please insert coins (penny/nickel/dime/quarter): ") 
        # TODO: Add logic for coin insertion and resource deduction


def process_order(selected_beverage: str) -> None:
    beverage = MENU[selected_beverage]
    check_resources(beverage_type=selected_beverage)
    
    print(f"Preparing your {selected_beverage}...")

    

def coffee_machine() -> None:
    drink_options = {
        "1": "espresso",
        "2": "latte",
        "3": "cappuccino"
    }
    while True:
        user_selection = input("What would you like? (1-espresso/2-latte/3-cappuccino):").lower()
        if user_selection == "off":
            print("Machine turning off...")
            break
        elif user_selection == "report":
            report()
        elif user_selection in drink_options:
            drink_name = drink_options[user_selection]
            process_order(selected_beverage=drink_name)
        else:
            print("Input error...Try again")


# TODO-5: If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.


# TODO-6: Check that the user has inserted enough money to purchase the drink they selected.


# TODO-7: Deduct the required ingredients from the coffee machine resources after a successful transaction.


# py main.py