from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cm = CoffeeMaker()
mm = MoneyMachine()
mu = Menu()

is_on = True

while is_on:
    user_choice = input(f"What would you like? {mu.get_items()}: ")

    if user_choice == "off":
        print("Machine turning off...")
        is_on = False
    elif user_choice == "report":
        cm.report()
        mm.report()
    else:
        item = mu.find_drink(user_choice)
        print(item.name)
        print(item.cost)


# py main.py
