"""
DAY-2
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

# 1. Arithmetic Operations

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Floor Division:", num1 // num2)
print("Modulus:", num1 % num2)


# 2. Even or Odd

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# 3. Voting Eligibility

age = int(input("Enter your age: "))

if age >= 18 and age <= 100:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


# 4. Membership Operator

items = ["apple", "banana", "mango", "orange"]

item = input("Enter an item to search: ")

if item in items:
    print("Item exists in the list.")
else:
    print("Item does not exist in the list.")



# 5. Experiment with Operators

print(2 ** 3)
print(10 // 3)
print(10 % 3)


# 6. Logical Operators

x = 10
y = 20

print(x > 5 and y > 15)
print(x > 15 or y > 15)
print(not(x > 15))


# 7. Operator Precedence

print(10 + 5 * 2)
print((10 + 5) * 2)

print(20 - 10 / 2)
print((20 - 10) / 2)

print(2 + 3 ** 2)
print((2 + 3) ** 2)

print(10 > 5 and 20 > 15)
print(10 > 5 or 20 < 15)