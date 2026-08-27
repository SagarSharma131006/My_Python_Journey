# ============================================================
# PYTHON JOURNEY - DAY 09
# Topic: Python Sets
# ============================================================

"""
DESCRIPTION:

A set is an unordered and mutable collection of unique elements.

Sets are especially useful when we need to:
- Remove duplicate values
- Check membership quickly
- Perform mathematical set operations
- Find union, intersection, and difference

Example:

numbers = {10, 20, 30, 40}

Today we will learn:

1. Creating sets
2. Duplicate elements
3. Set data types
4. Adding elements
5. Removing elements
6. discard()
7. pop()
8. clear()
9. Membership operators
10. Set length
11. Union
12. Intersection
13. Difference
14. Symmetric Difference
15. Subsets
16. Supersets
17. Disjoint sets
18. Updating sets
19. Converting list to set
20. Practical examples
"""


# ============================================================
# 1. CREATING A SET
# ============================================================

print("===== CREATING SETS =====")

numbers = {10, 20, 30, 40, 50}

fruits = {"Apple", "Banana", "Mango", "Orange"}

mixed = {10, "Python", 3.14, True}

print(numbers)
print(fruits)
print(mixed)


# ============================================================
# 2. DUPLICATE ELEMENTS
# ============================================================

print("\n===== DUPLICATES =====")

numbers = {10, 20, 10, 30, 20, 40}

print(numbers)

# Duplicate values are automatically removed.


# ============================================================
# 3. EMPTY SET
# ============================================================

print("\n===== EMPTY SET =====")

empty_set = set()

print(empty_set)
print(type(empty_set))

# {} creates an empty dictionary, NOT an empty set.


# ============================================================
# 4. ADDING ELEMENTS - add()
# ============================================================

print("\n===== ADD =====")

fruits = {"Apple", "Banana"}

fruits.add("Mango")

print(fruits)


# ============================================================
# 5. ADDING MULTIPLE ELEMENTS - update()
# ============================================================

print("\n===== UPDATE =====")

fruits = {"Apple", "Banana"}

fruits.update(["Mango", "Orange", "Grapes"])

print(fruits)


# ============================================================
# 6. REMOVE()
# ============================================================

print("\n===== REMOVE =====")

fruits = {"Apple", "Banana", "Mango"}

fruits.remove("Banana")

print(fruits)

# remove() gives an error if the element does not exist.


# ============================================================
# 7. DISCARD()
# ============================================================

print("\n===== DISCARD =====")

fruits = {"Apple", "Banana", "Mango"}

fruits.discard("Banana")

print(fruits)

# discard() does NOT give an error if the element doesn't exist.


# ============================================================
# 8. POP()
# ============================================================

print("\n===== POP =====")

numbers = {10, 20, 30, 40}

removed = numbers.pop()

print("Removed element:", removed)
print("Remaining set:", numbers)

# Set is unordered, so pop() removes an arbitrary element.


# ============================================================
# 9. CLEAR()
# ============================================================

print("\n===== CLEAR =====")

numbers = {10, 20, 30}

numbers.clear()

print(numbers)


# ============================================================
# 10. LENGTH OF A SET
# ============================================================

print("\n===== LENGTH =====")

numbers = {10, 20, 30, 40, 50}

print("Length:", len(numbers))


# ============================================================
# 11. MEMBERSHIP OPERATORS
# ============================================================

print("\n===== MEMBERSHIP =====")

fruits = {"Apple", "Banana", "Mango"}

print("Apple" in fruits)
print("Orange" in fruits)

print("Orange" not in fruits)


# ============================================================
# 12. LOOPING THROUGH A SET
# ============================================================

print("\n===== LOOPING =====")

fruits = {"Apple", "Banana", "Mango", "Orange"}

for fruit in fruits:
    print(fruit)


# ============================================================
# 13. UNION
# ============================================================

print("\n===== UNION =====")

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

result = set_a.union(set_b)

print("Set A:", set_a)
print("Set B:", set_b)
print("Union:", result)


# ============================================================
# 14. UNION USING | OPERATOR
# ============================================================

print("\n===== UNION USING | =====")

set_a = {1, 2, 3}
set_b = {3, 4, 5}

result = set_a | set_b

print("Union:", result)


# ============================================================
# 15. INTERSECTION
# ============================================================

print("\n===== INTERSECTION =====")

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

result = set_a.intersection(set_b)

print("Intersection:", result)


# ============================================================
# 16. INTERSECTION USING & OPERATOR
# ============================================================

print("\n===== INTERSECTION USING & =====")

set_a = {1, 2, 3}
set_b = {2, 3, 4}

result = set_a & set_b

print("Intersection:", result)


# ============================================================
# 17. DIFFERENCE
# ============================================================

print("\n===== DIFFERENCE =====")

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

result = set_a.difference(set_b)

print("A - B:", result)


# ============================================================
# 18. DIFFERENCE USING - OPERATOR
# ============================================================

print("\n===== DIFFERENCE USING - =====")

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5}

result = set_a - set_b

print("A - B:", result)


# ============================================================
# 19. SYMMETRIC DIFFERENCE
# ============================================================

print("\n===== SYMMETRIC DIFFERENCE =====")

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

result = set_a.symmetric_difference(set_b)

print("Symmetric Difference:", result)


# ============================================================
# 20. SYMMETRIC DIFFERENCE USING ^ OPERATOR
# ============================================================

print("\n===== SYMMETRIC DIFFERENCE USING ^ =====")

set_a = {1, 2, 3}
set_b = {3, 4, 5}

result = set_a ^ set_b

print("Symmetric Difference:", result)


# ============================================================
# 21. SUBSET
# ============================================================

print("\n===== SUBSET =====")

set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}

print("A is subset of B:", set_a.issubset(set_b))


# ============================================================
# 22. SUPERSET
# ============================================================

print("\n===== SUPERSET =====")

set_a = {1, 2, 3, 4, 5}
set_b = {1, 2, 3}

print("A is superset of B:", set_a.issuperset(set_b))


# ============================================================
# 23. DISJOINT SETS
# ============================================================

print("\n===== DISJOINT =====")

set_a = {1, 2, 3}
set_b = {4, 5, 6}

print("Are sets disjoint?", set_a.isdisjoint(set_b))


# ============================================================
# 24. CONVERTING LIST TO SET
# ============================================================

print("\n===== LIST TO SET =====")

numbers = [10, 20, 10, 30, 20, 40, 30]

unique_numbers = set(numbers)

print("Original list:", numbers)
print("Unique values:", unique_numbers)


# ============================================================
# 25. CONVERTING SET TO LIST
# ============================================================

print("\n===== SET TO LIST =====")

numbers = {10, 20, 30, 40}

numbers_list = list(numbers)

print("Set:", numbers)
print("List:", numbers_list)


# ============================================================
# 26. PRACTICAL EXAMPLE - REMOVE DUPLICATES
# ============================================================

print("\n===== REMOVE DUPLICATES =====")

numbers = [10, 20, 10, 30, 20, 40, 10]

unique_numbers = list(set(numbers))

print("Original:", numbers)
print("Without duplicates:", unique_numbers)


# ============================================================
# 27. PRACTICAL EXAMPLE - COMMON ELEMENTS
# ============================================================

print("\n===== COMMON ELEMENTS =====")

students_python = {"Sagar", "Rahul", "Aman", "Rohit"}

students_cpp = {"Aman", "Rohit", "Vikas", "Karan"}

common_students = students_python.intersection(students_cpp)

print("Students learning both:", common_students)


# ============================================================
# 28. PRACTICAL EXAMPLE - UNIQUE WORDS
# ============================================================

print("\n===== UNIQUE WORDS =====")

sentence = "python is easy and python is powerful"

words = sentence.split()

unique_words = set(words)

print("Words:", words)
print("Unique words:", unique_words)


# ============================================================
# IMPORTANT NOTES
# ============================================================

"""
IMPORTANT NOTES:

1. Sets are unordered.

2. Sets are mutable.

3. Sets do NOT allow duplicate elements.

4. Sets do not support indexing.

   Example:

       numbers[0]  ❌

5. Use set() to create an empty set.

       empty_set = set()

   {} creates an empty dictionary.

6. add() adds one element.

7. update() adds multiple elements.

8. remove() removes an element and gives an
   error if the element does not exist.

9. discard() removes an element without giving
   an error if it does not exist.

10. pop() removes an arbitrary element.

11. clear() removes all elements.

12. Important set operations:

       Union
       Intersection
       Difference
       Symmetric Difference

13. Operators:

       |  → Union
       &  → Intersection
       -  → Difference
       ^  → Symmetric Difference

14. Set relationship methods:

       issubset()
       issuperset()
       isdisjoint()

15. A list can be converted into a set:

       set(my_list)

16. A set can be converted into a list:

       list(my_set)

17. Sets are very useful for removing duplicate
    values from a collection.

18. Set elements must be hashable, so mutable
    objects such as lists cannot be elements of a set.
"""


# ============================================================
# PRACTICE QUESTIONS
# ============================================================

"""
PRACTICE:

1. Create a set containing 5 numbers and print it.

2. Create a set containing duplicate values and observe
   what happens.

3. Add a new element to a set using add().

4. Remove an element using remove() and discard().

5. Find the union of two sets.

6. Find the intersection of two sets.

7. Find the difference between two sets.

8. Find the symmetric difference between two sets.

9. Check whether one set is a subset of another set.

10. Given a list containing duplicate values, use a set
    to find the unique values.
"""