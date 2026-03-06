# Write a Python program to find the no of vowels in a given string.

string = input ( " Enter a string = " )
vowels = "aeiouAEIOU"
no_of_vowels = 0

for ch in string:
    
    if ch in vowels:
        no_of_vowels = no_of_vowels + 1

print ( " Number of vowels = " , no_of_vowels)