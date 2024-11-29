def any_lowercase5(s):
     for c in s:
          if not c.islower():
               return False
     return True

# Take user input
user_input = input("Enter a string: ")
result = any_lowercase5(user_input)
print("Function 5 result:", result)
