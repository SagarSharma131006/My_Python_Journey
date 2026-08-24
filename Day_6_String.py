# ============================================================
# PYTHON JOURNEY - DAY 06
# Topic: Python Strings
# ============================================================

"""
DESCRIPTION:

A string is a sequence of characters enclosed inside
single quotes (' '), double quotes (" "), or triple quotes.

Strings are one of the most commonly used data types in Python.

In this file, we will learn:

1. Creating strings
2. String indexing
3. String slicing
4. String concatenation
5. String repetition
6. String methods
7. String formatting
8. Escape characters
9. Membership operators
10. Useful string operations
"""


# ============================================================
# 1. CREATING STRINGS
# ============================================================

print("===== CREATING STRINGS =====")

name = "Sagar"
course = 'Python'
message = """Python is a powerful programming language."""

print(name)
print(course)
print(message)


# ============================================================
# 2. STRING INDEXING
# ============================================================

print("\n===== STRING INDEXING =====")

text = "Python"

print("First character:", text[0])
print("Second character:", text[1])
print("Last character:", text[-1])
print("Second last character:", text[-2])


# ============================================================
# 3. STRING SLICING
# ============================================================

print("\n===== STRING SLICING =====")

text = "Python Programming"

print("First 6 characters:", text[:6])
print("From index 7:", text[7:])
print("Characters 0 to 5:", text[0:6])
print("Every second character:", text[::2])
print("Reverse:", text[::-1])


# ============================================================
# 4. STRING CONCATENATION
# ============================================================

print("\n===== STRING CONCATENATION =====")

first_name = "Sagar"
last_name = "Sharma"

full_name = first_name + " " + last_name

print("Full Name:", full_name)


# ============================================================
# 5. STRING REPETITION
# ============================================================

print("\n===== STRING REPETITION =====")

word = "Python "

print(word * 3)


# ============================================================
# 6. STRING LENGTH
# ============================================================

print("\n===== STRING LENGTH =====")

text = "Python"

print("Length:", len(text))


# ============================================================
# 7. STRING METHODS
# ============================================================

print("\n===== STRING METHODS =====")

text = "  Python Programming  "

print("Original:", text)
print("Upper:", text.upper())
print("Lower:", text.lower())
print("Title:", text.title())
print("Capitalized:", text.capitalize())
print("Stripped:", text.strip())


# ============================================================
# 8. REPLACE()
# ============================================================

print("\n===== REPLACE =====")

text = "I am learning Java."

new_text = text.replace("Java", "Python")

print(new_text)


# ============================================================
# 9. SPLIT()
# ============================================================

print("\n===== SPLIT =====")

text = "Python is easy to learn"

words = text.split()

print(words)


# ============================================================
# 10. JOIN()
# ============================================================

print("\n===== JOIN =====")

words = ["Python", "is", "powerful"]

sentence = " ".join(words)

print(sentence)


# ============================================================
# 11. FIND()
# ============================================================

print("\n===== FIND =====")

text = "Python Programming"

position = text.find("Programming")

print("Position:", position)


# ============================================================
# 12. COUNT()
# ============================================================

print("\n===== COUNT =====")

text = "banana"

print("Number of 'a':", text.count("a"))


# ============================================================
# 13. STARTSWITH() AND ENDSWITH()
# ============================================================

print("\n===== STARTSWITH / ENDSWITH =====")

text = "Python Programming"

print(text.startswith("Python"))
print(text.endswith("Programming"))


# ============================================================
# 14. MEMBERSHIP OPERATORS
# ============================================================

print("\n===== MEMBERSHIP OPERATORS =====")

text = "Python Programming"

print("Python" in text)
print("Java" in text)

print("Java" not in text)


# ============================================================
# 15. STRING FORMATTING - f STRING
# ============================================================

print("\n===== F-STRING =====")

name = "Sagar"
age = 20
cgpa = 8.0

print(f"My name is {name}.")
print(f"I am {age} years old.")
print(f"My CGPA is {cgpa}.")


# ============================================================
# 16. ESCAPE CHARACTERS
# ============================================================

print("\n===== ESCAPE CHARACTERS =====")

print("Hello\nWorld")

print("Python\tProgramming")

print("He said, \"Python is easy.\"")


# ============================================================
# 17. CHECKING STRING CONTENT
# ============================================================

print("\n===== STRING CHECKING =====")

text = "Python123"

print("Is alphabetic:", text.isalpha())
print("Is numeric:", text.isnumeric())
print("Is alphanumeric:", text.isalnum())


# ============================================================
# 18. CASE CONVERSION
# ============================================================

print("\n===== CASE CONVERSION =====")

text = "Python Programming"

print(text.upper())
print(text.lower())
print(text.swapcase())


# ============================================================
# 19. PRACTICAL EXAMPLE - NAME FORMATTER
# ============================================================

print("\n===== NAME FORMATTER =====")

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

full_name = first_name.strip().title() + " " + last_name.strip().title()

print("Formatted Name:", full_name)


# ============================================================
# 20. PRACTICAL EXAMPLE - COUNT VOWELS
# ============================================================

print("\n===== COUNT VOWELS =====")

text = input("Enter a string: ")

vowels = "aeiou"
count = 0

for character in text.lower():

    if character in vowels:
        count += 1

print("Number of vowels:", count)


# ============================================================
# IMPORTANT NOTES
# ============================================================

"""
IMPORTANT NOTES:

1. Strings are immutable.

2. Indexing starts from 0.

3. Negative indexing starts from -1.

4. Slicing follows:
       string[start:stop:step]

5. The stop index is excluded.

6. Strings can be concatenated using +.

7. Strings can be repeated using *.

8. len() returns the number of characters.

9. upper(), lower(), title() and capitalize()
   are useful for changing string case.

10. strip() removes leading and trailing whitespace.

11. split() converts a string into a list.

12. join() combines elements into a string.

13. Strings support membership operators:
       in
       not in

14. Strings are immutable, so methods such as
    replace() return a new string instead of
    modifying the original string.

15. f-strings provide an easy way to format strings.
"""


# ============================================================
# PRACTICE QUESTIONS
# ============================================================

"""
PRACTICE:

1. Take a string from the user and print its length.

2. Take a string and print its first and last character.

3. Reverse a string using slicing.

4. Count the number of vowels in a string.

5. Count the number of spaces in a string.

6. Convert a string to uppercase and lowercase.

7. Check whether a given word exists inside a sentence.

8. Replace a word in a sentence with another word.

9. Count how many times a particular character appears
   in a string.

10. Check whether a string is a palindrome.
"""