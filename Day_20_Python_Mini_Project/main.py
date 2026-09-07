from student_manager import StudentManager
from utils import get_integer, get_marks


manager = StudentManager()


def add_student():

    print("\n========== ADD STUDENT ==========")

    name = input("Enter student name: ").strip()

    while not name:

        print("❌ Name cannot be empty.")

        name = input("Enter student name: ").strip()

    roll_no = get_integer("Enter roll number: ")

    marks = get_marks()

    manager.add_student(
        name,
        roll_no,
        marks
    )


def search_student():

    print("\n========== SEARCH STUDENT ==========")

    keyword = input(
        "Enter name or roll number: "
    ).strip()

    manager.search_student(keyword)


def update_student():

    print("\n========== UPDATE STUDENT ==========")

    roll_no = get_integer(
        "Enter roll number: "
    )

    marks = get_marks()

    manager.update_student(
        roll_no,
        marks
    )


def delete_student():

    print("\n========== DELETE STUDENT ==========")

    roll_no = get_integer(
        "Enter roll number: "
    )

    manager.delete_student(roll_no)


def sort_students():

    print("\n========== SORT STUDENTS ==========")

    print("1. By Name")
    print("2. By Average Marks")
    print("3. By Roll Number")

    choice = input("Choose option: ")

    manager.sort_students(choice)


def show_menu():

    print("\n")
    print("======================================")
    print("       🎓 STUDENT MANAGEMENT SYSTEM")
    print("======================================")

    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Student Statistics")
    print("7. Sort Students")
    print("8. Save Data")
    print("9. Exit")

    print("======================================")


def main():

    while True:

        show_menu()

        choice = input(
            "Enter your choice: "
        ).strip()

        if choice == "1":

            add_student()

        elif choice == "2":

            manager.display_students()

        elif choice == "3":

            search_student()

        elif choice == "4":

            update_student()

        elif choice == "5":

            delete_student()

        elif choice == "6":

            manager.statistics()

        elif choice == "7":

            sort_students()

        elif choice == "8":

            manager.save()

            print("\n✅ Data saved successfully.")

        elif choice == "9":

            manager.save()

            print("\nData saved successfully.")
            print("Thank you for using the system! 👋")

            break

        else:

            print("\n❌ Invalid choice.")


if __name__ == "__main__":
    main()