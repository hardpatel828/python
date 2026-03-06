# Write a program to read user name of students from console and save in a fitle(.txt).

# Ask user for number of students
n = int(input("Enter number of students: "))

# Open file in write mode
file = open("students.txt", "w")

# Read names and write to file
for i in range(n):
    name = input("Enter student name: ")
    file.write(name + "\n")

# Close the file
file.close()

print("Student names saved successfully in students.txt")