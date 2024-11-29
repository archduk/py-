# Function to read a dictionary from a file
def read_dict_from_file(filename):
    original_dict = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Strip whitespace and split each line by ":"
                key, value = line.strip().split(": ")
                # Add to dictionary
                original_dict[key] = value
    except FileNotFoundError:
        print("Error: The file does not exist.")
    return original_dict

# Function to invert the dictionary
def invert_dictionary(original_dict):
    inverted_dict = {}
    for key, value in original_dict.items():
        if value not in inverted_dict:
            inverted_dict[value] = []
        inverted_dict[value].append(key)
    return inverted_dict

# Function to write the inverted dictionary to a file
def write_dict_to_file(filename, dictionary):
    try:
        with open(filename, 'w') as file:
            for key, values in dictionary.items():
                # Combine list of values into a single string
                values_str = ', '.join(values)  
                file.write(f"{key}: {values_str}\n")
    except IOError:
        print("Error: Could not write to file.")

# Main Program
original_dict = read_dict_from_file("original_dict.txt")
inverted_dict = invert_dictionary(original_dict)
write_dict_to_file("inverted_dict.txt", inverted_dict)

# Print output results for the original dictionary
print("Original Dictionary:")
for key, value in original_dict.items():
    print(f"{key}: {value}")

# Print output results for the inverted dictionary
print("\nInverted Dictionary:")
for key, values in inverted_dict.items():
    values_str = ', '.join(values)
    print(f"{key}: {values_str}")
