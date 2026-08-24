from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

Cmachine = CoffeeMaker()
Mmachine = MoneyMachine()
menu = Menu()

while True:
    options = menu.get_items()
    select = input(f"What would you like? ({options}):").lower()
    if select == "off":
        break
    if select == "report":
        Cmachine.report()
        Mmachine.report()
    if select == "espresso" or select == "latte" or select == "cappuccino":
        item = menu.find_drink(select)
        if Cmachine.is_resource_sufficient(item):
            if Mmachine.make_payment(item.cost):
                Cmachine.make_coffee(item)
        