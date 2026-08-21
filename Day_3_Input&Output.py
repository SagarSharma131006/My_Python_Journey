# ============================================================
# PYTHON JOURNEY - DAY 03
# Topic: Input and Output in Python
# ============================================================

"""
DESCRIPTION:

Input and Output are fundamental concepts in Python.

INPUT:
The input() function is used to take data from the user.

OUTPUT:
The print() function is used to display information
on the screen.

In this lesson we will learn:

1. print()
2. input()
3. Taking different types of input
4. Multiple inputs
5. sep parameter
6. end parameter
7. Escape characters
8. f-strings
9. String formatting
"""


# ============================================================
# 1. BASIC OUTPUT USING print()
# ============================================================

print("Hello, Python!")
print("Welcome to my Python Journey.")

name = "Sagar"
age = 20

print("Name:", name)
print("Age:", age)


# ============================================================
# 2. PRINTING MULTIPLE VALUES
# ============================================================

print("\n===== MULTIPLE VALUES =====")

name = "Sagar"
age = 20
course = "CSE"

print("Name:", name, "Age:", age, "Course:", course)


# ============================================================
# 3. sep PARAMETER
# ============================================================

print("\n===== SEP PARAMETER =====")

print("2026", "08", "21", sep="-")

print("Python", "Java", "C++", sep=" | ")


# ============================================================
# 4. end PARAMETER
# ============================================================

print("\n===== END PARAMETER =====")

print("Hello", end=" ")
print("World")

print("Python", end=" -> ")
print("Programming")


# ============================================================
# 5. ESCAPE CHARACTERS
# ============================================================

print("\n===== ESCAPE CHARACTERS =====")

print("Hello\nPython")
print("Python\tProgramming")

print("He said, \"Python is easy to learn.\"")

print("C:\\Users\\Sagar\\Python")


# ============================================================
# 6. BASIC INPUT
# ============================================================

print("\n===== BASIC INPUT =====")

# Uncomment these lines when running interactively.

# name = input("Enter your name: ")
# print("Hello", name)


# ============================================================
# 7. INPUT IS ALWAYS A STRING
# ============================================================

print("\n===== INPUT DATA TYPE =====")

# Uncomment to test:

# age = input("Enter your age: ")
# print("Age:", age)
# print("Data type:", type(age))

"""
IMPORTANT:

input() always returns a string.

For example:

age = input("Enter age: ")

Even if the user enters:

20

Python stores it as:

"20"

"""


# ============================================================
# 8. TAKING INTEGER INPUT
# ============================================================

print("\n===== INTEGER INPUT =====")

# Uncomment to test:

# age = int(input("Enter your age: "))
# print("Your age is:", age)
# print("Data type:", type(age))


# ============================================================
# 9. TAKING FLOAT INPUT
# ============================================================

print("\n===== FLOAT INPUT =====")

# Uncomment to test:

# height = float(input("Enter your height: "))
# print("Height:", height)
# print("Data type:", type(height))


# ============================================================
# 10. TAKING MULTIPLE INPUTS
# ============================================================

print("\n===== MULTIPLE INPUTS =====")

# name, city = input("Enter your name and city: ").split()

# print("Name:", name)
# print("City:", city)


# ============================================================
# 11. MULTIPLE INTEGER INPUTS
# ============================================================

# Uncomment to test:

# a, b = map(int, input("Enter two numbers: ").split())

# print("First number:", a)
# print("Second number:", b)
# print("Sum:", a + b)


# ============================================================
# 12. F-STRINGS
# ============================================================

print("\n===== F-STRINGS =====")

name = "Sagar"
age = 20
cgpa = 7.5

print(f"My name is {name}.")
print(f"I am {age} years old.")
print(f"My CGPA is {cgpa}.")

print(f"My name is {name} and I am {age} years old.")


# ============================================================
# 13. STRING FORMATTING
# ============================================================

print("\n===== STRING FORMATTING =====")

name = "Sagar"
language = "Python"

print("My name is {} and I am learning {}.".format(name, language))


# ============================================================
# 14. PRACTICAL EXAMPLE
# ============================================================

print("\n===== PRACTICAL EXAMPLE =====")

# Uncomment to run:

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# city = input("Enter your city: ")

# print("\n===== STUDENT INFORMATION =====")
# print(f"Name: {name}")
# print(f"Age: {age}")
# print(f"City: {city}")


# ============================================================
# 15. SIMPLE CALCULATOR
# ============================================================

print("\n===== SIMPLE CALCULATOR =====")

# Uncomment to run:

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# print("Addition:", num1 + num2)
# print("Subtraction:", num1 - num2)
# print("Multiplication:", num1 * num2)
# print("Division:", num1 / num2)


# ============================================================
# IMPORTANT NOTES
# ============================================================

"""
IMPORTANT NOTES:

1. print() is used to display output.

2. input() is used to take input from the user.

3. input() always returns a STRING.

4. Convert input into another data type when required:

   int(input())
   float(input())

5. split() can be used to separate multiple inputs.

   Example:

   a, b = input().split()


6. map() can be used to convert multiple inputs.

   Example:

   a, b = map(int, input().split())


7. sep controls the separator between values.

   Example:

   print("A", "B", "C", sep="-")

   Output:
   A-B-C


8. end controls what is printed at the end.

   Example:

   print("Hello", end=" ")
   print("World")

   Output:
   Hello World


9. f-strings are one of the easiest ways to format strings.

   Example:

   name = "Sagar"
   print(f"Hello {name}")


10. Escape characters:

    \n  -> New line
    \t  -> Tab
    \"  -> Double quote
    \'  -> Single quote
    \\  -> Backslash
"""


# ============================================================
# PRACTICE QUESTIONS
# ============================================================

"""
PRACTICE:

1. Take your name as input and print:
   "Hello, <name>!"

2. Take two numbers from the user and print:
   - Sum
   - Difference
   - Product
   - Division

3. Take a student's:
   - Name
   - Age
   - CGPA

   Then display them using an f-string.

4. Take length and width of a rectangle
   and calculate its area.

5. Take temperature in Celsius and convert it
   into Fahrenheit.

   Formula:

   Fahrenheit = (Celsius * 9/5) + 32

6. Take three numbers in one line and calculate
   their average.

7. Create a simple bill generator that takes:
   - Product name
   - Price
   - Quantity

   Then calculate the total price.
"""