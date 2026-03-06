# Write a Python program that executes division and handles an ArithmeticError exception if there is an
# arithmetic error.

# Program to perform division with exception handling

try:
    # Take input from user
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    # Perform division
    result = a / b
    print("Result of division:", result)

except ArithmeticError:
    # Handles arithmetic errors like division by zero
    print("Arithmetic Error occurred! Division by zero is not allowed.")

else:
    print("Division executed successfully.")

finally:
    print("Program ended.")