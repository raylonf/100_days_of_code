from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
drink_menu = Menu()
coffee_machine = CoffeeMaker()
coffee_machine_payment = MoneyMachine()

while True:
    dr = input('What wold you like? (espresso/latte/cappuccino) ')

    if dr == 'report':
        coffee_machine.report()
        coffee_machine_payment.report()

    elif dr == 'espresso' or dr =='latte' or dr == 'cappuccino':
        drink = (drink_menu.find_drink(dr))
        if coffee_machine.is_resource_sufficient(drink):
            if coffee_machine_payment.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)       
               
    elif dr == 'off':
        print('Good bye!')
        break
    else:
        print('Option invalid!')




