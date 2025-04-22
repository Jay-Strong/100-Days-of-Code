from art import logo


def add(n1, n2): return n1 + n2


def subtract(n1, n2): return n1 - n2


def multiply(n1, n2): return n1 * n2


def divide(n1, n2): return n1 / n2


math_ops_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def perform_operation(num1: float, num2: float, sign: str) -> float:
    """Takes two numbers and an operator as inputs and performs
       the operation selected by the user."""
    return math_ops_dict[sign](num1, num2)


def calculator_app():
    proceed = True
    print(logo)
    print("Welcome to the Python Calculator!\n")
    first_number = float(input("What's the first number?: "))
    while proceed:
        for key in math_ops_dict:
            print(key)
        math_operator = input("Pick a math operation: ")
        second_number = float(input("What's the next number?: "))
        result = perform_operation(first_number, second_number, math_operator)
        print(f"{first_number} {math_operator} {second_number} = {result}")
        continue_calculation = input(f"Type 'y' to continue calculating with {result}, "
                                     f"or type 'n' to start a new calculation, "
                                     f"or type 'q' to quit: \n").lower()
        while continue_calculation != "y" and continue_calculation != "n" and continue_calculation != "q":
            print("Invalid Input.")
            continue_calculation = input(f"Type 'y' to continue calculating with {result}, "
                                         f"or type 'n' to start a new calculation, "
                                         f"or type 'q' to quit: \n").lower()
        if continue_calculation == "y":
            first_number = result
        elif continue_calculation == "n":
            proceed = False
            print("\n" * 100)
            calculator_app()
        elif continue_calculation == "q":
            print("Goodbye 🙂")
            return
        else:
            return


calculator_app()
