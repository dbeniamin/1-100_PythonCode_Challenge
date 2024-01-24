# RETURN - will BREAK the loop and save the function
# PRINT - will print the provided output at any point and NOT BREAK the loop

import art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    # key : value   -> dictionary data type , value can be anything from a string to a defined function
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(art.logo)

    num1 = float(input("What is the first number?: "))

    # "for" LOOP IN DICTIONARIES WILL GO THROUGH THE KEYS NOT THE VALUES 
    for symbol in operations:
        print(symbol)

    #  define the condition you need in order to be able to break the while loop
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
