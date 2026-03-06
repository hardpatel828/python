# Create a program that asks the user to enter their name and their age. Print out a message addressed to 
# them that tells them the year that they will turn 100 years old.

name = input ( " Enter the name = " )
age = int ( input ( " Enter your age = " ) )
current_year = int ( input ( " Enter current year = " ) )

year_100 = 100 - age
turn_100 = current_year + year_100

print ( " Hello " , name )
print ( " You will turn 100 year in this year = ", turn_100 )