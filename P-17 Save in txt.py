# Write a program to read user name of students from console and save in a fitle(.txt).

n = int(input("Enter number of students =  "))

file = open("students.txt", "w")

for i in range(n):
    name = input("Enter student name: ")
    file.write(name + "\n")

file = open("students.txt","r")

print(file.read())

file.close()
