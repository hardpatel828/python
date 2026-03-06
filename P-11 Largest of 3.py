# Implement a function that takes as input three variables, and returns the largest of the three.

# Function to find largest of three numbers
def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Take input from user
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

# Call function and print result
largest = largest_of_three(x, y, z)
print("Largest number is:", largest)