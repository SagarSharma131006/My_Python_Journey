from student import Student
from file_handler import save_students, load_students


class StudentManager:

    def __init__(self):

        data = load_students()

        self.students = []

        for student_data in data:

            student = Student.from_dict(student_data)

            self.students.append(student)

    # -------------------------
    # Add Student
    # -------------------------

    def add_student(self, name, roll_no, marks):

        for student in self.students:

            if student.roll_no == roll_no:

                print("\n❌ Roll number already exists.")

                return

        student = Student(name, roll_no, marks)

        self.students.append(student)

        self.save()

        print("\n✅ Student added successfully.")

    # -------------------------
    # View Students
    # -------------------------

    def display_students(self):

        if not self.students:

            print("\n❌ No students available.")

            return

        for student in self.students:

            student.display()

    # -------------------------
    # Search Student
    # -------------------------

    def search_student(self, keyword):

        found = []

        for student in self.students:

            if (
                keyword.lower() in student.name.lower()
                or keyword == str(student.roll_no)
            ):

                found.append(student)

        if not found:

            print("\n❌ Student not found.")

            return

        for student in found:

            student.display()

    # -------------------------
    # Update Student
    # -------------------------

    def update_student(self, roll_no, marks):

        for student in self.students:

            if student.roll_no == roll_no:

                student.marks = marks

                self.save()

                print("\n✅ Student updated successfully.")

                return

        print("\n❌ Student not found.")

    # -------------------------
    # Delete Student
    # -------------------------

    def delete_student(self, roll_no):

        for student in self.students:

            if student.roll_no == roll_no:

                self.students.remove(student)

                self.save()

                print("\n✅ Student deleted successfully.")

                return

        print("\n❌ Student not found.")

    # -------------------------
    # Statistics
    # -------------------------

    def statistics(self):

        if not self.students:

            print("\n❌ No students available.")

            return

        total_students = len(self.students)

        averages = [
            student.average_marks()
            for student in self.students
        ]

        highest = max(averages)
        lowest = min(averages)
        overall = sum(averages) / total_students

        print("\n========== STATISTICS ==========")

        print("Total Students :", total_students)
        print(f"Highest Average: {highest:.2f}")
        print(f"Lowest Average : {lowest:.2f}")
        print(f"Overall Average: {overall:.2f}")

    # -------------------------
    # Sort Students
    # -------------------------

    def sort_students(self, option):

        if option == "1":

            self.students.sort(
                key=lambda student: student.name.lower()
            )

        elif option == "2":

            self.students.sort(
                key=lambda student: student.average_marks(),
                reverse=True
            )

        elif option == "3":

            self.students.sort(
                key=lambda student: student.roll_no
            )

        else:

            print("\n❌ Invalid option.")

            return

        print("\n✅ Students sorted successfully.")

        self.display_students()

    # -------------------------
    # Save
    # -------------------------

    def save(self):

        save_students(self.students)