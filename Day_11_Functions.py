# ============================================================
# PYTHON JOURNEY - DAY 11
# Topic: Functions
# ============================================================

"""
Today I learned about Functions in Python.

A function is a reusable block of code that performs
a specific task.

Instead of writing the same code multiple times,
we can write it once inside a function and call it
whenever we need it.

Topics covered:

1. Creating a function
2. Calling a function
3. Parameters
4. Arguments
5. Return statement
6. Default arguments
7. Keyword arguments
8. Multiple parameters
9. *args
10. **kwargs
11. Local and global variables
12. Function with conditions
13. Function with loops
14. Practical examples
"""


# ============================================================
# 1. SIMPLE FUNCTION
# ============================================================

print("===== SIMPLE FUNCTION =====")


def greet():
    print("Hello! Welcome to my Python Journey.")


greet()


# ============================================================
# 2. FUNCTION WITH PARAMETERS
# ============================================================

print("\n===== FUNCTION WITH PARAMETERS =====")


def greet_user(name):
    print("Hello", name)


greet_user("Sagar")
greet_user("Rahul")


# ============================================================
# 3. FUNCTION WITH MULTIPLE PARAMETERS
# ============================================================

print("\n===== MULTIPLE PARAMETERS =====")


def introduce(name, age, branch):
    print("Name:", name)
    print("Age:", age)
    print("Branch:", branch)


introduce("Sagar", 20, "CSE")


# ============================================================
# 4. FUNCTION WITH RETURN
# ============================================================

print("\n===== RETURN STATEMENT =====")


def add(a, b):
    return a + b


result = add(10, 20)

print("Sum:", result)


# ============================================================
# 5. DIFFERENCE BETWEEN PRINT AND RETURN
# ============================================================

print("\n===== PRINT VS RETURN =====")


def print_sum(a, b):
    print(a + b)


def return_sum(a, b):
    return a + b


print_sum(5, 10)

result = return_sum(5, 10)

print("Returned value:", result)


# ============================================================
# 6. FUNCTION FOR SQUARE
# ============================================================

print("\n===== SQUARE =====")


def square(number):
    return number ** 2


print("Square:", square(5))


# ============================================================
# 7. FUNCTION FOR EVEN / ODD
# ============================================================

print("\n===== EVEN OR ODD =====")


def check_even_odd(number):

    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(check_even_odd(10))
print(check_even_odd(7))


# ============================================================
# 8. DEFAULT ARGUMENT
# ============================================================

print("\n===== DEFAULT ARGUMENT =====")


def welcome(name="User"):
    print("Welcome", name)


welcome("Sagar")
welcome()


# ============================================================
# 9. KEYWORD ARGUMENTS
# ============================================================

print("\n===== KEYWORD ARGUMENTS =====")


def student_info(name, age, branch):
    print("Name:", name)
    print("Age:", age)
    print("Branch:", branch)


student_info(
    branch="CSE",
    name="Sagar",
    age=20
)


# ============================================================
# 10. FUNCTION WITH LIST
# ============================================================

print("\n===== FUNCTION WITH LIST =====")


def calculate_sum(numbers):

    total = 0

    for number in numbers:
        total += number

    return total


numbers = [10, 20, 30, 40, 50]

print("Sum:", calculate_sum(numbers))


# ============================================================
# 11. FIND MAXIMUM USING FUNCTION
# ============================================================

print("\n===== MAXIMUM =====")


def find_max(numbers):

    maximum = numbers[0]

    for number in numbers:

        if number > maximum:
            maximum = number

    return maximum


numbers = [10, 45, 23, 67, 12]

print("Maximum:", find_max(numbers))


# ============================================================
# 12. *args
# ============================================================

print("\n===== *args =====")


def add_numbers(*numbers):

    total = 0

    for number in numbers:
        total += number

    return total


print(add_numbers(10, 20))
print(add_numbers(10, 20, 30))
print(add_numbers(1, 2, 3, 4, 5))


# ============================================================
# 13. **kwargs
# ============================================================

print("\n===== **kwargs =====")


def display_info(**details):

    for key, value in details.items():
        print(key, ":", value)


display_info(
    name="Sagar",
    age=20,
    branch="CSE"
)


# ============================================================
# 14. LOCAL VARIABLE
# ============================================================

print("\n===== LOCAL VARIABLE =====")


def my_function():

    message = "This is a local variable"

    print(message)


my_function()


# ============================================================
# 15. GLOBAL VARIABLE
# ============================================================

print("\n===== GLOBAL VARIABLE =====")


message = "This is a global variable"


def show_message():

    print(message)


show_message()


# ============================================================
# 16. FUNCTION WITH LOOP
# ============================================================

print("\n===== FUNCTION WITH LOOP =====")


def print_numbers(n):

    for i in range(1, n + 1):
        print(i)


print_numbers(5)


# ============================================================
# 17. FUNCTION FOR FACTORIAL
# ============================================================

print("\n===== FACTORIAL =====")


def factorial(n):

    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


print("Factorial:", factorial(5))


# ============================================================
# 18. FUNCTION FOR AVERAGE
# ============================================================

print("\n===== AVERAGE =====")


def calculate_average(numbers):

    total = sum(numbers)

    average = total / len(numbers)

    return average


marks = [85, 90, 78, 92, 88]

print("Average:", calculate_average(marks))


# ============================================================
# 19. FUNCTION RETURNING MULTIPLE VALUES
# ============================================================

print("\n===== MULTIPLE RETURN VALUES =====")


def calculate(a, b):

    addition = a + b
    subtraction = a - b
    multiplication = a * b

    return addition, subtraction, multiplication


result = calculate(10, 5)

print("Addition:", result[0])
print("Subtraction:", result[1])
print("Multiplication:", result[2])


# ============================================================
# 20. PRACTICAL EXAMPLE
# ============================================================

print("\n===== PRACTICAL EXAMPLE =====")


def calculate_percentage(marks):

    total = sum(marks)

    percentage = total / len(marks)

    return percentage


student_marks = [85, 90, 88, 92, 95]

percentage = calculate_percentage(student_marks)

print("Marks:", student_marks)
print("Percentage:", percentage)


# ============================================================
# IMPORTANT NOTES
# ============================================================

"""
IMPORTANT NOTES:

1. A function is a reusable block of code.

2. Function syntax:

       def function_name():
           code


3. Calling a function:

       function_name()


4. Parameters are variables written when defining
   the function.

       def greet(name):


5. Arguments are the actual values passed to the function.

       greet("Sagar")


6. return sends a value back from the function.

7. print() displays something on the screen.

8. return and print() are NOT the same.

9. A function can have multiple parameters.

10. Default arguments provide a value if the
    argument is not supplied.

11. Keyword arguments allow us to specify the
    parameter name.

12. *args allows a function to accept multiple
    positional arguments.

13. **kwargs allows a function to accept multiple
    keyword arguments.

14. Variables created inside a function are generally
    local variables.

15. A variable created outside a function can be
    accessed as a global variable.

16. Functions help make programs:

       Reusable
       Organized
       Easier to understand
       Easier to maintain


IMPORTANT:

Don't just memorize function syntax.

Understand this flow:

       Define
         ↓
       Call
         ↓
       Pass arguments
         ↓
       Execute
         ↓
       Return result
"""


# ============================================================
# PRACTICE QUESTIONS
# ============================================================

"""
PRACTICE QUESTIONS:

1. Create a function that prints your name.

2. Create a function that takes two numbers and
   returns their sum.

3. Create a function that takes a number and returns
   whether it is Even or Odd.

4. Create a function that takes three numbers and
   returns the largest number.

5. Create a function that takes a list and returns
   its sum.

6. Create a function that takes a list and returns
   the largest element.

7. Create a function to calculate the factorial
   of a number.

8. Create a function that takes marks of 5 subjects
   and returns the average.

9. Create a function using *args that calculates
   the sum of any number of values.

10. Create a function using **kwargs that displays
    student information.
"""