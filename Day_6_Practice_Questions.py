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


# Day 06 - Practice Question 1

text = input("Enter a string: ")

print("Length:", len(text))



# Day 06 - Practice Question 2

text = input("Enter a string: ")

print("First character:", text[0])
print("Last character:", text[-1])



# Day 06 - Practice Question 3

text = input("Enter a string: ")

reverse = text[::-1]

print("Reversed string:", reverse)




# Day 06 - Practice Question 4

text = input("Enter a string: ")

vowels = "aeiou"
count = 0

for character in text.lower():

    if character in vowels:
        count += 1

print("Number of vowels:", count)




# Day 06 - Practice Question 5

text = input("Enter a string: ")

count = 0

for character in text:

    if character == " ":
        count += 1

print("Number of spaces:", count)



# Day 06 - Practice Question 6

text = input("Enter a string: ")

print("Uppercase:", text.upper())
print("Lowercase:", text.lower())



# Day 06 - Practice Question 7

sentence = input("Enter a sentence: ")
word = input("Enter the word to search: ")

if word.lower() in sentence.lower():
    print("Word exists in the sentence.")
else:
    print("Word does not exist in the sentence.")




# Day 06 - Practice Question 8

sentence = input("Enter a sentence: ")
old_word = input("Enter the word to replace: ")
new_word = input("Enter the new word: ")

new_sentence = sentence.replace(old_word, new_word)

print("Updated sentence:", new_sentence)



# Day 06 - Practice Question 9

text = input("Enter a string: ")
character = input("Enter the character to count: ")

count = text.count(character)

print(f"'{character}' appears {count} time(s).")


# Alternate Approach to Solve this Question
text = input("Enter a string: ")
character = input("Enter the character to count: ")

count = 0

for ch in text:

    if ch == character:
        count += 1

print("Count:", count)





# Day 06 - Practice Question 10

text = input("Enter a string: ")

reverse = text[::-1]

if text == reverse:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")



   