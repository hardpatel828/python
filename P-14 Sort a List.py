# Write a Python program to sort a list of tuples using Lambda.

data = [(1, 3), (4, 1), (2, 2), (5, 0)]

sorted_data = sorted(data, key=lambda x: x[1])

print("Sorted list of tuples = ",sorted_data)
