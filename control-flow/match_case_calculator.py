# match_case_calculator.py

def main():
    # Prompt the user to input two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Prompt the user to select an operation
    operation = input("Choose the operation (+, -, *, /): ")

    # Perform the calculation using match-case statement
    match operation:
        case '+':
            result = num1 + num2
            print(f"The result is {result}")
        case '-':
            result = num1 - num2
            print(f"The result is {result}")
        case '*':
            result = num1 * num2
            print(f"The result is {result}")
        case '/':
            if num2 != 0:
                result = num1 / num2
                print(f"The result is {result}")
            else:
                print("Error: Division by zero is not allowed.")
        case _:
            print("Invalid operation selected. Please choose +, -, *, or /.")

if name == "__main__":
    main() 
