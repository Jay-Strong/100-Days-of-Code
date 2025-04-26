from data import MENU, COINS , resources as res
from art import mug
print(mug)
print("Welcome to Python Cafe!\n")

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
        print(f"Sorry, there is not enough water to make {beverage_type}.")
        return False
    
    if beverage["ingredients"]["coffee"] > res["coffee"]:
        print(f"Sorry, there is not enough coffee to make {beverage_type}.")
        return False
    
    if beverage_type == "latte" or beverage_type == "cappuccino":
        if beverage["ingredients"]["milk"] > res["milk"]:
            print(f"Sorry, there is not enough milk to make {beverage_type}.")
            return False
    print(f"You have selected {beverage_type}.")  
    return True


def deduct_resources(beverage_type: str) -> None:

    beverage = MENU[beverage_type]

    res["coffee"] -= beverage["ingredients"]["coffee"]
    res["water"] -= beverage["ingredients"]["water"]
    
    if beverage_type == "latte" or beverage_type == "cappuccino":
        res["milk"] -= beverage["ingredients"]["milk"]

 
def accept_payment(beverage_type: str) -> bool:

    beverage = MENU[beverage_type]
    payment = 0.0
    change = 0.0
    price = beverage["cost"]
    coin_options = {
        "1": "penny",
        "2": "nickel",
        "3": "dime",
        "4": "quarter",
    }

    print(f"Please pay ${price:.2f}")

    while True:
       coin_deposit = input(f"Please insert ${price - payment:.2f} coins. (/1-penny/2-nickel/3-dime/4-quarter) Type '0' after all coins are in: ")
       if coin_deposit == "0":
           
           if round(payment, 2) < round(price, 2):
               print(f"Sorry, not enough money...${payment:.2f} refunded.")
               return False
           elif round(payment, 2) > round(price, 2):
                change = payment - price
                payment -= change
                res["money"] += payment
                print(f"here is your ${change:.2f} in change.")
                return True
           else:
                res["money"] += payment
                return True
           
       elif coin_deposit in coin_options:
           coin = coin_options[coin_deposit]
           payment += COINS[coin]
       else:
           print("Invalid input...Try again.")
           continue
           

def process_order(selected_beverage: str) -> None:

    beverage = MENU[selected_beverage]

    if is_resources(beverage_type=selected_beverage):
        print("We can do that!")

        if accept_payment(beverage_type=selected_beverage):
            deduct_resources(beverage_type=selected_beverage)
            print(f"Here is your {selected_beverage}...Enjoy!")



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