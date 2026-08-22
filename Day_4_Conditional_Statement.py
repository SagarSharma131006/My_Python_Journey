# ============================================================
# PYTHON JOURNEY - DAY 04
# Topic: Conditional Statements
# ============================================================

"""
DESCRIPTION:

Conditional statements allow a Python program to make
decisions based on whether a condition is True or False.

Python provides:

1. if statement
2. if-else statement
3. if-elif-else statement
4. Nested if statements
5. Multiple conditions using logical operators
6. Conditional expressions (Ternary Operator)
"""


# ============================================================
# 1. BASIC if STATEMENT
# ============================================================

print("===== BASIC IF STATEMENT =====")

age = 20

if age >= 18:
    print("You are an adult.")


# ============================================================
# 2. if-else STATEMENT
# ============================================================

print("\n===== IF-ELSE STATEMENT =====")

age = 16

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# ============================================================
# 3. if-elif-else STATEMENT
# ============================================================

print("\n===== IF-ELIF-ELSE STATEMENT =====")

marks = 78

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")


# ============================================================
# 4. TAKING USER INPUT
# ============================================================

print("\n===== USER INPUT =====")

# Uncomment these lines to run:

# age = int(input("Enter your age: "))

# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")


# ============================================================
# 5. CHECK EVEN OR ODD
# ============================================================

print("\n===== EVEN OR ODD =====")

number = 15

if number % 2 == 0:
    print(number, "is even.")
else:
    print(number, "is odd.")


# ============================================================
# 6. POSITIVE, NEGATIVE OR ZERO
# ============================================================

print("\n===== POSITIVE / NEGATIVE / ZERO =====")

number = -10

if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")


# ============================================================
# 7. MULTIPLE CONDITIONS USING AND
# ============================================================

print("\n===== AND OPERATOR =====")

age = 22
has_license = True

if age >= 18 and has_license:
    print("You can drive.")
else:
    print("You cannot drive.")


# ============================================================
# 8. MULTIPLE CONDITIONS USING OR
# ============================================================

print("\n===== OR OPERATOR =====")

day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("It's the weekend.")
else:
    print("It's a working day.")


# ============================================================
# 9. NOT OPERATOR
# ============================================================

print("\n===== NOT OPERATOR =====")

is_raining = False

if not is_raining:
    print("You can go outside.")


# ============================================================
# 10. NESTED IF STATEMENT
# ============================================================

print("\n===== NESTED IF =====")

age = 20
has_id = True

if age >= 18:

    if has_id:
        print("Entry allowed.")
    else:
        print("Please show your ID.")

else:
    print("Entry not allowed.")


# ============================================================
# 11. COMPARING STRINGS
# ============================================================

print("\n===== STRING COMPARISON =====")

username = "Sagar"

if username == "Sagar":
    print("Welcome Sagar!")
else:
    print("Unknown user.")


# ============================================================
# 12. LOGIN EXAMPLE
# ============================================================

print("\n===== LOGIN SYSTEM =====")

correct_username = "sagar"
correct_password = "python123"

username = "sagar"
password = "python123"

if username == correct_username and password == correct_password:
    print("Login successful.")
else:
    print("Invalid username or password.")


# ============================================================
# 13. TERNARY / CONDITIONAL EXPRESSION
# ============================================================

print("\n===== TERNARY OPERATOR =====")

age = 20

status = "Adult" if age >= 18 else "Minor"

print(status)


# ============================================================
# 14. FIND LARGER NUMBER
# ============================================================

print("\n===== LARGER NUMBER =====")

a = 25
b = 40

if a > b:
    print(a, "is greater.")
elif b > a:
    print(b, "is greater.")
else:
    print("Both numbers are equal.")


# ============================================================
# 15. PRACTICAL EXAMPLE - RESULT SYSTEM
# ============================================================

print("\n===== RESULT SYSTEM =====")

marks = 72

if marks >= 90:
    result = "Excellent"
elif marks >= 75:
    result = "Very Good"
elif marks >= 60:
    result = "Good"
elif marks >= 40:
    result = "Pass"
else:
    result = "Fail"

print("Marks:", marks)
print("Result:", result)


# ============================================================
# IMPORTANT NOTES
# ============================================================

"""
IMPORTANT NOTES:

1. Conditional statements are used to make decisions
   in a program.

2. The basic syntax is:

   if condition:
       statement


3. Python uses INDENTATION to define a block.

   Correct:

   if age >= 18:
       print("Adult")


4. if-else is used when there are two possible outcomes.

   if condition:
       statement
   else:
       statement


5. elif is used when multiple conditions need to be checked.

   if condition:
       statement
   elif condition:
       statement
   else:
       statement


6. Conditions normally return True or False.

   Example:

   10 > 5

   Result:

   True


7. Logical operators can combine conditions:

   and
   or
   not


8. Nested if means an if statement inside another
   if statement.


9. Python supports a conditional expression:

   value_if_true if condition else value_if_false


10. The colon ':' is required after:

    if
    elif
    else
"""


# ============================================================
# PRACTICE QUESTIONS
# ============================================================

"""
PRACTICE:

1. Take a number from the user and check whether it is:
   - Positive
   - Negative
   - Zero

2. Take a number and check whether it is even or odd.

3. Take a person's age and check whether they are:
   - Child
   - Teenager
   - Adult
   - Senior Citizen

4. Take three numbers and find the largest number.

5. Take marks from the user and assign grades:
   90+  -> A+
   80+  -> A
   70+  -> B
   60+  -> C
   40+  -> D
   Below 40 -> F

6. Create a simple login system using username
   and password.

7. Check whether a year is a leap year.

8. Take a person's age and whether they have a
   driving license. Decide whether they can drive.

9. Create a simple calculator using if-elif-else.

10. Check whether a number is divisible by both
    3 and 5.
"""