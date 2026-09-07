import json
import os


FILE_NAME = "students.json"


def save_students(students):

    data = []

    for student in students:
        data.append(student.to_dict())

    with open(FILE_NAME, "w") as file:

        json.dump(data, file, indent=4)


def load_students():

    if not os.path.exists(FILE_NAME):
        return []

    try:

        with open(FILE_NAME, "r") as file:

            data = json.load(file)

            return data

    except (json.JSONDecodeError, FileNotFoundError):

        return []