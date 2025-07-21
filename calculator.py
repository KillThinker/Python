from art import logo
operator = {'+': '+', '-': '-', '*': '*', '/': '/'}

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calculator_app():
    print(logo)
    first_number = float(input("What's the first number?: "))
    still_continue = True
    while still_continue:
        print('+' + '\n' + '-' + '\n' + '/' + '\n' + '*')
        operation = input("Pick an operation: ")
        next_number = float(input("What's the next number?: "))
        result = 0
        if operation == operator['+']:
            result = add(first_number, next_number)
        elif operation == operator['-']:
            result = subtract(first_number, next_number)
        elif operation == operator['*']:
            result = multiply(first_number, next_number)
        elif operation == operator['/']:
            result = divide(first_number, next_number)
        print(f"{first_number} {operator[operation]} {next_number} = {result}")
        order = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
        if order == 'n':
            still_continue = False
            calculator_app()
        elif order == 'y':
            first_number = result


calculator_app()
