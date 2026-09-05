# Day 18 - Object-Oriented Programming (OOP)


# 1. Creating a Class

class Student:
    pass


student1 = Student()

print(student1)


# 2. Constructor and Attributes

class Student:

    def __init__(self, name, age, branch):
        self.name = name
        self.age = age
        self.branch = branch


student1 = Student("Sagar", 20, "CSE AI & ML")

print("\nStudent Information:")
print("Name:", student1.name)
print("Age:", student1.age)
print("Branch:", student1.branch)


# 3. Creating Methods

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)


student1 = Student("Sagar", 20)

print("\nUsing Method:")
student1.display_info()


# 4. Multiple Objects

student1 = Student("Sagar", 20)
student2 = Student("Rahul", 21)

print("\nMultiple Objects:")

student1.display_info()
student2.display_info()


# 5. Class Variable

class Student:

    college = "PIET"

    def __init__(self, name):
        self.name = name


student1 = Student("Sagar")
student2 = Student("Rahul")

print("\nCollege:", student1.college)
print("College:", student2.college)


# 6. Instance Variable

class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


car1 = Car("Toyota", "Fortuner")

print("\nCar Information:")
car1.display()



# 1st Pillar- Encapsulation

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount(5000)

account.deposit(1000)

print(account.get_balance())




# 2nd Pillar - Inheritance
class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):

    def bark(self):
        print("Dog is barking")


dog = Dog()

dog.eat()
dog.bark()




# 3rd Pillar - Polymorphism
class Dog:

    def sound(self):
        print("Dog says: Woof")


class Cat:

    def sound(self):
        print("Cat says: Meow")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()




# 4th Pillar - Abstraction
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Dog says: Woof")


class Cat(Animal):

    def sound(self):
        print("Cat says: Meow")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()




#-----------Complete Example (4 Pillars Together)
from abc import ABC, abstractmethod


# Abstraction
class Animal(ABC):

    def __init__(self, name):
        self.__name = name       # Encapsulation

    def get_name(self):
        return self.__name

    @abstractmethod
    def sound(self):
        pass


# Inheritance
class Dog(Animal):

    # Polymorphism
    def sound(self):
        print(self.get_name(), "says Woof")


class Cat(Animal):

    # Polymorphism
    def sound(self):
        print(self.get_name(), "says Meow")


dog = Dog("Tommy")
cat = Cat("Kitty")

dog.sound()
cat.sound()