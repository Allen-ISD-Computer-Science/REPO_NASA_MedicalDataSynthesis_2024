#This file will be used to filter symptoms out of user responses 

def find_matching_word(input_string, word_list):
    for word in word_list:
        if word in input_string:
            return word
    return None

input_string = input("Enter a string: ")
word_list = ["enter the symptoms here"]
matching_word = find_matching_word(input_string, word_list)
if matching_word:
    print(f"The input string matches the word '{matching_word}'.")
else:
    print("No match found.")
    