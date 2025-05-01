from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cm = CoffeeMaker()
mm = MoneyMachine()
mu = Menu()

is_on = True

while is_on:
    options = mu.get_items()
    user_choice = input(f"What would you like? ({options}): ")

    if user_choice == "off":
        print("Machine turning off...")
        is_on = False
    elif user_choice == "report":
        cm.report()
        mm.report()
    else:
        item = mu.find_drink(user_choice)
        if item != None:
           if cm.is_resource_sufficient(item):
               print("We can do that! 😁")
               if mm.make_payment(item.cost):
                   cm.make_coffee(item)



# py main.py
