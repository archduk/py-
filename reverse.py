# Input a sentence from the user
sentence = input("Enter a sentence: ")

# Split the sentence into a list of words
word_list = sentence.split()

# Reverse the word list
reversed_word_list = word_list[::-1]  

# Output the results
print("Original Word List:", word_list)
print("Reversed Word List:", reversed_word_list)
