"""
Practice

1. Create a file and write your name, age and branch into it. 
 
2. Read and print the complete content of a file. 
 
3. Append a new line to an existing file. 
 
4. Count the number of lines present in a file. 
 
5. Count the number of words present in a file. 
 
6. Count the number of characters present in a file. 
 
7. Read a file and print only the lines containing the word "Python". 
 
8. Copy the contents of one file into another file. 
 
9. Create a file containing 10 numbers and find their sum. 
 
10. Try to open a file that does not exist and handle 
    FileNotFoundError properly. 
"""


# Question 1

with open("student.txt", "w") as file:
    file.write("Name: Sagar Sharma\n")
    file.write("Age: 20\n")
    file.write("Branch: CSE AI & ML\n")

print("Data written successfully!")


# Question 2

with open("student.txt", "r") as file:
    content = file.read()

print("File Content:")
print(content)


# Question 3

with open("student.txt", "a") as file:
    file.write("College: PIET\n")

print("New line added successfully!")



# Question 4

with open("student.txt", "r") as file:
    lines = file.readlines()

print("Number of lines:", len(lines))



# Question 5

with open("student.txt", "r") as file:
    content = file.read()

words = content.split()

print("Number of words:", len(words))



# Question 6

with open("student.txt", "r") as file:
    content = file.read()

print("Number of characters:", len(content))



# Question 7

with open("python.txt", "w") as file:
    file.write("I am learning Python.\n")
    file.write("I am practicing C++.\n")
    file.write("Python is easy to learn.\n")
    file.write("I am learning Data Structures.\n")
    file.write("I use Python for Machine Learning.\n")


with open("python.txt", "r") as file:
    for line in file:
        if "Python" in line:
            print(line.strip())



# Question 8

with open("source.txt", "w") as file:
    file.write("This is the source file.\n")
    file.write("This content will be copied.\n")


with open("source.txt", "r") as source:
    content = source.read()


with open("destination.txt", "w") as destination:
    destination.write(content)

print("File copied successfully!")



# Question 9

with open("numbers.txt", "w") as file:
    for i in range(1, 11):
        file.write(str(i) + "\n")


total = 0

with open("numbers.txt", "r") as file:
    for line in file:
        number = int(line.strip())
        total += number

print("Sum:", total)



# Question 10

try:
    with open("unknown.txt", "r") as file:
        content = file.read()

    print(content)

except FileNotFoundError:
    print("Error: File not found!")



    