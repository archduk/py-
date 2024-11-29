# Nested conditional to check age and voter eligibility
age = int(input("Enter your age\n"))
# one above the age of 18
if age >= 18:
    if age < 65:
        print("You are eligible to vote.")
    else:
        print("You are a senior citizen eligible to vote.")
#one who is below the age of 18 
else:
    print("You are not eligible to vote yet.")
