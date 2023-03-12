from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# set up the objects
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()
menu = Menu()

is_on = True

# TODO 6. Loop
while is_on:
    # TODO 6.1. Ask user by printing “What would you like? (espresso/latte/cappuccino):”
    options = menu.get_items()
    user_input = input(f"What would you like? ({options}): ")

    if user_input == "off":
        is_on = False
    elif user_input == "report":
        my_coffee_maker.report()
        my_money_machine.report()
    else:
        my_drink = menu.find_drink(user_input)
        print(my_drink)
        if my_coffee_maker.is_resource_sufficient(my_drink) and (my_money_machine.make_payment(my_drink.cost)):
                my_coffee_maker.make_coffee(my_drink)



