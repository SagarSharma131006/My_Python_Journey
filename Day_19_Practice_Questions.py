# Day 19 - Practice Questions


# Q1. Create an iterator from a list
numbers = [10, 20, 30, 40, 50]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))


# Q2. Print all elements using iterator
numbers = [1, 2, 3, 4, 5]

iterator = iter(numbers)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break


# Q3. Create a generator for numbers 1 to 10
def numbers_generator():
    for i in range(1, 11):
        yield i


for number in numbers_generator():
    print(number)


# Q4. Create a generator for even numbers
def even_numbers(n):
    for i in range(2, n + 1, 2):
        yield i


for number in even_numbers(20):
    print(number)


# Q5. Create a generator for squares
def squares(n):
    for i in range(1, n + 1):
        yield i * i


for value in squares(10):
    print(value)


# Q6. Generator for odd numbers
def odd_numbers(n):
    for i in range(1, n + 1, 2):
        yield i


for number in odd_numbers(20):
    print(number)


# Q7. Generator for numbers divisible by 5
def divisible_by_five(n):
    for i in range(1, n + 1):
        if i % 5 == 0:
            yield i


for number in divisible_by_five(50):
    print(number)


# Q8. Generator for list elements
def list_generator(items):
    for item in items:
        yield item


names = ["Sagar", "Rahul", "Aman", "Rohit"]

for name in list_generator(names):
    print(name)


# Q9. Generator expression for cubes
cubes = (x ** 3 for x in range(1, 6))

for cube in cubes:
    print(cube)


# Q10. Generator for Fibonacci numbers
def fibonacci(n):

    a = 0
    b = 1

    for _ in range(n):
        yield a

        a, b = b, a + b


for number in fibonacci(10):
    print(number)