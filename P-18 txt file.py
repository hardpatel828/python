# Given file name of .txt file that has a list of a bunch of names, count how many of each name there are
# in the file, and print out the results to the screen.

file = open("students.txt","r")

data = {}

for line in file:
    name = line.strip()  

    if name in data:
        data[name] += 1
    else:
        data[name] = 1

print("\nName Count Results : ")
for key in data:
    print(key, " : ", data[key])

file.close()
