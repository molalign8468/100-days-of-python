from art import logo
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError:
        return "Error: Division by zero!"

def calc(num1, num2, op):
    operations = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
    }
    if op in operations:
        return operations[op](num1, num2)
    else:
        return "Invalid operator!"
print(logo)
while True:
    num1 = float(input("What's the first number?: "))
    print("+\n-\n*\n/")
    
    should_continue = True
    
    while should_continue:
        operation = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        
        result = calc(num1, num2, operation)
        
        if isinstance(result, str):
            print(result)
            should_continue = False
        else:
            print(f"{num1} {operation} {num2} = {result}")
            
            continue_calc = input(f"Type 'y' to continue with {result}, 'n' for new calculation, or 'q' to quit: ").lower()
            
            if continue_calc == 'y':
                num1 = result
            elif continue_calc == 'n':
                should_continue = False
            elif continue_calc == 'q':
                exit()
            else:
                print("Invalid choice! Starting new calculation.")
                should_continue = False