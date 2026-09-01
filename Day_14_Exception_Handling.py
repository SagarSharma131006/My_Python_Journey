# ============================================================
# PYTHON JOURNEY - DAY 14
# Topic: Exception Handling
# ============================================================

"""
Today I learned about Exception Handling in Python.

Exceptions are errors that occur while a program is running.

Instead of allowing the program to crash, we can handle
these exceptions using:

    try
    except
    else
    finally

Topics covered:

1. What is an exception?
2. try
3. except
4. Handling specific exceptions
5. Multiple except blocks
6. else
7. finally
8. Raising exceptions
9. ValueError
10. ZeroDivisionError
11. TypeError
12. FileNotFoundError
"""


# ============================================================
# 1. BASIC TRY-EXCEPT
# ============================================================

print("===== BASIC TRY-EXCEPT =====")

try:
    number = int(input("Enter a number: "))
    print("You entered:", number)

except:
    print("Invalid input!")


# ============================================================
# 2. ZERO DIVISION ERROR
# ============================================================

print("\n===== ZERO DIVISION ERROR =====")

try:

    a = 10
    b = 0

    result = a / b

    print(result)

except ZeroDivisionError:
    print("You cannot divide by zero.")


# ============================================================
# 3. VALUE ERROR
# ============================================================

print("\n===== VALUE ERROR =====")

try:

    number = int("hello")

    print(number)

except ValueError:
    print("The value cannot be converted into an integer.")


# ============================================================
# 4. TYPE ERROR
# ============================================================

print("\n===== TYPE ERROR =====")

try:

    result = "10" + 5

    print(result)

except TypeError:
    print("These two data types cannot be combined.")


# ============================================================
# 5. MULTIPLE EXCEPTIONS
# ============================================================

print("\n===== MULTIPLE EXCEPTIONS =====")

try:

    number = int(input("Enter a number: "))

    result = 100 / number

    print("Result:", result)

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("Number cannot be zero.")


# ============================================================
# 6. ELSE
# ============================================================

print("\n===== ELSE =====")

try:

    number = int(input("Enter a number: "))

except ValueError:

    print("Invalid input.")

else:

    print("Valid number:", number)


# ============================================================
# 7. FINALLY
# ============================================================

print("\n===== FINALLY =====")

try:

    number = 10 / 2

    print("Result:", number)

except ZeroDivisionError:

    print("Cannot divide by zero.")

finally:

    print("This block always executes.")


# ============================================================
# 8. TRY + EXCEPT + ELSE + FINALLY
# ============================================================

print("\n===== COMPLETE STRUCTURE =====")

try:

    number = int(input("Enter a number: "))

    result = 100 / number

except ValueError:

    print("Please enter a valid integer.")

except ZeroDivisionError:

    print("Zero is not allowed.")

else:

    print("Result:", result)

finally:

    print("Program execution completed.")


# ============================================================
# 9. ACCESSING EXCEPTION MESSAGE
# ============================================================

print("\n===== EXCEPTION MESSAGE =====")

try:

    number = int("abc")

except ValueError as error:

    print("Error:", error)


# ============================================================
# 10. RAISING AN EXCEPTION
# ============================================================

print("\n===== RAISING EXCEPTION =====")


def check_age(age):

    if age < 0:
        raise ValueError("Age cannot be negative.")

    print("Valid age:", age)


try:

    check_age(20)

except ValueError as error:

    print("Error:", error)


# ============================================================
# 11. PRACTICAL EXAMPLE - DIVISION
# ============================================================

print("\n===== PRACTICAL DIVISION PROGRAM =====")


def divide_numbers(a, b):

    try:

        return a / b

    except ZeroDivisionError:

        return "Cannot divide by zero."


print(divide_numbers(20, 5))
print(divide_numbers(20, 0))


# ============================================================
# 12. PRACTICAL EXAMPLE - MARKS
# ============================================================

print("\n===== PRACTICAL MARKS PROGRAM =====")


try:

    marks = int(input("Enter your marks: "))

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")

    print("Your marks:", marks)

except ValueError as error:

    print("Invalid marks:", error)


# ============================================================
# IMPORTANT NOTES
# ============================================================

"""
IMPORTANT NOTES:

1. An exception is an error that occurs while the
   program is running.

2. try:
   Contains code that might produce an exception.

3. except:
   Handles the exception.

4. else:
   Executes when no exception occurs.

5. finally:
   Executes whether an exception occurs or not.

6. Basic structure:

       try:
           risky_code()

       except:
           handle_error()


7. Better practice is to catch specific exceptions.

   Example:

       except ValueError:
           ...


8. Common exceptions:

       ValueError
       TypeError
       ZeroDivisionError
       IndexError
       KeyError
       FileNotFoundError


9. We can store the error using:

       except ValueError as error:


10. We can manually raise an exception using:

       raise ValueError("message")


11. Exception handling prevents unexpected errors
    from immediately stopping the entire program.


------------------------------------------------------------
WHAT I LEARNED TODAY
------------------------------------------------------------

Today I learned that errors don't always have to
crash the entire program.

Using exception handling, I can anticipate possible
problems and handle them properly.

The basic flow I want to remember is:

        try
         ↓
      Error?
      ↙   ↘
    YES    NO
     ↓      ↓
  except   else
     ↘      ↙
       finally
"""


# ============================================================
# PRACTICE QUESTIONS
# ============================================================

"""
PRACTICE QUESTIONS:

1. Write a program that takes two numbers from the user
   and handles ZeroDivisionError.


2. Take an integer as input and handle ValueError if
   the user enters something other than a number.


3. Create a program that accesses an element from a list
   and handles IndexError.


4. Create a program that accesses a dictionary key
   and handles KeyError.


5. Create a program that adds two values and handles
   TypeError.


6. Use try, except and finally in a program.


7. Use try, except and else in a program.


8. Create a function that checks age.
   Raise ValueError if age is negative.


9. Create a calculator using exception handling for
   invalid input and division by zero.


10. Create a program that opens a file and handles
    FileNotFoundError.
"""