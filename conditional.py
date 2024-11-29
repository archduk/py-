#chained conditional to categorize age group
# user inputs the age
age=int(input('Enter your age\n'))
# if the age is less than 18 the output will be Minor
if age < 18:
    print("Minor")
# if the age is more than 18 the output will be Adult
elif 18 <= age < 65:
    print("Adult")
#if the age is above 65 the output will be Senior Citizen
else:
    print("Senior Citizen")
