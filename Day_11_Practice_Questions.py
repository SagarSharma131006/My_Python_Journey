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

# 1.
def print_name():
    print("Sagar")


print_name()


# 2.
def add_numbers(a, b):
    return a + b


result = add_numbers(10, 20)

print("Sum:", result)




# 3.
def check_even_odd(number):

    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


result = check_even_odd(15)

print(result)



#4.
def find_largest(a, b, c):

    if a >= b and a >= c:
        return a

    elif b >= a and b >= c:
        return b

    else:
        return c


result = find_largest(10, 25, 15)

print("Largest:", result)



# 5.
def calculate_sum(numbers):

    total = 0

    for number in numbers:
        total += number

    return total


numbers = [10, 20, 30, 40, 50]

result = calculate_sum(numbers)

print("Sum:", result)



# 6.
def find_largest(numbers):

    largest = numbers[0]

    for number in numbers:

        if number > largest:
            largest = number

    return largest


numbers = [12, 45, 23, 67, 34]

result = find_largest(numbers)

print("Largest:", result)




# 7.
def factorial(number):

    result = 1

    for i in range(1, number + 1):
        result *= i

    return result


result = factorial(5)

print("Factorial:", result)




# 8.
def calculate_average(marks):

    total = sum(marks)

    average = total / len(marks)

    return average


marks = [85, 90, 78, 92, 88]

result = calculate_average(marks)

print("Average:", result)




# 9.
def add_numbers(*numbers):

    total = 0

    for number in numbers:
        total += number

    return total


print(add_numbers(10, 20))
print(add_numbers(10, 20, 30))
print(add_numbers(1, 2, 3, 4, 5))



# 10.
def student_information(**details):

    for key, value in details.items():
        print(key, ":", value)


student_information(
    name="Sagar",
    age=20,
    branch="CSE",
    cgpa=8.5
)



