import math

def hypotenuse(a, b):
    # Compute the square root of a^2 + b^2
    return math.sqrt(a**2 + b**2)

# Testing with inputs
result = hypotenuse(3,4)
result1=hypotenuse(19,9)
print(f"The hypotenuse of a triangle with sides 3 and 4 is: {result}")

print(f"The hypotenuse of a triangle with sides 19 and 9 is: {result1}")
