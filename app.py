def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return  n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return  n1 / n2

calculate = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    should_accumulate = True
    n1 = float(input("What is the first number?: "))

    while should_accumulate:
        for symbol in calculate:
            print(symbol)
        operator = input("Pick the operation: ")
        n2 = float(input("What's the next number?: "))
        result = calculate[operator](n1,n2)
        print(f"{n1} {operator} {n2} = {result}")

        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if choice == "y":
            n1 = result
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()
        

        






