"""
DAY-3
PRACTICE:

1. Take your name as input and print:
   "Hello, <name>!"

2. Take two numbers from the user and print:
   - Sum
   - Difference
   - Product
   - Division

3. Take a student's:
   - Name
   - Age
   - CGPA

   Then display them using an f-string.

4. Take length and width of a rectangle
   and calculate its area.

5. Take temperature in Celsius and convert it
   into Fahrenheit.

   Formula:

   Fahrenheit = (Celsius * 9/5) + 32

6. Take three numbers in one line and calculate
   their average.

7. Create a simple bill generator that takes:
   - Product name
   - Price
   - Quantity

   Then calculate the total price.
"""



# 1. Greeting

name = input("Enter your name: ")

print("Hello,", name + "!")


# 2. Arithmetic Operations

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Division:", num1 / num2)


# 3. Student Information

name = input("Enter your name: ")
age = int(input("Enter your age: "))
cgpa = float(input("Enter your CGPA: "))

print(f"Name: {name}")
print(f"Age: {age}")
print(f"CGPA: {cgpa}")


# 4. Area of Rectangle

length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width

print(f"Area of rectangle: {area}")


# 5. Celsius to Fahrenheit

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print(f"Temperature in Fahrenheit: {fahrenheit}")


# 6. Average of Three Numbers

num1, num2, num3 = map(float, input("Enter three numbers: ").split())

average = (num1 + num2 + num3) / 3

print(f"Average: {average}")


# 7. Simple Bill Generator

product_name = input("Enter product name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

total_price = price * quantity

print("\n----- BILL -----")
print(f"Product: {product_name}")
print(f"Price: ₹{price}")
print(f"Quantity: {quantity}")
print(f"Total Price: ₹{total_price}")