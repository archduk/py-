# Get name from the user
name = input("Enter your name: ")

#Accept n as input from the user
n = int(input("Enter the number of characters to display from the left: "))

#Display first n characters using slicing
print("First", n, "characters of the name:", name[:n])

#Count the number of vowels using a loop and counter
vowels = 'aeiouAEIOU'
vowel_count = 0
for char in name:
    if char in vowels:
        vowel_count += 1
print(f"Number of vowels in the name: {vowel_count}")

# Reverse the string with slicing
reversed_name = name[::-1]
print(f"Reversed name: {reversed_name}")

