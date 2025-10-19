# 251008 Day 29 of Python

# Day 16 Project
# Making the OPP Coffee Machine project

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine() # 객체만들고 변수 저장
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
        # 위 두 문장을 합쳐서
        # if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
        # 라고 할수도있음! 
                coffee_maker.make_coffee(drink)
        else:
            is_on = False
