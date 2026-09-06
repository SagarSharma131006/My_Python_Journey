# Day 19 - Iterators and Generators


# -------------------------------
# 1. Iterable and Iterator
# -------------------------------

numbers = [10, 20, 30, 40, 50]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))


# -------------------------------
# 2. Using next()
# -------------------------------

numbers = [1, 2, 3]

iterator = iter(numbers)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break


# -------------------------------
# 3. Custom Iterator
# -------------------------------

class Count:

    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):

        if self.current <= self.end:
            value = self.current
            self.current += 1
            return value

        raise StopIteration


counter = Count(1, 5)

for number in counter:
    print(number)


# -------------------------------
# 4. Generator Function
# -------------------------------

def count_numbers(n):

    for i in range(1, n + 1):
        yield i


for number in count_numbers(5):
    print(number)


# -------------------------------
# 5. Generator with Squares
# -------------------------------

def square_generator(n):

    for i in range(1, n + 1):
        yield i * i


for square in square_generator(5):
    print(square)


# -------------------------------
# 6. Generator Expression
# -------------------------------

squares = (x * x for x in range(1, 6))

for square in squares:
    print(square)


# -------------------------------
# 7. Infinite Generator
# -------------------------------

def infinite_numbers():

    number = 1

    while True:
        yield number
        number += 1


numbers = infinite_numbers()

print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))