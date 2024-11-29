try:
    # Attempt to open a non-existent file
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    # Handling the file not found error
    print("Error: The file does not exist. Please check the filename and try again.")
