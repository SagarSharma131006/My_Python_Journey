# 🎓 Student Management System

A Python-based **Student Management System** built as the final mini project of my **100 Days of Code in Python** journey.

This project combines the Python concepts learned throughout Days 1–19 into a practical, modular application.

---

## 🚀 Features

- ➕ Add Student
- 👀 View All Students
- 🔍 Search Student by Name or Roll Number
- ✏️ Update Student Marks
- 🗑️ Delete Student
- 📊 View Student Statistics
- 🔢 Sort Students by:
  - Name
  - Average Marks
  - Roll Number
- 💾 Save Student Data
- 🔄 Automatically Load Saved Data
- 🛡️ Input Validation
- ⚠️ Exception Handling
- 📁 Persistent Data Storage using JSON

---

## 🧠 Concepts Used

- Variables & Data Types
- Input & Output
- Conditional Statements
- Loops
- Strings
- Lists
- Functions
- Modules
- Exception Handling
- File Handling
- JSON
- List Comprehensions
- Object-Oriented Programming (OOP)
  - Classes & Objects
  - Constructors
  - Encapsulation
  - Inheritance
  - Polymorphism
  - Abstraction

---

## 📂 Project Structure

```text
Day_20_Python_Mini_Project/
│
├── main.py
├── student.py
├── student_manager.py
├── file_handler.py
├── utils.py
├── students.json
└── README.md
```

---

## ⚙️ Project Architecture

```text
                main.py
                   │
                   ↓
            StudentManager
                   │
                   ↓
               Student
                   │
                   ↓
             File Handler
                   │
                   ↓
             students.json
```

Each file has a specific responsibility, making the project easier to understand, maintain, and extend.

---

## 💾 Data Persistence

Student records are stored in `students.json`.

The application automatically:

- Saves student data when changes are made.
- Loads previously saved data when the application starts.
- Keeps student records available even after closing the program.

---

## ▶️ How to Run

Make sure Python is installed on your system.

Open the project folder in VS Code and run:

```bash
python main.py
```

---

## 📋 Main Menu

```text
======================================
       🎓 STUDENT MANAGEMENT SYSTEM
======================================

1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Student Statistics
7. Sort Students
8. Save Data
9. Exit

======================================
```

---

## 🎯 Project Goal

The goal of this project was to apply the Python fundamentals learned during **Days 1–19** into one practical application.

Instead of learning concepts individually, this project combines them to build a complete command-line based application.

---

## 🐍 Python Journey

**Day 20/100 — Python Mini Project ✅**

This project marks the completion of my **Python Fundamentals Phase** in my 100 Days of Code journey.

---

## 👨‍💻 Author

**Sagar Sharma**

Built with ❤️ using **Python**.
