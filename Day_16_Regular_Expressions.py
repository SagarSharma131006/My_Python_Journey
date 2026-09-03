# Day 16 - Regular Expressions

import re


# 1. Search for a pattern
text = "I am learning Python."

result = re.search("Python", text)

if result:
    print("Python found!")
else:
    print("Python not found!")


# 2. Find all matching words
text = "Python is easy. Python is powerful."

matches = re.findall("Python", text)

print("\nMatches:", matches)


# 3. Find all digits
text = "My age is 20 and my semester is 4."

digits = re.findall(r"\d+", text)

print("\nDigits:", digits)


# 4. Find all words starting with P
text = "Python Programming is Powerful"

words = re.findall(r"\bP\w*", text)

print("\nWords starting with P:", words)


# 5. Replace text
text = "I like Java."

new_text = re.sub("Java", "Python", text)

print("\nAfter replacement:", new_text)


# 6. Check email pattern
email = "student@example.com"

pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

if re.match(pattern, email):
    print("\nValid email")
else:
    print("\nInvalid email")


# 7. Extract phone numbers
text = "Contact me at 9876543210 or 8765432109."

phone_numbers = re.findall(r"\b\d{10}\b", text)

print("\nPhone numbers:", phone_numbers)