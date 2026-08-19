# ============================================================
# PYTHON JOURNEY - DAY 01
# Topic: Python Data Types
# ============================================================

"""
DESCRIPTION:
Python data types define the type of value stored in a variable.

Python is dynamically typed, which means we don't need to
explicitly declare the data type of a variable.

Example:
    age = 20

Python automatically understands that age is an integer.
"""


# ============================================================
# 1. INTEGER (int)
# ============================================================

age = 20
marks = 85
temperature = -5

print("Integer Examples:")
print(age)
print(marks)
print(temperature)

print("Type of age:", type(age))


# ============================================================
# 2. FLOAT (float)
# ============================================================

height = 5.9
price = 99.99
percentage = 87.5

print("\nFloat Examples:")
print(height)
print(price)
print(percentage)

print("Type of height:", type(height))


# ============================================================
# 3. STRING (str)
# ============================================================

name = "Sagar"
course = "Python Programming"

print("\nString Examples:")
print(name)
print(course)

print("Type of name:", type(name))


# ============================================================
# 4. BOOLEAN (bool)
# ============================================================

is_student = True
is_working = False

print("\nBoolean Examples:")
print(is_student)
print(is_working)

print("Type of is_student:", type(is_student))


# ============================================================
# 5. NONE (NoneType)
# ============================================================

result = None

print("\nNone Example:")
print(result)

print("Type of result:", type(result))


# ============================================================
# 6. COMPLEX NUMBERS (complex)
# ============================================================

number = 3 + 4j

print("\nComplex Number:")
print(number)

print("Type of number:", type(number))


# ============================================================
# 7. CHECKING DATA TYPES
# ============================================================

x = 100
y = 10.5
z = "Python"
a = True

print("\nChecking Data Types:")

print(type(x))
print(type(y))
print(type(z))
print(type(a))


# ============================================================
# 8. MULTIPLE VARIABLES
# ============================================================

student_name, age, cgpa = "Sagar", 20, 7.5

print("\nMultiple Variables:")
print("Name:", student_name)
print("Age:", age)
print("CGPA:", cgpa)


# ============================================================
# 9. CHANGING DATA TYPE
# ============================================================

number = 10

print("\nOriginal value:")
print(number)
print(type(number))

number = "10"

print("\nAfter changing the value:")
print(number)
print(type(number))


# ============================================================
# 10. BASIC DATA TYPE CHECKING
# ============================================================

value = 25

print("\nData Type Checking:")

if isinstance(value, int):
    print("value is an integer")

if isinstance(value, float):
    print("value is a float")

if isinstance(value, str):
    print("value is a string")


# ============================================================
# PRACTICE
# ============================================================

"""
PRACTICE QUESTIONS:

1. Create variables for:
   - Your name
   - Your age
   - Your height
   - Your CGPA
   - Whether you are a student

2. Print the value and data type of each variable.

3. Create one variable containing a complex number.

4. Create a variable with None as its value.

5. Change an integer variable into a string.

Try solving these yourself before looking at other examples.
"""


# ============================================================
# IMPORTANT NOTES
# ============================================================

"""
IMPORTANT NOTES:

1. Python is dynamically typed.
   Example:
       x = 10
       x = "Python"

2. Use type() to check the data type:
       type(variable)

3. Common Python built-in data types include:
       int
       float
       str
       bool
       complex
       list
       tuple
       set
       dict
       NoneType

4. Strings are written inside quotes:
       "Hello"
       'Python'

5. Boolean values are:
       True
       False

6. None represents the absence of a value.

7. Python variables do not require explicit type declaration.

Example:
       age = 20
       name = "Sagar"
       height = 5.9
       student = True
"""