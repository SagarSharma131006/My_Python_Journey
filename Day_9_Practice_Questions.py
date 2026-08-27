"""
PRACTICE:

1. Create a set containing 5 numbers and print it.

2. Create a set containing duplicate values and observe
   what happens.

3. Add a new element to a set using add().

4. Remove an element using remove() and discard().

5. Find the union of two sets.

6. Find the intersection of two sets.

7. Find the difference between two sets.

8. Find the symmetric difference between two sets.

9. Check whether one set is a subset of another set.

10. Given a list containing duplicate values, use a set
    to find the unique values.
"""

# Q1 - Create a set

numbers = {10, 20, 30, 40, 50}

print("Set:", numbers)


# Q2 - Duplicate values in a set

numbers = {10, 20, 10, 30, 20, 40, 30}

print("Set:", numbers)



# Q3 - Add an element

numbers = {10, 20, 30, 40}

print("Before:", numbers)

numbers.add(50)

print("After:", numbers)



# Q4 - remove() and discard()

numbers = {10, 20, 30, 40, 50}

numbers.remove(30)

print("After remove():", numbers)

numbers.discard(40)

print("After discard():", numbers)

# discard() does not give an error if the element is absent.



# Q5 - Union

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

union_set = set_a.union(set_b)

print("Set A:", set_a)
print("Set B:", set_b)
print("Union:", union_set)


# Q6 - Intersection

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

intersection_set = set_a.intersection(set_b)

print("Intersection:", intersection_set)

# OR
intersection_set = set_a & set_b



# Q7 - Difference

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

difference_set = set_a.difference(set_b)

print("A - B:", difference_set)

# OR
difference_set = set_a - set_b



# Q8 - Symmetric Difference

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

result = set_a.symmetric_difference(set_b)

print("Symmetric Difference:", result)



# Q9 - Subset

set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}

result = set_a.issubset(set_b)

print("Is A a subset of B?", result)



# Q10 - Remove duplicates

numbers = [10, 20, 10, 30, 20, 40, 30, 10]

print("Original list:", numbers)

unique_numbers = set(numbers)

print("Unique values:", unique_numbers)




#--------------BONUS PRACTICE-------------#
# Given
students_python = {"Sagar", "Rahul", "Aman", "Rohit"}
students_cpp = {"Aman", "Rohit", "Vikas", "Karan"}


# To Find
"""
1. Students learning both Python and C++
2. Students learning only Python
3. Students learning only C++
4. All unique students
"""

students_python = {"Sagar", "Rahul", "Aman", "Rohit"}
students_cpp = {"Aman", "Rohit", "Vikas", "Karan"}

both = students_python & students_cpp
only_python = students_python - students_cpp
only_cpp = students_cpp - students_python
all_students = students_python | students_cpp

print("Learning both:", both)
print("Only Python:", only_python)
print("Only C++:", only_cpp)
print("All students:", all_students)