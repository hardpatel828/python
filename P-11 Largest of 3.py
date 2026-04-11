# Implement a function that takes as input three variables, and returns the largest of the three.

a = int(input("Enter first number  = "))
b = int(input("Enter second number = "))
c = int(input("Enter third number  = "))

if a >= b and a >= c:
    print("Largest number is = ",a)
elif b >= a and b >= c:
    print("Largest number is = ",b)
else:
    print("Largest number is = ",c)
