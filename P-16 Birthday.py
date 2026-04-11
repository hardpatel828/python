# Write a program to keep track of friend’s birthdays, and be able to find that information based on their
# name. Create a dictionary of names and birthdays. When you run your program it should ask the user
# to enter a name, and return the birthday of that person back to them.

birthdays = {
    "Hard": "12 March",
    "Dax": "25 July",
    "Aryan": "9 January",
    "Akshay": "18 October",
    "Bhavesh": "6 August"
}

name = input("Enter friend's name: ")

if name in birthdays:
    print("Birthday of", name, "is:", birthdays[name])
else:
    print("Sorry! Birthday not found for this name.")
