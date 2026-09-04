# 1. Create a list of square from 1 to 10
# Question 1

squares = [x ** 2 for x in range(1, 11)]

print(squares)



# 2. Create a list of even numbers from 1 to 20
# Question 2

even_numbers = [x for x in range(1, 21) if x % 2 == 0]

print(even_numbers)


# 3. Create a list of odd numbers from 1 to 20
# Question 3

odd_numbers = [x for x in range(1, 21) if x % 2 != 0]

print(odd_numbers)


# 4. Create a list containing numbers greater than 10
# Given: 
numbers = [5, 12, 8, 20, 3, 15, 7, 25]

# Question 4

numbers = [5, 12, 8, 20, 3, 15, 7, 25]

result = [x for x in numbers if x > 10]

print(result)



# 5. Convert all words in a list to uppercase
# Question 5

words = ["python", "java", "c++", "sql", "machine learning"]

uppercase_words = [word.upper() for word in words]

print(uppercase_words)


# 6. Create a list of the lengths of each word
# Given:
words = ["Python", "Java", "C++", "Machine"]

# Question 6

words = ["Python", "Java", "C++", "Machine"]

lengths = [len(word) for word in words]

print(lengths)



# 7. Replace negative numbers with 0
# Given: 
numbers = [10, -5, 20, -8, 15, -2]

# Question 7

numbers = [10, -5, 20, -8, 15, -2]

result = [x if x >= 0 else 0 for x in numbers]

print(result)


# 8. Create a list containing "Even" or "Odd" for numbers 1 to 10
# Question 8

result = ["Even" if x % 2 == 0 else "Odd" for x in range(1, 11)]

print(result)


# 9. Extract vowels from a string
# Given:
text = "Python Programming"
# Question 9

text = "Python Programming"

vowels = [char for char in text if char.lower() in "aeiou"]

print(vowels)


# 10. Create a list of numbers divisible by both 3 and 5 from 1 to 100
# Question 10

numbers = [x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0]

print(numbers)

