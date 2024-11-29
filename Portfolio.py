import math

def circle_area(radius):
#Computes the area of a circle given its radius.
    return math.pi * radius ** 2

# Test the function
area = circle_area(5)
area1 = circle_area(7)
area2 = circle_area(12)
print(f"The area of a circle with radius 5 is: {area}")
print(f"The area of a circle with radius 7 is: {area1}")
print(f"The area of a circle with radius 12 is: {area2}")
