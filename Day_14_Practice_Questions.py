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

# Q1. Handle ZeroDivisionError

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter valid numbers.")



# Q2. Handle ValueError

try:
    number = int(input("Enter an integer: "))

    print("You entered:", number)

except ValueError:
    print("Error: Please enter a valid integer.")




# Q3. Handle IndexError

numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter index: "))

    print("Element:", numbers[index])

except IndexError:
    print("Error: Index does not exist.")

except ValueError:
    print("Error: Please enter a valid index.")



# Q4. Handle KeyError

student = {
    "name": "Sagar",
    "age": 20,
    "branch": "CSE"
}

try:
    key = input("Enter key: ")

    print("Value:", student[key])

except KeyError:
    print("Error: This key does not exist.")




# Q5. Handle TypeError

try:
    num1 = "10"
    num2 = 20

    result = num1 + num2

    print("Result:", result)

except TypeError:
    print("Error: Cannot perform operation on these data types.")




# Q6. try, except and finally

try:
    number = int(input("Enter a number: "))

    result = 100 / number

    print("Result:", result)

except ValueError:
    print("Error: Please enter a valid number.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

finally:
    print("Program execution completed.")




# Q7. try, except and else

try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Error: Invalid input.")

else:
    print("You entered:", number)
    print("No error occurred.")



# Q8. Raise ValueError

def check_age(age):

    if age < 0:
        raise ValueError("Age cannot be negative.")

    print("Valid age:", age)


try:
    age = int(input("Enter your age: "))

    check_age(age)

except ValueError as error:
    print("Error:", error)




# Q9. Calculator with Exception Handling

try:

    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":

        result = num1 + num2

    elif operator == "-":

        result = num1 - num2

    elif operator == "*":

        result = num1 * num2

    elif operator == "/":

        result = num1 / num2

    else:

        print("Invalid operator.")
        result = None

    if result is not None:
        print("Result:", result)


except ValueError:

    print("Error: Please enter valid numbers.")

except ZeroDivisionError:

    print("Error: Cannot divide by zero.")



# Q10. Handle FileNotFoundError

try:

    file = open("student.txt", "r")

    content = file.read()

    print(content)

    file.close()

except FileNotFoundError:

    print("Error: File not found.")

# Better approach

try:

    with open("student.txt", "r") as file:

        content = file.read()

        print(content)

except FileNotFoundError:

    print("Error: File not found.")



