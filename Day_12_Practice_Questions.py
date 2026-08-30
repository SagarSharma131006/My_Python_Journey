"""
PRACTICE QUESTIONS:

1. Create a recursive function to print numbers from
   1 to 10.

2. Create a recursive function to print numbers from
   10 to 1.

3. Create a recursive function to calculate the factorial
   of a number.

4. Create a recursive function to calculate the sum of
   numbers from 1 to n.

5. Create a recursive function to calculate a number's
   power.

6. Create a recursive function to find the sum of all
   elements in a list.

7. Create a recursive function to find the largest
   element in a list.

8. Create a recursive function to reverse a string.

9. Create a recursive function to count the number of
   digits in a number.

10. Create a recursive function to calculate the nth
    Fibonacci number.
"""

# 1.
def print_numbers(n):

    if n > 10:
        return

    print(n)

    print_numbers(n + 1)


print_numbers(1)




# 2.
def print_numbers(n):

    if n < 1:
        return

    print(n)

    print_numbers(n - 1)


print_numbers(10)




#  3.
def factorial(n):

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


number = 5

print("Factorial:", factorial(number))




# 4.
def sum_numbers(n):

    if n == 0:
        return 0

    return n + sum_numbers(n - 1)


number = 5

print("Sum:", sum_numbers(number))




# 5.
def power(base, exponent):

    if exponent == 0:
        return 1

    return base * power(base, exponent - 1)


base = 2
exponent = 5

print("Result:", power(base, exponent))





# 6.
def list_sum(numbers, index=0):

    if index == len(numbers):
        return 0

    return numbers[index] + list_sum(numbers, index + 1)


numbers = [10, 20, 30, 40, 50]

print("Sum:", list_sum(numbers))



# 7.
def find_largest(numbers, index=0):

    if index == len(numbers) - 1:
        return numbers[index]

    largest = find_largest(numbers, index + 1)

    if numbers[index] > largest:
        return numbers[index]

    return largest


numbers = [12, 45, 23, 67, 34]

print("Largest:", find_largest(numbers))




# 8.
def reverse_string(text):

    if len(text) == 0:
        return ""

    return reverse_string(text[1:]) + text[0]


text = "Python"

print("Original:", text)
print("Reversed:", reverse_string(text))




# 9.
def count_digits(number):

    if number == 0:
        return 0

    return 1 + count_digits(number // 10)


number = 12345

print("Number of digits:", count_digits(number))





# 10.
def fibonacci(n):

    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


n = 7

print("Fibonacci number:", fibonacci(n))



