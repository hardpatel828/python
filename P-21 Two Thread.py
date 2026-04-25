# Write a Python program that creates two threads to find and print even and odd numbers.

import threading

def print_even():
    print("Even Numbers:")
    for i in range(2, 11, 2):
        print(i)

def print_odd():
    print("Odd Numbers:")
    for i in range(1, 11, 2):
        print(i)

t1 = threading.Thread(target=print_even)
t2 = threading.Thread(target=print_odd)

t1.start()
t2.start()

t1.join()
t2.join()

print("Both threads finished execution.")
