# ============================================================
# PYTHON JOURNEY - DAY 07
# Topic: Python Lists
# ============================================================

"""
DESCRIPTION:

A list is an ordered and mutable collection in Python.

Lists can store multiple values in a single variable.
They can contain different data types and can be modified
after creation.

Example:

numbers = [10, 20, 30, 40]

Today we will learn:

1. Creating lists
2. Accessing list elements
3. List indexing
4. Negative indexing
5. List slicing
6. Updating list elements
7. Adding elements
8. Removing elements
9. List methods
10. Sorting and reversing
11. Copying lists
12. Nested lists
13. Looping through lists
14. Useful list operations
"""


# ============================================================
# 1. CREATING A LIST
# ============================================================

print("===== CREATING LISTS =====")

numbers = [10, 20, 30, 40, 50]

names = ["Sagar", "Rahul", "Aman", "Rohit"]

mixed = [10, "Python", 3.14, True]

print(numbers)
print(names)
print(mixed)


# ============================================================
# 2. LIST INDEXING
# ============================================================

print("\n===== LIST INDEXING =====")

fruits = ["Apple", "Banana", "Mango", "Orange"]

print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])
print("Last fruit:", fruits[-1])
print("Second last fruit:", fruits[-2])


# ============================================================
# 3. LIST SLICING
# ============================================================

print("\n===== LIST SLICING =====")

numbers = [10, 20, 30, 40, 50, 60]

print("First three:", numbers[:3])
print("From index 2:", numbers[2:])
print("Index 1 to 4:", numbers[1:5])
print("Every second element:", numbers[::2])
print("Reversed list:", numbers[::-1])


# ============================================================
# 4. MODIFYING LIST ELEMENTS
# ============================================================

print("\n===== MODIFYING LIST =====")

fruits = ["Apple", "Banana", "Mango"]

print("Before:", fruits)

fruits[1] = "Orange"

print("After:", fruits)


# ============================================================
# 5. APPEND()
# ============================================================

print("\n===== APPEND =====")

fruits = ["Apple", "Banana"]

fruits.append("Mango")

print(fruits)


# ============================================================
# 6. INSERT()
# ============================================================

print("\n===== INSERT =====")

fruits = ["Apple", "Mango"]

fruits.insert(1, "Banana")

print(fruits)


# ============================================================
# 7. EXTEND()
# ============================================================

print("\n===== EXTEND =====")

fruits = ["Apple", "Banana"]

more_fruits = ["Mango", "Orange"]

fruits.extend(more_fruits)

print(fruits)


# ============================================================
# 8. REMOVE()
# ============================================================

print("\n===== REMOVE =====")

fruits = ["Apple", "Banana", "Mango"]

fruits.remove("Banana")

print(fruits)


# ============================================================
# 9. POP()
# ============================================================

print("\n===== POP =====")

fruits = ["Apple", "Banana", "Mango"]

removed_fruit = fruits.pop()

print("Removed:", removed_fruit)
print("Remaining:", fruits)


# ============================================================
# 10. DEL
# ============================================================

print("\n===== DEL =====")

numbers = [10, 20, 30, 40]

del numbers[1]

print(numbers)


# ============================================================
# 11. CLEAR()
# ============================================================

print("\n===== CLEAR =====")

numbers = [10, 20, 30]

numbers.clear()

print(numbers)


# ============================================================
# 12. LENGTH OF A LIST
# ============================================================

print("\n===== LENGTH =====")

numbers = [10, 20, 30, 40, 50]

print("Length:", len(numbers))


# ============================================================
# 13. CHECKING MEMBERSHIP
# ============================================================

print("\n===== MEMBERSHIP =====")

fruits = ["Apple", "Banana", "Mango"]

print("Apple" in fruits)
print("Orange" in fruits)

print("Orange" not in fruits)


# ============================================================
# 14. COUNT()
# ============================================================

print("\n===== COUNT =====")

numbers = [10, 20, 10, 30, 10, 40]

print("10 appears:", numbers.count(10), "times")


# ============================================================
# 15. INDEX()
# ============================================================

print("\n===== INDEX =====")

fruits = ["Apple", "Banana", "Mango"]

print("Index of Mango:", fruits.index("Mango"))


# ============================================================
# 16. SORT()
# ============================================================

print("\n===== SORT =====")

numbers = [50, 10, 40, 20, 30]

numbers.sort()

print("Ascending:", numbers)

numbers.sort(reverse=True)

print("Descending:", numbers)


# ============================================================
# 17. SORTED()
# ============================================================

print("\n===== SORTED =====")

numbers = [50, 10, 40, 20, 30]

sorted_numbers = sorted(numbers)

print("Original:", numbers)
print("Sorted:", sorted_numbers)


# ============================================================
# 18. REVERSE()
# ============================================================

print("\n===== REVERSE =====")

numbers = [10, 20, 30, 40]

numbers.reverse()

print(numbers)


# ============================================================
# 19. COPYING A LIST
# ============================================================

print("\n===== COPYING LIST =====")

original = [10, 20, 30]

copy_list = original.copy()

copy_list.append(40)

print("Original:", original)
print("Copy:", copy_list)


# ============================================================
# 20. LOOPING THROUGH A LIST
# ============================================================

print("\n===== LOOPING THROUGH LIST =====")

fruits = ["Apple", "Banana", "Mango", "Orange"]

for fruit in fruits:
    print(fruit)


# ============================================================
# 21. LIST WITH NUMBERS
# ============================================================

print("\n===== NUMBER LIST =====")

numbers = [10, 20, 30, 40, 50]

print("Sum:", sum(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))


# ============================================================
# 22. LIST COMPREHENSION
# ============================================================

print("\n===== LIST COMPREHENSION =====")

numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]

print("Numbers:", numbers)
print("Squares:", squares)


# ============================================================
# 23. LIST COMPREHENSION WITH CONDITION
# ============================================================

print("\n===== LIST COMPREHENSION WITH CONDITION =====")

numbers = range(1, 11)

even_numbers = [number for number in numbers if number % 2 == 0]

print("Even numbers:", even_numbers)


# ============================================================
# 24. NESTED LIST
# ============================================================

print("\n===== NESTED LIST =====")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)

print("First row:", matrix[0])
print("First element:", matrix[0][0])
print("Middle element:", matrix[1][1])


# ============================================================
# 25. LOOPING THROUGH A NESTED LIST
# ============================================================

print("\n===== NESTED LIST LOOP =====")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:

    for value in row:
        print(value, end=" ")

    print()


# ============================================================
# 26. PRACTICAL EXAMPLE - STUDENT MARKS
# ============================================================

print("\n===== STUDENT MARKS =====")

marks = [85, 92, 78, 88, 95]

total = sum(marks)
average = total / len(marks)

print("Marks:", marks)
print("Total:", total)
print("Average:", average)


# ============================================================
# 27. PRACTICAL EXAMPLE - FIND EVEN NUMBERS
# ============================================================

print("\n===== EVEN NUMBERS =====")

numbers = [11, 20, 35, 42, 56, 71, 80]

even_numbers = []

for number in numbers:

    if number % 2 == 0:
        even_numbers.append(number)

print("Original:", numbers)
print("Even numbers:", even_numbers)


# ============================================================
# IMPORTANT NOTES
# ============================================================

"""
IMPORTANT NOTES:

1. Lists are ordered.

2. Lists are mutable.

3. Lists allow duplicate values.

4. Lists can contain different data types.

5. Indexing starts from 0.

6. Negative indexing starts from -1.

7. List slicing follows:

       list[start:stop:step]

8. append() adds one element at the end.

9. insert() adds an element at a specific position.

10. extend() adds multiple elements.

11. remove() removes an element by value.

12. pop() removes and returns an element.

13. sort() modifies the original list.

14. sorted() returns a new sorted list.

15. reverse() reverses the original list.

16. copy() creates a copy of the list.

17. len() returns the number of elements.

18. Lists support membership operators:

       in
       not in

19. Lists can contain other lists.
    These are called nested lists.

20. List comprehensions provide a short way
    to create lists.

Example:

numbers = [1, 2, 3, 4, 5]

squares = [x ** 2 for x in numbers]
"""


# ============================================================
# PRACTICE QUESTIONS
# ============================================================

"""
PRACTICE:

1. Create a list of 5 numbers and print the list.

2. Take 5 numbers from the user and store them in a list.

3. Find the largest and smallest number in a list.

4. Calculate the sum and average of numbers in a list.

5. Count how many even and odd numbers are present in a list.

6. Remove duplicate elements from a list.

7. Reverse a list without using reverse().

8. Find the second largest number in a list.

9. Create a list of squares from 1 to 10 using
   list comprehension.

10. Create a nested list representing a 3x3 matrix
    and print its elements.
"""