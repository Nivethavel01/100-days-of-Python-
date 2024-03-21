from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

'''Setting objects for different classes'''
cof_maker_obj=CoffeeMaker()
money_machine_obj=MoneyMachine()
menu_obj=Menu()
menuitem_obj_name=MenuItem
print(menuitem_obj_name)
      
coffee_input= None
while coffee_input !="off" :
    print("\n╭──────────.★..─╮\n")
    print(menu_obj.get_items())
    print("╰─..★.──────────╯\n")
    coffee_input = input("What would you like?")
    
    '''Shut down the coffee machine'''
    if (coffee_input == "off"):
      exit
      
      '''Print the report'''
    elif coffee_input == "report" :
        cof_maker_obj.report()
        money_machine_obj.report()
    else:
        drink=menu_obj.find_drink(coffee_input)
        if cof_maker_obj.is_resource_sufficient(drink) :
            money_machine_obj.make_payment(drink.cost)
            cof_maker_obj.make_coffee(drink)