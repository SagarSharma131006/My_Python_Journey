"""
PRACTICE:

1. Create a dictionary containing your name, age,
   branch and CGPA. Print each value.

2. Add a new key "city" to the dictionary.

3. Update your CGPA.

4. Delete the age key.

5. Check whether "name" exists in the dictionary.

6. Print all keys, values and key-value pairs.

7. Create a dictionary containing marks of 5 subjects.
   Find:
       - Total marks
       - Average marks
       - Highest marks

8. Create a nested dictionary containing details
   of 3 students.

9. Create a dictionary containing numbers from 1 to 10
   and their squares using dictionary comprehension.

10. Create a dictionary containing numbers from 1 to 10
    and store "Even" or "Odd" as their values.
"""

# Q1. Create a dictionary containing your name, age,
#     branch and CGPA. Print each value.

print("===== Q1 =====")

student = {
    "name": "Sagar",
    "age": 20,
    "branch": "CSE",
    "cgpa": 8.5
}

print("Name:", student["name"])
print("Age:", student["age"])
print("Branch:", student["branch"])
print("CGPA:", student["cgpa"])


# Q2. Add a new key "city" to the dictionary.

print("\n===== Q2 =====")

student["city"] = "Panipat"

print("Updated Dictionary:", student)


# Q3. Update your CGPA.

print("\n===== Q3 =====")

student["cgpa"] = 9.0

print("Updated CGPA:", student["cgpa"])
print("Updated Dictionary:", student)


# Q4. Delete the age key.

print("\n===== Q4 =====")

del student["age"]

print("Dictionary after deleting age:", student)


# Q5. Check whether "name" exists in the dictionary.

print("\n===== Q5 =====")

if "name" in student:
    print("The 'name' key exists in the dictionary.")
else:
    print("The 'name' key does not exist in the dictionary.")


# Q6. Print all keys, values and key-value pairs.

print("\n===== Q6 =====")

print("Keys:")
print(student.keys())

print("\nValues:")
print(student.values())

print("\nKey-Value Pairs:")
print(student.items())


# Q7. Create a dictionary containing marks of 5 subjects.
#     Find:
#       - Total marks
#       - Average marks
#       - Highest marks

print("\n===== Q7 =====")

marks = {
    "Math": 85,
    "Python": 92,
    "C++": 88,
    "DBMS": 90,
    "SQL": 95
}

total_marks = sum(marks.values())
average_marks = total_marks / len(marks)
highest_marks = max(marks.values())

print("Marks:", marks)
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)
print("Highest Marks:", highest_marks)


# Q8. Create a nested dictionary containing details
#     of 3 students.

print("\n===== Q8 =====")

students = {
    "student1": {
        "name": "Sagar",
        "age": 20,
        "branch": "CSE"
    },

    "student2": {
        "name": "Rahul",
        "age": 21,
        "branch": "ECE"
    },

    "student3": {
        "name": "Aman",
        "age": 20,
        "branch": "CSE"
    }
}

print(students)

print("\nStudent 1:")
print("Name:", students["student1"]["name"])
print("Age:", students["student1"]["age"])
print("Branch:", students["student1"]["branch"])

print("\nStudent 2:")
print("Name:", students["student2"]["name"])
print("Age:", students["student2"]["age"])
print("Branch:", students["student2"]["branch"])

print("\nStudent 3:")
print("Name:", students["student3"]["name"])
print("Age:", students["student3"]["age"])
print("Branch:", students["student3"]["branch"])



# Q9. Create a dictionary containing numbers from 1 to 10
#     and their squares using dictionary comprehension.

print("\n===== Q9 =====")

squares = {
    number: number ** 2
    for number in range(1, 11)
}

print("Numbers and their squares:")
print(squares)


# Q10. Create a dictionary containing numbers from 1 to 10
#      and store "Even" or "Odd" as their values.

print("\n===== Q10 =====")

even_odd = {
    number: "Even" if number % 2 == 0 else "Odd"
    for number in range(1, 11)
}

print("Numbers and their type:")
print(even_odd)