# ============================================================
# PYTHON JOURNEY - DAY 08
# Topic: Python Tuples
# ============================================================

"""
DESCRIPTION:

A tuple is an ordered and immutable collection in Python.

Tuples are similar to lists, but unlike lists, their elements
cannot be changed after the tuple is created.

Example:

numbers = (10, 20, 30, 40)

Today we will learn:

1. Creating tuples
2. Tuple indexing
3. Negative indexing
4. Tuple slicing
5. Tuple length
6. Tuple methods
7. Membership operators
8. Looping through tuples
9. Tuple packing
10. Tuple unpacking
11. Nested tuples
12. Converting between lists and tuples
13. Single-element tuples
14. Practical examples
"""


# ============================================================
# 1. CREATING A TUPLE
# ============================================================

print("===== CREATING TUPLES =====")

numbers = (10, 20, 30, 40, 50)

names = ("Sagar", "Rahul", "Aman", "Rohit")

mixed = (10, "Python", 3.14, True)

print(numbers)
print(names)
print(mixed)


# ============================================================
# 2. TUPLE INDEXING
# ============================================================

print("\n===== TUPLE INDEXING =====")

fruits = ("Apple", "Banana", "Mango", "Orange")

print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])
print("Last fruit:", fruits[-1])
print("Second last fruit:", fruits[-2])


# ============================================================
# 3. TUPLE SLICING
# ============================================================

print("\n===== TUPLE SLICING =====")

numbers = (10, 20, 30, 40, 50, 60)

print("First three:", numbers[:3])
print("From index 2:", numbers[2:])
print("Index 1 to 4:", numbers[1:5])
print("Every second element:", numbers[::2])
print("Reversed tuple:", numbers[::-1])


# ============================================================
# 4. TUPLES ARE IMMUTABLE
# ============================================================

print("\n===== IMMUTABILITY =====")

numbers = (10, 20, 30)

print("Original tuple:", numbers)

# The following line would cause an error:
# numbers[0] = 100

print("Tuple elements cannot be changed directly.")


# ============================================================
# 5. LENGTH OF A TUPLE
# ============================================================

print("\n===== LENGTH =====")

numbers = (10, 20, 30, 40, 50)

print("Length:", len(numbers))


# ============================================================
# 6. COUNT()
# ============================================================

print("\n===== COUNT =====")

numbers = (10, 20, 10, 30, 10, 40)

print("10 appears:", numbers.count(10), "times")


# ============================================================
# 7. INDEX()
# ============================================================

print("\n===== INDEX =====")

fruits = ("Apple", "Banana", "Mango")

print("Index of Mango:", fruits.index("Mango"))


# ============================================================
# 8. MEMBERSHIP OPERATORS
# ============================================================

print("\n===== MEMBERSHIP =====")

fruits = ("Apple", "Banana", "Mango")

print("Apple" in fruits)
print("Orange" in fruits)

print("Orange" not in fruits)


# ============================================================
# 9. LOOPING THROUGH A TUPLE
# ============================================================

print("\n===== LOOPING =====")

fruits = ("Apple", "Banana", "Mango", "Orange")

for fruit in fruits:
    print(fruit)


# ============================================================
# 10. TUPLE PACKING
# ============================================================

print("\n===== TUPLE PACKING =====")

student = ("Sagar", 20, "CSE")

print(student)


# ============================================================
# 11. TUPLE UNPACKING
# ============================================================

print("\n===== TUPLE UNPACKING =====")

student = ("Sagar", 20, "CSE")

name, age, branch = student

print("Name:", name)
print("Age:", age)
print("Branch:", branch)


# ============================================================
# 12. MULTIPLE ASSIGNMENT
# ============================================================

print("\n===== MULTIPLE ASSIGNMENT =====")

a, b, c = 10, 20, 30

print("a =", a)
print("b =", b)
print("c =", c)


# ============================================================
# 13. SWAPPING VARIABLES USING TUPLES
# ============================================================

print("\n===== SWAPPING =====")

a = 10
b = 20

print("Before:")
print("a =", a)
print("b =", b)

a, b = b, a

print("After:")
print("a =", a)
print("b =", b)


# ============================================================
# 14. SINGLE ELEMENT TUPLE
# ============================================================

print("\n===== SINGLE ELEMENT TUPLE =====")

number = (10,)

print(number)
print(type(number))


# This is NOT a tuple:

not_tuple = (10)

print(not_tuple)
print(type(not_tuple))


# ============================================================
# 15. NESTED TUPLES
# ============================================================

print("\n===== NESTED TUPLES =====")

matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

print(matrix)

print("First row:", matrix[0])
print("Middle element:", matrix[1][1])


# ============================================================
# 16. LOOPING THROUGH NESTED TUPLES
# ============================================================

print("\n===== NESTED TUPLE LOOP =====")

matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

for row in matrix:

    for value in row:
        print(value, end=" ")

    print()


# ============================================================
# 17. LIST TO TUPLE
# ============================================================

print("\n===== LIST TO TUPLE =====")

numbers_list = [10, 20, 30, 40]

numbers_tuple = tuple(numbers_list)

print("List:", numbers_list)
print("Tuple:", numbers_tuple)


# ============================================================
# 18. TUPLE TO LIST
# ============================================================

print("\n===== TUPLE TO LIST =====")

numbers_tuple = (10, 20, 30, 40)

numbers_list = list(numbers_tuple)

print("Tuple:", numbers_tuple)
print("List:", numbers_list)


# ============================================================
# 19. CONCATENATING TUPLES
# ============================================================

print("\n===== CONCATENATING TUPLES =====")

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

result = tuple1 + tuple2

print("Result:", result)


# ============================================================
# 20. REPEATING A TUPLE
# ============================================================

print("\n===== REPEATING TUPLE =====")

numbers = (1, 2, 3)

result = numbers * 3

print(result)


# ============================================================
# 21. MINIMUM, MAXIMUM AND SUM
# ============================================================

print("\n===== TUPLE OPERATIONS =====")

numbers = (10, 20, 30, 40, 50)

print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Sum:", sum(numbers))


# ============================================================
# 22. PRACTICAL EXAMPLE - STUDENT DETAILS
# ============================================================

print("\n===== STUDENT DETAILS =====")

student = ("Sagar", 20, "CSE", 8.5)

name, age, branch, cgpa = student

print("Name:", name)
print("Age:", age)
print("Branch:", branch)
print("CGPA:", cgpa)


# ============================================================
# 23. PRACTICAL EXAMPLE - COORDINATES
# ============================================================

print("\n===== COORDINATES =====")

point = (10, 20)

x, y = point

print("X coordinate:", x)
print("Y coordinate:", y)


# ============================================================
# IMPORTANT NOTES
# ============================================================

"""
IMPORTANT NOTES:

1. Tuples are ordered.

2. Tuples are immutable.

3. Tuples allow duplicate values.

4. Tuples can contain different data types.

5. Tuple indexing starts from 0.

6. Negative indexing starts from -1.

7. Tuple slicing works like list slicing:

       tuple[start:stop:step]

8. Tuples have two main methods:

       count()
       index()

9. Tuples support membership operators:

       in
       not in

10. Tuple packing means putting multiple values
    together into a tuple.

11. Tuple unpacking means assigning tuple values
    to multiple variables.

12. A single-element tuple requires a comma:

       (10,)

    NOT:

       (10)

13. Tuples can contain other tuples.
    These are called nested tuples.

14. A list can be converted to a tuple using:

       tuple(list_name)

15. A tuple can be converted to a list using:

       list(tuple_name)

16. Tuples are useful when data should not be changed.

17. Tuples can be concatenated using +.

18. Tuples can be repeated using *.

19. Common built-in functions:

       len()
       min()
       max()
       sum()
"""


# ============================================================
# PRACTICE QUESTIONS
# ============================================================

"""
PRACTICE:

1. Create a tuple containing 5 numbers and print it.

2. Create a tuple containing your name, age, and branch.
   Print each value using indexing.

3. Find the length of a tuple.

4. Count how many times a particular value occurs
   in a tuple.

5. Find the index of a particular element.

6. Check whether an element exists in a tuple.

7. Create a tuple and unpack its values into variables.

8. Swap two variables using tuple unpacking.

9. Convert a list into a tuple and a tuple into a list.

10. Create a nested tuple representing a 3x3 matrix
    and print the middle element.
"""