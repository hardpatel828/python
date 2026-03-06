# Develop a program to Sort Python Dictionaries by Key or Value using Lambda.

# Create a dictionary
data = {3: 'C', 1: 'A', 2: 'B', 5: 'E', 4: 'D'}

# Sort dictionary by key using lambda
sorted_by_key = dict(sorted(data.items(), key=lambda x: x[0]))

# Print result
print("Dictionary sorted by key:")


# Create a dictionary
data = {3: 'C', 1: 'A', 2: 'B', 5: 'E', 4: 'D'}

# Sort dictionary by value using lambda
sorted_by_value = dict(sorted(data.items(), key=lambda x: x[1]))

# Print result
print("Dictionary sorted by value:")
print(sorted_by_value)