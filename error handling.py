# Improved version with error handling for division by zero
try:
    num1 = float(input("Enter the num1: "))
    num2 = float(input("Enter the num2: "))

    # Attempting the division operation
    result = num1/num2
    print(f"The result of the division is: {result}")

except ZeroDivisionError:
    # Handling the division by zero error
    print("Error: Division by zero is not allowed. Please enter a valid number.")
