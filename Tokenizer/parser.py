# This file will be used to filter symptoms out of user responses 

# Function to find a matching word from a list of words input
def find_matching_word(input_string, word_list):
    words = []
    # Itereates over each word in the list
    for word in word_list:
        # Checks if the word is present in the input string
        if word in input_string:
            words.append(word)
    if words == []:
        return None
    else:
        return words
# Gets input from the user
input_string = input("Enter a string: ")

# List of words to search for
word_list = ["enter the symptoms here"]

# Calls the function to find a matching word
matching_words = find_matching_word(input_string, word_list)

# Checks if a matching word is found
if matching_words:
    print(f"The input string matches the words '{matching_words}'.")
else:
    print("No match found.")
    