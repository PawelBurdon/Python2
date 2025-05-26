def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():

    first_number = int(input("What's the first number?: "))
    while(True):
        
        print("+\n-\n*\n/")
        operation = input("Pick an operation: ")
        second_number = int(input("What's is the next number?: "))
        result = operations[operation](first_number,second_number)
        print(f"{first_number} {operation} {second_number} = {result}")

        if_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, or q to quit: ")
        if if_continue == "y":
            first_number = result
        elif if_continue == "n":
            print("\n"*20)
            calculator()
        elif if_continue == "q":
            break

calculator()

