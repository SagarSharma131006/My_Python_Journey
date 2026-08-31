# ============================================================
# PYTHON JOURNEY - DAY 13
# Topic: Modules & Packages
# ============================================================

"""
Today I learned about Modules and Packages.

A module is simply a Python file containing code
that we can reuse in another Python file.

Instead of putting everything in one large file,
we can divide our program into smaller modules.
"""


# ============================================================
# 1. IMPORTING OUR OWN MODULE
# ============================================================

import math_operations


print("===== USING MATH MODULE =====")

print("Addition:", math_operations.add(10, 5))
print("Subtraction:", math_operations.subtract(10, 5))
print("Multiplication:", math_operations.multiply(10, 5))
print("Division:", math_operations.divide(10, 5))


# ============================================================
# 2. IMPORTING SPECIFIC FUNCTIONS
# ============================================================

from math_operations import add, multiply


print("\n===== IMPORTING SPECIFIC FUNCTIONS =====")

print("Addition:", add(20, 10))
print("Multiplication:", multiply(20, 10))


# ============================================================
# 3. IMPORTING WITH AN ALIAS
# ============================================================

import math_operations as math_ops


print("\n===== USING ALIAS =====")

print("Addition:", math_ops.add(50, 25))


# ============================================================
# 4. IMPORTING ANOTHER MODULE
# ============================================================

from student import student_info


print("\n===== STUDENT INFORMATION =====")

student_info(
    "Sagar",
    20,
    "CSE"
)


# ============================================================
# 5. BUILT-IN MODULE — math
# ============================================================

import math


print("\n===== MATH MODULE =====")

print("Square root:", math.sqrt(25))
print("Power:", math.pow(2, 3))
print("Value of pi:", math.pi)


# ============================================================
# 6. BUILT-IN MODULE — random
# ============================================================

import random


print("\n===== RANDOM MODULE =====")

random_number = random.randint(1, 100)

print("Random number:", random_number)


# ============================================================
# 7. BUILT-IN MODULE — datetime
# ============================================================

import datetime


print("\n===== DATETIME MODULE =====")

current_date = datetime.date.today()

print("Today's date:", current_date)


# ============================================================
# 8. BUILT-IN MODULE — os
# ============================================================

import os


print("\n===== OS MODULE =====")

print("Current working directory:")
print(os.getcwd())


# ============================================================
# IMPORTANT NOTES
# ============================================================

"""
IMPORTANT NOTES:

1. A MODULE is a Python file (.py) containing
   functions, variables or classes.

2. We can import a module using:

       import module_name


3. We can access something from a module using:

       module_name.function_name()


4. We can import specific functions using:

       from module_name import function_name


5. We can import multiple functions:

       from module_name import add, multiply


6. We can give a module an alias:

       import math_operations as math_ops


7. Python also provides many built-in modules.

   Examples:

       math
       random
       datetime
       os


8. A PACKAGE is a collection of related Python
   modules organized in a directory.

9. Modules help us:

       Organize code
       Reuse code
       Avoid repetition
       Make projects easier to maintain


10. Instead of having one huge Python file:

       project.py

    we can organize our code:

       project/
       │
       ├── main.py
       ├── calculator.py
       ├── student.py
       └── utilities.py


------------------------------------------------------------
WHAT I LEARNED TODAY
------------------------------------------------------------

Earlier I was writing all my code inside one file.

Today I learned that Python allows me to divide my
program into multiple files and reuse them using imports.

This will become very useful when I start working on
larger Python projects.
"""