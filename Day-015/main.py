import os
clear = lambda: os.system("cls")


def Print_Report(resources, money):
    """
    Takes resources dict and money as parameter and formate and print the data.
    """
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def Check_Resources(ingredients, resources):
    """
    It takes the ingredients and resources as paramente and prints which resource is not enough 
    and returns false, and returns true only if every resources are enough.
    """
    for key in ingredients:
        if resources[key] >= ingredients[key]:
            pass
        else:
            print(f"Sorry there is not enough {key}.")
            return False
        
    return True


def Process_Coins(cost):
    """
    It takes the cost of coffee as parameter and coins as user input and prints the changes and 
    returns true if coins is sufficient and prints 'not enough money' and returns false if it is 
    not sufficient.
    """
    print("Please insert coins.")
    quaters = int(input("How many quaters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    total_money = round((quaters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01), 2)

    if total_money >= cost:
        change = total_money - cost
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money Refunded.")
        return False


def Make_Coffee(ingredients, resources):
    """
    Take ingredients and resources as input and reduce the amount of ingredients from the resources.
    """
    for key in ingredients:
        resources[key] -= ingredients[key]

    

def Coffee_Machine():
    """Coffee Machine Program"""
    MENU = {
        "espresso": {
            "ingredients": {
                "water": 50,
                "coffee": 18,
            },
            "cost": 1.5,
        },
        "latte": {
            "ingredients": {
                "water": 200,
                "milk": 150,
                "coffee": 24,
            },
            "cost": 2.5,
        },
        "cappuccino": {
            "ingredients": {
                "water": 250,
                "milk": 100,
                "coffee": 24,
            },
            "cost": 3.0,
        }
    }

    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }

    money = 0

    clear()
    loop = True
    while loop:
        option = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()

        if option == "report":
            Print_Report(resources, money)
        elif option in MENU:
            ingredients = MENU[option]["ingredients"]
            cost = MENU[option]["cost"]
            if Check_Resources(ingredients, resources):
                if Process_Coins(cost):
                    money += cost
                    Make_Coffee(ingredients, resources)
                    print(f"Here is you {option} Enjoy!")
        elif option == "off":
            loop = False
        else:
            print("Sorry, can't do it now.")


loop = True
while loop:
    Coffee_Machine()
    loop_again = input("Press 'enter' key to reset or type 'exit' to shutdown the coffee machine: ").lower()
    if loop_again == "exit":
        loop = False
        clear()