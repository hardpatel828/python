# Write a function that takes a string (asks the user for a long string containing multiple words) and Print
# back to the user the same string, except with the words in backwards order.

string = input ( " Enter a sentence = " )
 
words = string.split ()

words.reverse()

result = " ".join ( words )

print ( " Sentence with words reversed = ",result)
