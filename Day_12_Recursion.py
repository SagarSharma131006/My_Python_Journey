# ============================================================
# PYTHON JOURNEY - DAY 12
# Topic: Recursion
# ============================================================

"""
Today I learned about Recursion.

Recursion means a function calls itself.

A recursive function normally has two important parts:

1. Base Case
   -> Condition that stops the recursion.

2. Recursive Case
   -> Function calls itself with a smaller/simpler input.

Topics covered:

1. Basic recursion
2. Base case
3. Recursive case
4. Countdown
5. Count up
6. Factorial
7. Sum of numbers
8. Power of a number
9. Fibonacci
10. Reverse a string
11. Sum of list elements
12. Important notes
"""


# ============================================================
# 1. BASIC RECURSION
# ============================================================

print("===== BASIC RECURSION =====")


def countdown(n):

    if n == 0:
        print("Done!")
        return

    print(n)

    countdown(n - 1)


countdown(5)


# ============================================================
# 2. COUNT UP USING RECURSION
# ============================================================

print("\n===== COUNT UP =====")


def count_up(n):

    if n == 0:
        return

    count_up(n - 1)

    print(n)


count_up(5)


# ============================================================
# 3. FACTORIAL USING RECURSION
# ============================================================

print("\n===== FACTORIAL =====")


def factorial(n):

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


print("Factorial of 5:", factorial(5))


# ============================================================
# 4. SUM OF FIRST N NUMBERS
# ============================================================

print("\n===== SUM OF NUMBERS =====")


def sum_numbers(n):

    if n == 0:
        return 0

    return n + sum_numbers(n - 1)


print("Sum:", sum_numbers(5))


# ============================================================
# 5. POWER OF A NUMBER
# ============================================================

print("\n===== POWER =====")


def power(base, exponent):

    if exponent == 0:
        return 1

    return base * power(base, exponent - 1)


print("2^5 =", power(2, 5))


# ============================================================
# 6. FIBONACCI
# ============================================================

print("\n===== FIBONACCI =====")


def fibonacci(n):

    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(8):
    print(fibonacci(i), end=" ")


# ============================================================
# 7. REVERSE A STRING
# ============================================================

print("\n\n===== REVERSE STRING =====")


def reverse_string(text):

    if len(text) == 0:
        return ""

    return reverse_string(text[1:]) + text[0]


text = "Python"

print("Original:", text)
print("Reversed:", reverse_string(text))


# ============================================================
# 8. SUM OF LIST ELEMENTS
# ============================================================

print("\n===== SUM OF LIST =====")


def list_sum(numbers, index=0):

    if index == len(numbers):
        return 0

    return numbers[index] + list_sum(numbers, index + 1)


numbers = [10, 20, 30, 40, 50]

print("List:", numbers)
print("Sum:", list_sum(numbers))


# ============================================================
# 9. FIND MAXIMUM USING RECURSION
# ============================================================

print("\n===== MAXIMUM =====")


def find_max(numbers, index=0):

    if index == len(numbers) - 1:
        return numbers[index]

    maximum = find_max(numbers, index + 1)

    if numbers[index] > maximum:
        return numbers[index]

    return maximum


numbers = [10, 45, 23, 67, 12]

print("Numbers:", numbers)
print("Maximum:", find_max(numbers))


# ============================================================
# 10. PRINT ARRAY ELEMENTS USING RECURSION
# ============================================================

print("\n===== PRINT LIST =====")


def print_list(numbers, index=0):

    if index == len(numbers):
        return

    print(numbers[index])

    print_list(numbers, index + 1)


numbers = [10, 20, 30, 40, 50]

print_list(numbers)


# ============================================================
# IMPORTANT NOTES
# ============================================================

"""
IMPORTANT NOTES:

1. Recursion means a function calling itself.

2. Every recursive function should have a BASE CASE.

3. The base case stops the recursion.

4. Without a proper base case, recursion can continue
   indefinitely and cause an error.

5. General structure:

       def function():

           if base_condition:
               return

           function()


6. Example:

       def countdown(n):

           if n == 0:
               return

           print(n)

           countdown(n - 1)


7. Recursive problems usually break a large problem
   into smaller versions of the same problem.

8. Factorial:

       5! = 5 × 4 × 3 × 2 × 1


9. Recursive factorial:

       factorial(5)
       = 5 * factorial(4)
       = 5 * 4 * factorial(3)
       = 5 * 4 * 3 * factorial(2)
       = 5 * 4 * 3 * 2 * factorial(1)
       = 120


10. Recursion uses the function call stack, so recursive
    solutions can require additional memory.

11. Recursion is very important in DSA.

    It will be useful later in:

       Trees
       Graphs
       Backtracking
       Divide and Conquer
       Dynamic Programming


12. Recursion is not always the most efficient solution.
    Sometimes an iterative solution using loops is better.

13. The important thing is to understand:

       Base Case
            ↓
       Recursive Case
            ↓
       Smaller Problem
            ↓
       Base Case


------------------------------------------------------------
WHAT I LEARNED TODAY
------------------------------------------------------------

Before today, I mostly used loops when I wanted to
repeat something.

Today I learned that a function can call itself and
solve a problem by reducing it into smaller problems.

The most important thing I want to remember is:

    "Every recursion needs a clear stopping condition."
"""


# ============================================================
# PRACTICE QUESTIONS
# ============================================================

"""
PRACTICE QUESTIONS:

1. Create a recursive function to print numbers from
   1 to 10.

2. Create a recursive function to print numbers from
   10 to 1.

3. Create a recursive function to calculate the factorial
   of a number.

4. Create a recursive function to calculate the sum of
   numbers from 1 to n.

5. Create a recursive function to calculate a number's
   power.

6. Create a recursive function to find the sum of all
   elements in a list.

7. Create a recursive function to find the largest
   element in a list.

8. Create a recursive function to reverse a string.

9. Create a recursive function to count the number of
   digits in a number.

10. Create a recursive function to calculate the nth
    Fibonacci number.
"""