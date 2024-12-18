# capitalize_words.py

def capitalize_words(input_string):
    # Split the string into words
    words = input_string.split()
    
    # Capitalize the first letter of each word and join them back
    capitalized_words = ' '.join([word.capitalize() for word in words])
    
    return capitalized_words

# Accept user input
if __name__ == "__main__":
    input_string = input("Enter a string: ")  # This will allow the user to input a string
    print(capitalize_words(input_string))  # Output the capitalized version of the string
