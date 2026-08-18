def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b

operations = { '+' : add, '-' : subtract, '*' : multiply, '/' : divide}

def calculator():
    num1 = float(input("Enter a first number:"))
    for key in operations:
        print(key)
    flag = True
    while(flag):
        operation_symbol = input("Enter another operation: ")
        num2 = float(input("Enter the next number:"))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        option = input(f"'y' to continue claculating with {answer}, or enter 'n' to start a new calculation: ")
        if option == 'y':    
            num1 = answer
        else:
            flag = False
            print("\n" *10)
            calculator()

calculator()