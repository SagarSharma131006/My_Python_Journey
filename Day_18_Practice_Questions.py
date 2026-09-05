"""1. Create a Student class with name and age attributes.
   Create an object and print the details.

2. Create a Car class with brand and model attributes.
   Create two objects and display their details.

3. Create a Student class with a method display_info()
   that prints student information.

4. Create a Rectangle class with length and width.
   Create a method to calculate area.

5. Create a Circle class with radius.
   Create a method to calculate area.

6. Create a BankAccount class with account holder name
   and balance. Create methods for deposit and withdrawal.

7. Create a Calculator class with methods for:
   addition, subtraction, multiplication and division.

8. Create an Employee class with name, salary and department.
   Create a method to display employee information.

9. Create a class with a class variable "college".
   Create multiple objects and access the class variable.

10. Create a Person class with name and age.
    Create a method that checks whether the person is
    eligible to vote."""



# Question 1

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Sagar", 20)

print("Name:", student1.name)
print("Age:", student1.age)



# Question 2

class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


car1 = Car("Toyota", "Fortuner")
car2 = Car("Mahindra", "Thar")

print("Car 1:")
print("Brand:", car1.brand)
print("Model:", car1.model)

print("\nCar 2:")
print("Brand:", car2.brand)
print("Model:", car2.model)




# Question 3

class Student:

    def __init__(self, name, age, branch):
        self.name = name
        self.age = age
        self.branch = branch

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Branch:", self.branch)


student1 = Student("Sagar", 20, "CSE AI & ML")

student1.display_info()




# Question 4

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


rectangle = Rectangle(10, 5)

area = rectangle.calculate_area()

print("Area of Rectangle:", area)





# Question 5

import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2


circle = Circle(5)

area = circle.calculate_area()

print("Area of Circle:", area)




# Question 6

class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
        print("Current Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
            print("Current Balance:", self.balance)
        else:
            print("Insufficient Balance")


account = BankAccount("Sagar", 10000)

print("Account Holder:", account.account_holder)
print("Initial Balance:", account.balance)

print()

account.deposit(5000)

print()

account.withdraw(3000)

print()

account.withdraw(15000)




# Question 7

class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b


calculator = Calculator()

print("Addition:", calculator.add(10, 5))
print("Subtraction:", calculator.subtract(10, 5))
print("Multiplication:", calculator.multiply(10, 5))
print("Division:", calculator.divide(10, 5))




# Question 8

class Employee:

    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def display_info(self):
        print("Employee Name:", self.name)
        print("Salary:", self.salary)
        print("Department:", self.department)


employee1 = Employee("Sagar", 50000, "AI & ML")

employee1.display_info()





# Question 9

class Student:

    college = "PIET"

    def __init__(self, name, branch):
        self.name = name
        self.branch = branch


student1 = Student("Sagar", "CSE AI & ML")
student2 = Student("Rahul", "CSE")

print("Student 1:")
print("Name:", student1.name)
print("Branch:", student1.branch)
print("College:", student1.college)

print("\nStudent 2:")
print("Name:", student2.name)
print("Branch:", student2.branch)
print("College:", student2.college)




# Question 10

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def check_voting_eligibility(self):
        if self.age >= 18:
            print(self.name, "is eligible to vote.")
        else:
            print(self.name, "is not eligible to vote.")


person1 = Person("Sagar", 20)
person2 = Person("Rahul", 16)

person1.check_voting_eligibility()
person2.check_voting_eligibility()



