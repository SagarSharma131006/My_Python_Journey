"""
Practice:
1. Use regex to check whether the word "Python" exists in a string.

2. Find all numbers present in a string.

3. Find all words starting with the letter "A".

4. Find all email addresses from a given text.

5. Find all 10-digit phone numbers from a string.

6. Replace every occurrence of "Python" with "Programming".

7. Count how many times "Python" appears in a string using regex.

8. Check whether a given string contains only digits.

9. Check whether a given string contains only alphabets.

10. Extract all hashtags from a sentence.
"""

# 1.
import re

text = "I am learning Python."

result = re.search(r"Python", text)

if result:
    print("Python exists in the string.")
else:
    print("Python does not exist.")



# 2.
import re

text = "I have 2 apples, 5 bananas and 10 oranges."

numbers = re.findall(r"\d+", text)

print("Numbers:", numbers)




# 3.
import re

text = "Apple is an Amazing fruit and An apple a day is healthy."

words = re.findall(r"\bA\w*", text)

print("Words starting with A:", words)




# 4.
import re

text = """
Contact us at student@gmail.com
or support@yahoo.com
for more information.
"""

emails = re.findall(r"[\w\.-]+@[\w\.-]+\.\w+", text)

print("Email addresses:")

for email in emails:
    print(email)




# 5.
import re

text = "Contact me at 9876543210 or 8765432109."

phone_numbers = re.findall(r"\b\d{10}\b", text)

print("Phone Numbers:", phone_numbers)



# 6.
import re

text = "Python is easy. I love Python. Python is powerful."

new_text = re.sub(r"Python", "Programming", text)

print(new_text)




# 7.
import re

text = "Python is easy. Python is powerful. I am learning Python."

matches = re.findall(r"Python", text)

print("Python appears", len(matches), "times.")





# 8.
import re

text = "123456"

if re.fullmatch(r"\d+", text):
    print("The string contains only digits.")
else:
    print("The string does not contain only digits.")




# 9.
import re

text = "Python"

if re.fullmatch(r"[A-Za-z]+", text):
    print("The string contains only alphabets.")
else:
    print("The string does not contain only alphabets.")



# 10.
import re

text = "I am learning #Python and #Programming. Today I completed #Day16."

hashtags = re.findall(r"#\w+", text)

print("Hashtags:", hashtags)


