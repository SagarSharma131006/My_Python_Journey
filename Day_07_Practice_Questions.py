"""
PRACTICE:

1. Create a list of 5 numbers and print the list.

2. Take 5 numbers from the user and store them in a list.

3. Find the largest and smallest number in a list.

4. Calculate the sum and average of numbers in a list.

5. Count how many even and odd numbers are present in a list.

6. Remove duplicate elements from a list.

7. Reverse a list without using reverse().

8. Find the second largest number in a list.

9. Create a list of squares from 1 to 10 using
   list comprehension.

10. Create a nested list representing a 3x3 matrix
    and print its elements.
"""


# Q1 - Create a list of 5 numbers

numbers = [10, 20, 30, 40, 50]

print("List:", numbers)




# Q2 - Take 5 numbers from the user

numbers = []

for i in range(5):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

print("List:", numbers)




# Q3 - Find largest and smallest number

numbers = [45, 12, 78, 23, 9]

largest = max(numbers)
smallest = min(numbers)

print("Largest:", largest)
print("Smallest:", smallest)


# Method-2  {Without using max() and min() functions}
# Q3 - Without max() and min()

numbers = [45, 12, 78, 23, 9]

largest = numbers[0]
smallest = numbers[0]

for number in numbers:

    if number > largest:
        largest = number

    if number < smallest:
        smallest = number

print("Largest:", largest)
print("Smallest:", smallest)



# Q4 - Calculate sum and average

numbers = [10, 20, 30, 40, 50]

total = sum(numbers)
average = total / len(numbers)

print("Sum:", total)
print("Average:", average)



# Q5 - Count even and odd numbers

numbers = [10, 15, 22, 31, 40, 51]

even_count = 0
odd_count = 0

for number in numbers:

    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)



# Q6 - Remove duplicate elements

numbers = [10, 20, 10, 30, 20, 40]

unique_numbers = []

for number in numbers:

    if number not in unique_numbers:
        unique_numbers.append(number)

print("Original list:", numbers)
print("Without duplicates:", unique_numbers)




# Q7 - Reverse using slicing

numbers = [1, 2, 3, 4, 5]

reversed_list = numbers[::-1]

print("Original:", numbers)
print("Reversed:", reversed_list)

# Method-2 Using Loop
# Q7 - Reverse using a loop

numbers = [1, 2, 3, 4, 5]

reversed_list = []

for number in numbers:
    reversed_list.insert(0, number)

print("Original:", numbers)
print("Reversed:", reversed_list)



# Q8 - Find second largest number

numbers = [10, 50, 20, 80, 40]

largest = float("-inf")
second_largest = float("-inf")

for number in numbers:

    if number > largest:
        second_largest = largest
        largest = number

    elif number > second_largest and number != largest:
        second_largest = number

print("Largest:", largest)
print("Second largest:", second_largest)



# Q9 - Squares using list comprehension

numbers = range(1, 11)

squares = [number ** 2 for number in numbers]

print("Squares:", squares)# Q9 - Squares using list comprehension

numbers = range(1, 11)

squares = [number ** 2 for number in numbers]

print("Squares:", squares)




# Q10 - 3x3 Matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:

    for value in row:
        print(value, end=" ")

    print()


