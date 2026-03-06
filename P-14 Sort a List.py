# Write a Python program to sort a list of tuples using Lambda.

# List of tuples
data = [(1, 3), (4, 1), (2, 2), (5, 0)]

# Sort the list using lambda
sorted_data = sorted(data, key=lambda x: x[1])

# Print the result
print("Sorted list of tuples:")
print(sorted_data)