from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker =CoffeeMaker()
menu= Menu()
money_machine=MoneyMachine()
should_cont=True
while should_cont:
    print("what would ou like to choose?")
    user_input=input(menu.get_items())
    if user_input=="off":
        should_cont=False
    elif user_input=="report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink=menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(drink) == True:

            if money_machine.make_payment(drink.cost) == True:
                coffee_maker.make_coffee(drink)
                # coffee_maker.report()
                # money_machine.report()
            else:
                should_cont = False
        else:
            should_cont=False

