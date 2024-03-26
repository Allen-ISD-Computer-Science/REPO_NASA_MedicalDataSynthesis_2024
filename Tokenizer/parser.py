# This file will be used to filter symptoms out of user responses 

# Function to find a matching word from a list of words input
def find_matching_word(input_string, word_list):
    # Itereates over each word in the list
    for word in word_list:
        # Checks if the word is present in the input string
        if word in input_string:
            return word # Returns matching word if found
    return None 
# Gets input from the user
input_string = input("Enter a string: ")

# List of words to search for
word_list = ["enter the symptoms here"]

# Calls the function to find a matching word
matching_word = find_matching_word(input_string, word_list)

# Checks if a matching word is found
if matching_word:
    print(f"The input string matches the word '{matching_word}'.")
else:
    print("No match found.")
    