"""
DAY-5
PRACTICE:

1. Print numbers from 1 to 20 using a for loop.

2. Print all even numbers from 1 to 50.

3. Print all odd numbers from 1 to 50.

4. Take a number from the user and print its multiplication
   table from 1 to 10.

5. Calculate the sum of numbers from 1 to 100.

6. Take a number from the user and calculate its factorial.

7. Count the number of vowels in a string.

8. Reverse a string using a loop.

9. Print this pattern:

   *
   **
   ***
   ****
   *****

10. Create a number guessing game using a while loop.
"""


# Day 05 - Practice Question 1

for i in range(1, 21):
    print(i)



# Day 05 - Practice Question 2

for i in range(1, 51):

    if i % 2 == 0:
        print(i)

# Better Approach
for i in range(2, 51, 2):
    print(i)



# Day 05 - Practice Question 3

for i in range(1, 51):

    if i % 2 != 0:
        print(i)

# Better Approach
for i in range(1, 51, 2):
    print(i)



# Day 05 - Practice Question 4

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{number} × {i} = {number * i}")



# Day 05 - Practice Question 5

total = 0

for i in range(1, 101):
    total += i

print("Sum:", total)



# Day 05 - Practice Question 6

number = int(input("Enter a number: "))

factorial = 1

for i in range(1, number + 1):
    factorial *= i

print(f"Factorial of {number} = {factorial}")




# Day 05 - Practice Question 7

text = input("Enter a string: ")

vowels = "aeiou"
count = 0

for character in text.lower():

    if character in vowels:
        count += 1

print("Number of vowels:", count)



# Day 05 - Practice Question 8

text = input("Enter a string: ")

reverse = ""

for character in text:
    reverse = character + reverse

print("Reversed string:", reverse)



# Day 05 - Practice Question 9

for i in range(1, 6):
    print("*" * i)


# Nested Loop Approach
for i in range(1, 6):

    for j in range(i):
        print("*", end="")

    print()



# Day 05 - Practice Question 10

secret_number = 7

while True:

    guess = int(input("Guess the number: "))

    if guess == secret_number:
        print("Congratulations! You guessed it.")
        break

    elif guess < secret_number:
        print("Too low. Try again.")

    else:
        print("Too high. Try again.")




