# Develop a program to Sort Python Dictionaries by Key or Value using Lambda.

data = {5: 'C', 3: 'A', 1: 'B', 4: 'E', 2: 'D'}

sorted_by_key = dict(sorted(data.items(), key=lambda x: x[0]))

print("Dictionary sorted by key = ",sorted_by_key)

sorted_by_value = dict(sorted(data.items(), key=lambda x: x[1]))

print("Dictionary sorted by value = ",sorted_by_value)
