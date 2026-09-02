# Day 15 - File Handling

# 1. Create and write to a file
file = open("demo.txt", "w")
file.write("Hello! This is my Day 15 Python practice.\n")
file.write("I am learning File Handling in Python.")
file.close()


# 2. Read the file
file = open("demo.txt", "r")
content = file.read()
print("File Content:")
print(content)
file.close()


# 3. Append data to the file
file = open("demo.txt", "a")
file.write("\nThis line was added using append mode.")
file.close()


# 4. Read line by line
file = open("demo.txt", "r")

print("\nReading line by line:")

for line in file:
    print(line.strip())

file.close()


# 5. Using with statement
# 'with' automatically closes the file

with open("demo.txt", "r") as file:
    content = file.read()

print("\nUsing with statement:")
print(content)