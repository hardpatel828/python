# Given file name of .txt file that has a list of a bunch of names, count how many of each name there are
# in the file, and print out the results to the screen.

# Ask user for file name
file_name = input("Enter file name (with .txt): ")

# Dictionary to store name counts
name_count = {}

# Open file in read mode
with open(file_name, "r") as file:
    # Read file line by line
    for line in file:
        name = line.strip()   # Remove newline and spaces

        # Count each name
        if name in name_count:
            name_count[name] += 1
        else:
            name_count[name] = 1

# Print results
print("\nName Count Results:")
for name, count in name_count.items():
    print(name, ":", count)