# Ask the user for a string and print out whether this string is a palindrome or not.

string = input ( " Enter a string = " )

reverse_string = string [ ::-1 ]

if string == reverse_string :
    print( " The string is a Palindrome " )
else :
    print( " The string is not a Palindrome " )