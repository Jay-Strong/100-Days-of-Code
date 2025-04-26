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


def is_resources(beverage_type: str) -> bool:
    beverage = MENU[beverage_type]

    if beverage["ingredients"]["water"] > res["water"]:
        f"Sorry, there is not enough water to make {beverage_type}."
        return False
    
    if beverage["ingredients"]["coffee"] > res["coffee"]:
        f"Sorry, there is not enough coffee to make {beverage_type}."
        return False
    
    if beverage_type == "latte" or beverage_type == "cappuccino":
        if beverage["ingredients"]["milk"] > res["milk"]:
            f"Sorry, there is not enough milk to make {beverage_type}."
            return False
        
    return True


    
def accept_payment(beverage_type: str) -> None:
    beverage = MENU[beverage_type]
    payment = 0.0
    price = f"${beverage["cost:"]:.2f}"
    while payment < beverage["cost"]:
        input(f"Please insert {price} (penny/nickel/dime/quarter): ") 
        # TODO: Add logic for coin insertion, resource deduction


def process_order(selected_beverage: str) -> None:
    beverage = MENU[selected_beverage]
    if is_resources(beverage_type=selected_beverage):
        print("Hooray!")

    
    

    

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

coffee_machine()
# TODO-5: If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.


# TODO-6: Check that the user has inserted enough money to purchase the drink they selected.


# TODO-7: Deduct the required ingredients from the coffee machine resources after a successful transaction.


# py main.py