from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

MenuApp = Menu()
CoffeeMakerApp = CoffeeMaker()
MoneyMachineApp = MoneyMachine()

machine_status = True
while(machine_status):
    drinks_list = MenuApp.get_items()
    user_input = input(f"What would you like? ({drinks_list}): ").lower()
    if user_input == "off":
        machine_status = False
    elif user_input == "report":
        CoffeeMakerApp.report()
        MoneyMachineApp.report()
    else:
        OrderedItem = MenuApp.find_drink(user_input)
        if(OrderedItem):
            if(CoffeeMakerApp.is_resource_sufficient(OrderedItem)):
                if(MoneyMachineApp.make_payment(OrderedItem.cost)):
                    CoffeeMakerApp.make_coffee(OrderedItem)

        # if CoffeeMakerApp.is_resource_sufficient(OrderedItem) and MoneyMachineApp.make_payment(OrderedItem.cost):
        #     CoffeeMakerApp.make_coffee(OrderedItem)