# Write a Python program that executes division and handles an ArithmeticError exception if there is an
# arithmetic error.

try:
    
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b
    print("Result of division:", result)

except ArithmeticError:
   
    print("Arithmetic Error occurred! Division by zero is not allowed.")

else:
    print("Division executed successfully.")

finally:
    print("Program ended.")
