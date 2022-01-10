# Calculator
from art import logo

# Add
def add(n1, n2):
    return n1+n2

# Subtract
def subtract(n1, n2):
    return n1-n2

# Multiply
def multiply(n1, n2):
    return n1*n2

# Divide
def divide(n1, n2):
    return n1/n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for item in operations:
        print(item)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        is_another_calculation = input(f"Type 'y' to continue calculating with {answer}, type 'a' to start a new calculation, or type any keyword to exit the calculator: ")
        if is_another_calculation == "y":
            num1 = answer
        elif is_another_calculation == "a":
            should_continue = False
            calculator()
        else:
            should_continue = False
            
calculator()