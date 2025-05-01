from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cm = CoffeeMaker()
mm = MoneyMachine()
mu = Menu()

cm.report()
mm.report()
menu_items = mu.get_items()
print(menu_items)


# py main.py
