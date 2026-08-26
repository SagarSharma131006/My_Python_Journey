"""
PRACTICE:

1. Create a tuple containing 5 numbers and print it.

2. Create a tuple containing your name, age, and branch.
   Print each value using indexing.

3. Find the length of a tuple.

4. Count how many times a particular value occurs
   in a tuple.

5. Find the index of a particular element.

6. Check whether an element exists in a tuple.

7. Create a tuple and unpack its values into variables.

8. Swap two variables using tuple unpacking.

9. Convert a list into a tuple and a tuple into a list.

10. Create a nested tuple representing a 3x3 matrix
    and print the middle element.
"""
# Q1 - Create a tuple

numbers = (10, 20, 30, 40, 50)

print("Tuple:", numbers)


# Q2 - Access tuple elements using indexing

student = ("Sagar", 20, "CSE")

print("Name:", student[0])
print("Age:", student[1])
print("Branch:", student[2])


# Q3 - Find tuple length

numbers = (10, 20, 30, 40, 50)

print("Length:", len(numbers))


# Q4 - Count an element

numbers = (10, 20, 10, 30, 10, 40)

count = numbers.count(10)

print("10 appears:", count, "times")


# Q4 - Count an element

numbers = (10, 20, 10, 30, 10, 40)

count = numbers.count(10)

print("10 appears:", count, "times")


# Q6 - Membership operator

fruits = ("Apple", "Banana", "Mango")

print("Mango exists:", "Mango" in fruits)
print("Orange exists:", "Orange" in fruits)



# Q7 - Tuple unpacking

student = ("Sagar", 20, "CSE")

name, age, branch = student

print("Name:", name)
print("Age:", age)
print("Branch:", branch)



# Q8 - Swap variables

a = 10
b = 20

print("Before:")
print("a =", a)
print("b =", b)

a, b = b, a

print("\nAfter:")
print("a =", a)
print("b =", b)



# Q9 - List to Tuple and Tuple to List

numbers_list = [10, 20, 30, 40]

numbers_tuple = tuple(numbers_list)

print("Tuple:", numbers_tuple)


numbers_tuple = (50, 60, 70, 80)

numbers_list = list(numbers_tuple)

print("List:", numbers_list)



# Q10 - Nested tuple

matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

print("Matrix:")

for row in matrix:

    for value in row:
        print(value, end=" ")

    print()

print("Middle element:", matrix[1][1])


#----------Bonus Challenge Soltuion----------
# Bonus - Tuple operations

numbers = (10, 20, 30, 40, 50)

# 1. Sum
total = sum(numbers)

# 2. Largest
largest = max(numbers)

# 3. Smallest
smallest = min(numbers)

# 4. Average
average = total / len(numbers)

# 5. Reverse
reversed_tuple = numbers[::-1]

print("Tuple:", numbers)
print("Sum:", total)
print("Largest:", largest)
print("Smallest:", smallest)
print("Average:", average)
print("Reversed:", reversed_tuple)