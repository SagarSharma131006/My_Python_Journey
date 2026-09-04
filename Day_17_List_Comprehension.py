# Day 17 - List Comprehensions


# 1. Basic list comprehension

numbers = [1, 2, 3, 4, 5]

squares = [x * x for x in numbers]

print("Squares:", squares)


# 2. Even numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [x for x in numbers if x % 2 == 0]

print("Even numbers:", even_numbers)


# 3. Odd numbers

odd_numbers = [x for x in numbers if x % 2 != 0]

print("Odd numbers:", odd_numbers)


# 4. Numbers greater than 5

numbers = [2, 5, 8, 3, 10, 15, 1]

greater_than_5 = [x for x in numbers if x > 5]

print("Numbers greater than 5:", greater_than_5)


# 5. Convert words to uppercase

words = ["python", "java", "c++", "machine learning"]

uppercase_words = [word.upper() for word in words]

print("Uppercase words:", uppercase_words)


# 6. Create numbers from 1 to 10

numbers = [x for x in range(1, 11)]

print("Numbers:", numbers)


# 7. Squares from 1 to 10

squares = [x ** 2 for x in range(1, 11)]

print("Squares:", squares)


# 8. Even numbers from 1 to 20

even_numbers = [x for x in range(1, 21) if x % 2 == 0]

print("Even numbers:", even_numbers)


# 9. Conditional expression

numbers = [1, 2, 3, 4, 5]

result = ["Even" if x % 2 == 0 else "Odd" for x in numbers]

print("Result:", result)