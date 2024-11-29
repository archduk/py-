# Nested conditional to check user age and membership status
age = int(input("Enter your age\n"))
member = input("Are you a member? (yes/no): ")

if age >= 18:
    if member == "yes":
#if one is a member
        print("Welcome! You are eligible for a discount.")
#if one is not a member
    else:
        print("You are eligible but no discount available.")
#if one is below 18 
else:
    print("You are not eligible due to age restrictions.")
