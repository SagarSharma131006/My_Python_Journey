"""
Day-4
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


# 1. Positive, Negative or Zero

number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")



# 2. Even or Odd

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")



# 3. Age Classification

age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior Citizen")




# 4. Largest of Three Numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print("Largest number:", num1)
elif num2 >= num1 and num2 >= num3:
    print("Largest number:", num2)
else:
    print("Largest number:", num3)



# 5. Grade Calculator

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 40:
    print("Grade: D")
else:
    print("Grade: F")





# 6. Simple Login System

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Username or Password")




# 7. Leap Year

year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap Year")
elif year % 100 == 0:
    print("Not a Leap Year")
elif year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")




# 8. Driving Eligibility

age = int(input("Enter your age: "))
license = input("Do you have a driving license? (yes/no): ")

if age >= 18 and license == "yes":
    print("You can drive.")
else:
    print("You cannot drive.")




# 9. Simple Calculator

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print("Result:", num1 + num2)

elif operator == "-":
    print("Result:", num1 - num2)

elif operator == "*":
    print("Result:", num1 * num2)

elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero.")

else:
    print("Invalid operator.")




# 10. Divisible by Both 3 and 5

number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 == 0:
    print("The number is divisible by both 3 and 5.")
else:
    print("The number is not divisible by both 3 and 5.")


