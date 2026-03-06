# Write a Python program that creates two threads to find and print even and odd numbers.

# Import threading module
import threading

# Function to print even numbers
def print_even():
    print("Even Numbers:")
    for i in range(2, 21, 2):
        print(i)

# Function to print odd numbers
def print_odd():
    print("Odd Numbers:")
    for i in range(1, 21, 2):
        print(i)

# Create threads
t1 = threading.Thread(target=print_even)
t2 = threading.Thread(target=print_odd)

# Start threads
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()

print("Both threads finished execution.")