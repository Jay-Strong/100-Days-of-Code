from data import MENU , resources as res
from art import mug
print(mug)
print("Welcome to Python Cafe!\n")

def report() -> None:
    units = {
        "water": "ml",
        "milk": "ml",
        "coffee": "g",
        "money": "$",

    }

    for key, val in res.items():
        unit = units.get(key, "")
        if key == "money":
            print(f"{key.capitalize()}: {unit}{val:.2f}")
        else:
            print(f"{key.capitalize()}: {val}{unit}")


def is_resources(beverage_type: str) -> bool:
    ingredients = MENU[beverage_type]["ingredients"]

    for item, required_amount in ingredients.items():
        if required_amount > res[item]:
            print(f"Sorry, there is not enough {item} to make a {beverage_type}.")
            return False

    print(f"You have selected {beverage_type}.")
    return True


def deduct_resources(beverage_type: str) -> None:
    ingredients = MENU[beverage_type]["ingredients"]

    for item, deduct_resources in ingredients.items():
        res[item] -= deduct_resources


 
def accept_payment(beverage_type: str) -> bool:
    beverage = MENU[beverage_type]
    price = beverage["cost"]
    payment = 0.0
    coin_values = {
        "1": 0.01,  # penny
        "2": 0.05,  # nickel
        "3": 0.10,  # dime
        "4": 0.25,  # quarter
    }

    print(f"Please pay ${price:.2f}")

    while round(payment, 2) < round(price, 2):
        remaining = price - payment
        coin_deposit = input(f"Insert ${remaining:.2f} (1-penny/2-nickel/3-dime/4-quarter, or '0' to cancel): ")

        if coin_deposit == "0":
            print(f"Transaction canceled. Refunding ${payment:.2f}.")
            return False
        elif coin_deposit in coin_values:
            payment += coin_values[coin_deposit]
        else:
            print("Invalid input. Please try again.")

    change = round(payment - price, 2)
    res["money"] += price  # Add the exact price to the machine's money
    if change > 0:
        print(f"Here is your ${change:.2f} in change.")
    return True
           

def process_order(selected_beverage: str) -> None:
    if is_resources(beverage_type=selected_beverage):
        print("We can do that!")

        if accept_payment(beverage_type=selected_beverage):
            deduct_resources(beverage_type=selected_beverage)
            print(f"Here is your {selected_beverage}☕...Enjoy!")


def coffee_machine() -> None:
    drink_options = {
        "1": "espresso",
        "2": "latte",
        "3": "cappuccino",
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


# py main.py