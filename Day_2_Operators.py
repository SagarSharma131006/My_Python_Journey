# ============================================================
# PYTHON JOURNEY - DAY 02
# Topic: Python Operators
# ============================================================

"""
DESCRIPTION:
Operators are special symbols or keywords used to perform
operations on values and variables.

Python provides different types of operators such as:

1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Identity Operators
6. Membership Operators
7. Bitwise Operators
"""


# ============================================================
# 1. ARITHMETIC OPERATORS
# ============================================================

a = 10
b = 3

print("===== ARITHMETIC OPERATORS =====")

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)


# ============================================================
# 2. ASSIGNMENT OPERATORS
# ============================================================

print("\n===== ASSIGNMENT OPERATORS =====")

x = 10
print("Initial value:", x)

x += 5
print("After += 5:", x)

x -= 3
print("After -= 3:", x)

x *= 2
print("After *= 2:", x)

x /= 4
print("After /= 4:", x)

x //= 2
print("After //= 2:", x)

x %= 3
print("After %= 3:", x)

x **= 2
print("After **= 2:", x)


# ============================================================
# 3. COMPARISON OPERATORS
# ============================================================

print("\n===== COMPARISON OPERATORS =====")

p = 10
q = 20

print("p == q:", p == q)
print("p != q:", p != q)
print("p > q:", p > q)
print("p < q:", p < q)
print("p >= q:", p >= q)
print("p <= q:", p <= q)


# ============================================================
# 4. LOGICAL OPERATORS
# ============================================================

print("\n===== LOGICAL OPERATORS =====")

age = 20
has_id = True

print("age >= 18 and has_id:", age >= 18 and has_id)
print("age >= 18 or has_id:", age >= 18 or has_id)
print("not has_id:", not has_id)


# Example

username = "Sagar"
password = "python123"

print("\nLogin Check:")

if username == "Sagar" and password == "python123":
    print("Login Successful")
else:
    print("Invalid Credentials")


# ============================================================
# 5. IDENTITY OPERATORS
# ============================================================

print("\n===== IDENTITY OPERATORS =====")

list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print("list1 is list2:", list1 is list2)
print("list1 is list3:", list1 is list3)

print("list1 is not list3:", list1 is not list3)


# ============================================================
# 6. MEMBERSHIP OPERATORS
# ============================================================

print("\n===== MEMBERSHIP OPERATORS =====")

languages = ["Python", "C++", "Java", "JavaScript"]

print("'Python' in languages:", "Python" in languages)
print("'C' in languages:", "C" in languages)

print("'Ruby' not in languages:", "Ruby" not in languages)


# Membership operators with strings

text = "Python Programming"

print("'Python' in text:", "Python" in text)
print("'Java' in text:", "Java" in text)


# ============================================================
# 7. BITWISE OPERATORS
# ============================================================

print("\n===== BITWISE OPERATORS =====")

a = 5
b = 3

print("a =", a)
print("b =", b)

print("a & b:", a & b)
print("a | b:", a | b)
print("a ^ b:", a ^ b)
print("~a:", ~a)
print("a << 1:", a << 1)
print("a >> 1:", a >> 1)


# ============================================================
# 8. OPERATOR PRECEDENCE
# ============================================================

print("\n===== OPERATOR PRECEDENCE =====")

result1 = 10 + 5 * 2
result2 = (10 + 5) * 2

print("10 + 5 * 2 =", result1)
print("(10 + 5) * 2 =", result2)


# ============================================================
# 9. PRACTICAL EXAMPLE
# ============================================================

print("\n===== PRACTICAL EXAMPLE =====")

marks = 75

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "Fail"

print("Marks:", marks)
print("Grade:", grade)


# ============================================================
# 10. IMPORTANT NOTES
# ============================================================

"""
IMPORTANT NOTES:

1. Arithmetic Operators:
   +   Addition
   -   Subtraction
   *   Multiplication
   /   Division
   //  Floor Division
   %   Modulus
   **  Exponentiation


2. Assignment Operators:
   =   +=   -=   *=   /=   //=   %=   **=


3. Comparison Operators always return True or False:
   ==   Equal
   !=   Not Equal
   >    Greater Than
   <    Less Than
   >=   Greater Than or Equal To
   <=   Less Than or Equal To


4. Logical Operators:
   and
   or
   not


5. Identity Operators:
   is
   is not

   They check whether two variables refer to the
   same object in memory.


6. Membership Operators:
   in
   not in

   They check whether a value exists inside a sequence.


7. Bitwise Operators work at the binary level:
   &    AND
   |    OR
   ^    XOR
   ~    NOT
   <<   Left Shift
   >>   Right Shift


8. Operator precedence determines the order in which
   operations are performed.

   Example:

   10 + 5 * 2

   Multiplication happens first.

   Result = 20


9. Use parentheses when you want to make the order
   of operations clear.

   (10 + 5) * 2
"""


# ============================================================
# PRACTICE QUESTIONS
# ============================================================

"""
PRACTICE:

1. Take two numbers from the user and perform:
   - Addition
   - Subtraction
   - Multiplication
   - Division
   - Floor Division
   - Modulus

2. Check whether a number is even or odd using %.

3. Check whether a person is eligible to vote
   using comparison and logical operators.

4. Check whether a particular item exists in a list
   using the 'in' operator.

5. Experiment with:
       2 ** 3
       10 // 3
       10 % 3

6. Predict the output:

       x = 10
       y = 20

       print(x > 5 and y > 15)
       print(x > 15 or y > 15)
       print(not(x > 15))

7. Try different expressions to understand
   operator precedence.
"""