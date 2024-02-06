from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

### create objects to access the class defined methods ###
money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()
menu = Menu()

is_on = True

coffe_maker.report()
money_machine.report()

while is_on:
    option = menu.get_items()
    choice = input(f"What would you like ? ({option}) ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        # have if condition to make the coffe
        # code could have 2 nested if statements or 1 if + and statement
        if coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffe_maker.make_coffee(drink)
