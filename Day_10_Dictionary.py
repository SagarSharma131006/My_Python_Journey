# ============================================================
# PYTHON JOURNEY - DAY 10
# Topic: Python Dictionaries
# ============================================================

"""
DESCRIPTION:

A dictionary is a collection of data stored in
KEY : VALUE pairs.

Example:

student = {
    "name": "Sagar",
    "age": 20,
    "branch": "CSE"
}

Dictionaries are:
- Ordered (Python 3.7+)
- Mutable
- Indexed using keys
- Able to store different data types
- Able to store unique keys

Today we will learn:

1. Creating dictionaries
2. Accessing values
3. Adding elements
4. Updating elements
5. Removing elements
6. Dictionary methods
7. Keys
8. Values
9. Items
10. Membership operators
11. Looping
12. Nested dictionaries
13. Dictionary from user input
14. Dictionary comprehension
15. Practical examples
"""


# ============================================================
# 1. CREATING A DICTIONARY
# ============================================================

print("===== CREATING DICTIONARIES =====")

student = {
    "name": "Sagar",
    "age": 20,
    "branch": "CSE",
    "cgpa": 8.5
}

print(student)


# ============================================================
# 2. ACCESSING VALUES
# ============================================================

print("\n===== ACCESSING VALUES =====")

student = {
    "name": "Sagar",
    "age": 20,
    "branch": "CSE"
}

print("Name:", student["name"])
print("Age:", student["age"])
print("Branch:", student["branch"])


# ============================================================
# 3. get()
# ============================================================

print("\n===== get() =====")

student = {
    "name": "Sagar",
    "age": 20
}

print(student.get("name"))
print(student.get("age"))

# get() returns None if the key does not exist.

print(student.get("city"))

# We can also provide a default value.

print(student.get("city", "Not Available"))


# ============================================================
# 4. ADDING A NEW ELEMENT
# ============================================================

print("\n===== ADDING ELEMENT =====")

student = {
    "name": "Sagar",
    "age": 20
}

student["branch"] = "CSE"

print(student)


# ============================================================
# 5. UPDATING AN ELEMENT
# ============================================================

print("\n===== UPDATING ELEMENT =====")

student = {
    "name": "Sagar",
    "age": 20,
    "branch": "CSE"
}

student["age"] = 21

print(student)


# ============================================================
# 6. update()
# ============================================================

print("\n===== update() =====")

student = {
    "name": "Sagar",
    "age": 20
}

student.update({
    "branch": "CSE",
    "cgpa": 8.5
})

print(student)


# ============================================================
# 7. keys()
# ============================================================

print("\n===== keys() =====")

student = {
    "name": "Sagar",
    "age": 20,
    "branch": "CSE"
}

print(student.keys())


# ============================================================
# 8. values()
# ============================================================

print("\n===== values() =====")

print(student.values())


# ============================================================
# 9. items()
# ============================================================

print("\n===== items() =====")

print(student.items())


# ============================================================
# 10. CHECKING A KEY
# ============================================================

print("\n===== MEMBERSHIP =====")

student = {
    "name": "Sagar",
    "age": 20,
    "branch": "CSE"
}

print("name" in student)
print("city" in student)

print("city" not in student)


# ============================================================
# 11. REMOVING ELEMENT - pop()
# ============================================================

print("\n===== pop() =====")

student = {
    "name": "Sagar",
    "age": 20,
    "branch": "CSE"
}

removed = student.pop("age")

print("Removed value:", removed)
print("Dictionary:", student)


# ============================================================
# 12. popitem()
# ============================================================

print("\n===== popitem() =====")

student = {
    "name": "Sagar",
    "age": 20,
    "branch": "CSE"
}

removed = student.popitem()

print("Removed:", removed)
print("Dictionary:", student)


# ============================================================
# 13. del
# ============================================================

print("\n===== del =====")

student = {
    "name": "Sagar",
    "age": 20,
    "branch": "CSE"
}

del student["age"]

print(student)


# ============================================================
# 14. clear()
# ============================================================

print("\n===== clear() =====")

student = {
    "name": "Sagar",
    "age": 20
}

student.clear()

print(student)


# ============================================================
# 15. LOOPING THROUGH KEYS
# ============================================================

print("\n===== LOOP THROUGH KEYS =====")

student = {
    "name": "Sagar",
    "age": 20,
    "branch": "CSE"
}

for key in student:
    print(key)


# ============================================================
# 16. LOOPING THROUGH VALUES
# ============================================================

print("\n===== LOOP THROUGH VALUES =====")

for value in student.values():
    print(value)


# ============================================================
# 17. LOOPING THROUGH KEY-VALUE PAIRS
# ============================================================

print("\n===== LOOP THROUGH ITEMS =====")

for key, value in student.items():
    print(key, ":", value)


# ============================================================
# 18. DICTIONARY WITH DIFFERENT DATA TYPES
# ============================================================

print("\n===== DIFFERENT DATA TYPES =====")

data = {
    "name": "Sagar",
    "age": 20,
    "cgpa": 8.5,
    "is_student": True,
    "skills": ["Python", "C++", "SQL"]
}

print(data)


# ============================================================
# 19. NESTED DICTIONARY
# ============================================================

print("\n===== NESTED DICTIONARY =====")

students = {
    "student1": {
        "name": "Sagar",
        "age": 20,
        "branch": "CSE"
    },

    "student2": {
        "name": "Rahul",
        "age": 21,
        "branch": "ECE"
    }
}

print(students)

print("Student 1 Name:", students["student1"]["name"])
print("Student 2 Branch:", students["student2"]["branch"])


# ============================================================
# 20. DICTIONARY WITH LIST
# ============================================================

print("\n===== DICTIONARY WITH LIST =====")

student = {
    "name": "Sagar",
    "skills": ["Python", "C++", "SQL"]
}

print("Name:", student["name"])
print("Skills:", student["skills"])

print("First skill:", student["skills"][0])


# ============================================================
# 21. USER INPUT - STUDENT DICTIONARY
# ============================================================

print("\n===== USER INPUT =====")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
branch = input("Enter your branch: ")

student = {
    "name": name,
    "age": age,
    "branch": branch
}

print("\nStudent Details:")
print(student)


# ============================================================
# 22. DICTIONARY OF MARKS
# ============================================================

print("\n===== MARKS =====")

marks = {
    "Math": 85,
    "Python": 92,
    "C++": 88,
    "SQL": 90
}

print("Python Marks:", marks["Python"])

print("All subjects and marks:")

for subject, mark in marks.items():
    print(subject, ":", mark)


# ============================================================
# 23. FIND TOTAL AND AVERAGE
# ============================================================

print("\n===== TOTAL AND AVERAGE =====")

marks = {
    "Math": 85,
    "Python": 92,
    "C++": 88,
    "SQL": 90
}

total = sum(marks.values())
average = total / len(marks)

print("Total:", total)
print("Average:", average)


# ============================================================
# 24. FIND HIGHEST MARK
# ============================================================

print("\n===== HIGHEST MARK =====")

marks = {
    "Math": 85,
    "Python": 92,
    "C++": 88,
    "SQL": 90
}

highest = max(marks.values())

print("Highest Mark:", highest)


# ============================================================
# 25. DICTIONARY COMPREHENSION
# ============================================================

print("\n===== DICTIONARY COMPREHENSION =====")

numbers = [1, 2, 3, 4, 5]

squares = {
    number: number ** 2
    for number in numbers
}

print(squares)


# ============================================================
# 26. EVEN / ODD USING DICTIONARY COMPREHENSION
# ============================================================

print("\n===== EVEN / ODD =====")

numbers = [1, 2, 3, 4, 5, 6]

result = {
    number: "Even" if number % 2 == 0 else "Odd"
    for number in numbers
}

print(result)


# ============================================================
# 27. COPY A DICTIONARY
# ============================================================

print("\n===== COPY =====")

student = {
    "name": "Sagar",
    "age": 20
}

student_copy = student.copy()

print("Original:", student)
print("Copy:", student_copy)


# ============================================================
# 28. PRACTICAL EXAMPLE - PRODUCT
# ============================================================

print("\n===== PRODUCT =====")

product = {
    "name": "Laptop",
    "price": 55000,
    "brand": "HP",
    "in_stock": True
}

print("Product:", product["name"])
print("Price:", product["price"])
print("Brand:", product["brand"])
print("Available:", product["in_stock"])


# ============================================================
# IMPORTANT NOTES
# ============================================================

"""
IMPORTANT NOTES:

1. Dictionary stores data in KEY : VALUE pairs.

2. Example:

       student = {
           "name": "Sagar",
           "age": 20
       }

3. Keys must be unique.

4. Values can be duplicated.

5. Dictionaries are mutable.

6. Access values using:

       dictionary["key"]

7. get() can safely access a key.

       dictionary.get("key")

8. Add a new element:

       dictionary["city"] = "Panipat"

9. Update an element:

       dictionary["age"] = 21

10. update() can add/update multiple elements.

11. Important dictionary methods:

       keys()
       values()
       items()
       get()
       update()
       pop()
       popitem()
       clear()
       copy()

12. Membership operators check KEYS:

       "name" in student

13. Loop through keys:

       for key in student:

14. Loop through values:

       for value in student.values():

15. Loop through key-value pairs:

       for key, value in student.items():

16. Dictionaries can contain lists.

17. Dictionaries can contain other dictionaries.
    These are called nested dictionaries.

18. Dictionary comprehension allows us to create
    dictionaries in a compact way.

19. Example:

       squares = {
           x: x ** 2
           for x in range(1, 6)
       }

20. Dictionary keys must be hashable.

21. Dictionaries are extremely important in Python
    and will become very useful later in:
    
       Data Analysis
       Pandas
       Machine Learning
       APIs
       JSON
       Data Processing
"""


# ============================================================
# PRACTICE QUESTIONS
# ============================================================

"""
PRACTICE:

1. Create a dictionary containing your name, age,
   branch and CGPA. Print each value.

2. Add a new key "city" to the dictionary.

3. Update your CGPA.

4. Delete the age key.

5. Check whether "name" exists in the dictionary.

6. Print all keys, values and key-value pairs.

7. Create a dictionary containing marks of 5 subjects.
   Find:
       - Total marks
       - Average marks
       - Highest marks

8. Create a nested dictionary containing details
   of 3 students.

9. Create a dictionary containing numbers from 1 to 10
   and their squares using dictionary comprehension.

10. Create a dictionary containing numbers from 1 to 10
    and store "Even" or "Odd" as their values.
"""