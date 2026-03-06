# Write a program to keep track of friend’s birthdays, and be able to find that information based on their
# name. Create a dictionary of names and birthdays. When you run your program it should ask the user
# to enter a name, and return the birthday of that person back to them.

# Dictionary to store names and birthdays
birthdays = {
    "Rahul": "12 March",
    "Amit": "25 July",
    "Sneha": "9 January",
    "Priya": "18 October",
    "Hard": "6 August"
}

# Ask user for name
name = input("Enter friend's name: ")

# Check and display birthday
if name in birthdays:
    print("Birthday of", name, "is:", birthdays[name])
else:
    print("Sorry! Birthday not found for this name.")