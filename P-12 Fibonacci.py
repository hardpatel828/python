# Write a function to generate N fibonacci numbers. Make sure to ask the user to enter the value of N.

n = int(input("Enter the value of N = "))
a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c=a+b
    a=b
    b=c
