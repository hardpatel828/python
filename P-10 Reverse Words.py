# Write a function that takes a string (asks the user for a long string containing multiple words) and Print
# back to the user the same string, except with the words in backwards order.

# Function to reverse word order
def reverse_words () :
    # Take input from the user
    string = input ( " Enter a sentence = " )

    # Split sentence into words
    words = string.split ()

    # Reverse the list of words
    reversed_words = words [ ::-1 ]

    # Join words back into a string
    result = " ".join ( reversed_words )

    # Print the result
    print ( " Sentence with words reversed = " )
    print ( result )

# Call the function
reverse_words ()