# Write a Python program to find a given string is happy or unhappy. A string is happy if every three
# consecutive characters are distinct.

string = input ( " Enter a string = ")
happy = True

for i in range ( len ( string ) - 2 ):
    if string [ i ] == string [ i+1 ] or string [ i+1 ] == string [ i+2 ] or string [ i ] == string [ i+2 ] :
        happy = False
        break

if happy :
    print ( " The string is happy " )
else :
    print ( " The string is unhappy " )    