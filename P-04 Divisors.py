# Create a program that asks the user for a number and then prints out a list of all the divisors of that
# number.

num = int ( input ( " Enter any number = " ) )
print ( " Divisors are = " )

i = 1
while i <= num :
    if num % i == 0 :
        print ( i )
    i = i + 1