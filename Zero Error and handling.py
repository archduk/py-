# A simple division program that may result in a division by zero error
num1 = float(input("Enter the num1:"))
num2 = float(input("Enter the num2:"))

# This can raise a runtime error if num2 is zero
result = num1/num2

print(f"The result of the division is: {result}")
