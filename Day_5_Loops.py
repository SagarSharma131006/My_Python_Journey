# ============================================================
# PYTHON JOURNEY - DAY 05
# Topic: Python Loops
# ============================================================

"""
DESCRIPTION:

Loops are used to execute a block of code repeatedly.

Python mainly provides two types of loops:

1. for loop
2. while loop

Loops are useful when we need to repeat a task multiple times
without writing the same code again and again.
"""


# ============================================================
# 1. FOR LOOP
# ============================================================

print("===== FOR LOOP =====")

for i in range(5):
    print(i)


# ============================================================
# 2. RANGE()
# ============================================================

print("\n===== RANGE() =====")

for i in range(1, 6):
    print(i)


# range(start, stop, step)

print("\nNumbers with step 2:")

for i in range(2, 11, 2):
    print(i)


# ============================================================
# 3. ITERATING THROUGH A STRING
# ============================================================

print("\n===== STRING ITERATION =====")

name = "Python"

for character in name:
    print(character)


# ============================================================
# 4. ITERATING THROUGH A LIST
# ============================================================

print("\n===== LIST ITERATION =====")

fruits = ["Apple", "Banana", "Mango", "Orange"]

for fruit in fruits:
    print(fruit)


# ============================================================
# 5. WHILE LOOP
# ============================================================

print("\n===== WHILE LOOP =====")

count = 1

while count <= 5:
    print(count)
    count += 1


# ============================================================
# 6. BREAK
# ============================================================

print("\n===== BREAK =====")

for i in range(1, 11):

    if i == 6:
        break

    print(i)


# ============================================================
# 7. CONTINUE
# ============================================================

print("\n===== CONTINUE =====")

for i in range(1, 11):

    if i == 5:
        continue

    print(i)


# ============================================================
# 8. PASS
# ============================================================

print("\n===== PASS =====")

for i in range(5):

    if i == 2:
        pass

    print(i)


# ============================================================
# 9. NESTED LOOPS
# ============================================================

print("\n===== NESTED LOOPS =====")

for i in range(1, 4):

    for j in range(1, 4):
        print(i, j)


# ============================================================
# 10. MULTIPLICATION TABLE
# ============================================================

print("\n===== MULTIPLICATION TABLE =====")

number = 5

for i in range(1, 11):
    print(f"{number} × {i} = {number * i}")


# ============================================================
# 11. SUM OF NUMBERS
# ============================================================

print("\n===== SUM OF NUMBERS =====")

total = 0

for i in range(1, 11):
    total += i

print("Sum:", total)


# ============================================================
# 12. IMPORTANT NOTES
# ============================================================

"""
IMPORTANT NOTES:

1. for loop is generally used when iterating over a sequence
   or when the number of iterations is known.

2. while loop continues executing as long as its condition
   remains True.

3. range() generates a sequence of numbers.

4. break immediately exits the loop.

5. continue skips the current iteration and moves to the
   next iteration.

6. pass does nothing. It is used as a placeholder.

7. Nested loops mean a loop inside another loop.

8. Be careful with while loops because an incorrect condition
   can create an infinite loop.

Example:

count = 1

while count <= 5:
    print(count)
    count += 1

"""


# ============================================================
# PRACTICE QUESTIONS
# ============================================================

"""
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