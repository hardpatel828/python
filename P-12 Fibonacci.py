# Write a function to generate N fibonacci numbers. Make sure to ask the user to enter the value of N.

# Function to generate N Fibonacci numbers
def fibonacci(n):
    a = 0
    b = 1

    print("Fibonacci Series:")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Ask user for value of N
n = int(input("Enter the value of N: "))

# Call the function
fibonacci(n)