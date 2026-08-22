# 🐍 My Python Journey

> **A day-by-day journey to learn, practice, and master Python programming.**

Welcome to my **Python Journey** repository! 🚀

I created this repository to document my Python learning journey and maintain a record of everything I learn and practice along the way.

Instead of learning Python only through theory, my goal is to **learn concepts, write code, practice problems, and document my progress every day**.

This repository will contain my daily Python programs, examples, practice questions, important concepts, and notes.

---

## 🎯 Goals of This Journey

Through this journey, I aim to:

* 🐍 Build a strong foundation in Python
* 💻 Improve my programming and problem-solving skills
* 🧠 Understand Python concepts through practical coding
* 📝 Document my learning consistently
* 📊 Prepare for Data Science and Machine Learning
* 🤖 Build a strong programming foundation for AI/ML
* 🚀 Develop the habit of learning and coding every day

---

## 📚 Python Fundamentals Roadmap

| Day | Topic                  |    Status    |
| :-: | ---------------------- | :----------: |
|  01 | Data Types             | 🟩 Completed |
|  02 | Operators              | 🟩 Completed |
|  03 | Input & Output         | 🟩 Completed |
|  04 | Conditional Statements | 🟩 Completed |
|  05 | Loops                  |  🟪 Pending  |
|  06 | Strings                |  🟪 Pending  |
|  07 | Lists                  |  🟪 Pending  |
|  08 | Tuples                 |  🟪 Pending  |
|  09 | Sets                   |  🟪 Pending  |
|  10 | Dictionaries           |  🟪 Pending  |
|  11 | Functions              |  🟪 Pending  |
|  12 | Recursion              |  🟪 Pending  |
|  13 | Modules & Packages     |  🟪 Pending  |
|  14 | Exception Handling     |  🟪 Pending  |
|  15 | File Handling          |  🟪 Pending  |
|  16 | Regular Expressions    |  🟪 Pending  |

---

# 📅 Daily Progress

## 🟩 Day 01 — Data Types

### Topics Covered

* Integer (`int`)
* Float (`float`)
* String (`str`)
* Boolean (`bool`)
* Complex (`complex`)
* `NoneType`
* `type()`
* `isinstance()`
* Dynamic Typing
* Variables

### Key Learning

Python is a **dynamically typed language**, which means we don't need to explicitly declare the data type of a variable.

```python
x = 10
x = "Python"
```

The same variable can hold values of different data types.

---

## 🟩 Day 02 — Operators

### Topics Covered

* Arithmetic Operators
* Assignment Operators
* Comparison Operators
* Logical Operators
* Identity Operators
* Membership Operators
* Bitwise Operators
* Operator Precedence

### Key Learning

An important distinction is between `==` and `is`.

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True
print(a is b)  # False
```

`==` compares **values**, while `is` checks whether two variables refer to the **same object**.

---

## 🟩 Day 03 — Input & Output

### Topics Covered

* `print()`
* `input()`
* Integer and float input
* Multiple inputs
* `split()`
* `map()`
* `sep`
* `end`
* Escape characters
* f-strings
* String formatting

### Key Learning

The `input()` function always returns a **string**.

```python
age = input("Enter your age: ")

print(type(age))
```

For numerical operations, the input needs to be converted:

```python
age = int(input("Enter your age: "))
```

---

## 🟩 Day 04 — Conditional Statements

### Topics Covered

* `if`
* `if-else`
* `if-elif-else`
* Nested `if`
* `and`
* `or`
* `not`
* Conditional expressions / Ternary operator
* Decision making

### Key Learning

Conditional statements allow a program to make decisions based on whether a condition is `True` or `False`.

Example:

```python
age = 20

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

---

## 🟪 Day 05 — Loops

### Planned Topics

* `for` loop
* `while` loop
* `range()`
* Nested loops
* `break`
* `continue`
* `pass`
* Loop patterns
* Practical problems

### Goal

Learn how to repeat a block of code efficiently and solve repetitive programming problems.

---

## 🟪 Day 06 — Strings

### Planned Topics

* Creating strings
* String indexing
* String slicing
* String methods
* String concatenation
* String formatting
* Escape characters
* Common string operations

---

## 🟪 Day 07 — Lists

### Planned Topics

* Creating lists
* Indexing
* Slicing
* Adding elements
* Removing elements
* Updating elements
* List methods
* Nested lists
* List operations

---

## 🟪 Day 08 — Tuples

### Planned Topics

* Creating tuples
* Tuple indexing
* Tuple slicing
* Tuple methods
* Tuple unpacking
* Immutability
* Tuple vs List

---

## 🟪 Day 09 — Sets

### Planned Topics

* Creating sets
* Unique elements
* Adding and removing elements
* Set operations
* Union
* Intersection
* Difference
* Symmetric difference
* Set methods

---

## 🟪 Day 10 — Dictionaries

### Planned Topics

* Key-value pairs
* Creating dictionaries
* Accessing values
* Adding and updating values
* Removing elements
* Dictionary methods
* Nested dictionaries
* Iterating through dictionaries

---

## 🟪 Day 11 — Functions

### Planned Topics

* Creating functions
* Calling functions
* Parameters
* Arguments
* Return values
* Default arguments
* Keyword arguments
* Positional arguments
* Variable-length arguments
* `*args`
* `**kwargs`

### Goal

Learn how to write reusable and organized Python code.

---

## 🟪 Day 12 — Recursion

### Planned Topics

* What is recursion?
* Recursive functions
* Base case
* Recursive case
* Call stack
* Factorial
* Fibonacci
* Recursion vs iteration

---

## 🟪 Day 13 — Modules & Packages

### Planned Topics

* What are modules?
* `import`
* `from ... import`
* Built-in modules
* Creating custom modules
* Packages
* `__name__`
* `__main__`
* Using Python libraries

---

## 🟪 Day 14 — Exception Handling

### Planned Topics

* Errors vs Exceptions
* `try`
* `except`
* `else`
* `finally`
* Multiple exceptions
* `raise`
* Custom exceptions

### Goal

Learn how to handle errors gracefully instead of allowing programs to crash unexpectedly.

---

## 🟪 Day 15 — File Handling

### Planned Topics

* Opening files
* Reading files
* Writing files
* Appending data
* File modes
* `with` statement
* Text files
* Working with file paths

---

## 🟪 Day 16 — Regular Expressions

### Planned Topics

* Introduction to Regular Expressions
* `re` module
* `search()`
* `match()`
* `findall()`
* `finditer()`
* `sub()`
* Character classes
* Quantifiers
* Patterns
* Practical validation examples

---

# 🛠️ Tools & Technologies

Throughout this journey, I will primarily use:

* 🐍 Python
* 💻 Visual Studio Code
* 🔧 Git
* 🐙 GitHub

As the journey progresses, I plan to explore Python libraries and tools related to:

* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn
* Jupyter Notebook

---

# 📂 Repository Structure

The repository is organized according to the learning days:

```text
My-Python-Journey/
│
├── README.md
│
├── Day_01_Data_Types/
│   └── data_types.py
│
├── Day_02_Operators/
│   └── operators.py
│
├── Day_03_Input_Output/
│   └── input_output.py
│
├── Day_04_Conditional_Statements/
│   └── conditional_statements.py
│
├── Day_05_Loops/
│   └── loops.py
│
├── Day_06_Strings/
│   └── strings.py
│
├── Day_07_Lists/
│   └── lists.py
│
├── Day_08_Tuples/
│   └── tuples.py
│
├── Day_09_Sets/
│   └── sets.py
│
├── Day_10_Dictionaries/
│   └── dictionaries.py
│
├── Day_11_Functions/
│   └── functions.py
│
├── Day_12_Recursion/
│   └── recursion.py
│
├── Day_13_Modules_Packages/
│   └── modules_packages.py
│
├── Day_14_Exception_Handling/
│   └── exception_handling.py
│
├── Day_15_File_Handling/
│   └── file_handling.py
│
└── Day_16_Regular_Expressions/
    └── regular_expressions.py
```

---

# 📈 Learning Method

For each topic, I follow a simple learning cycle:

```text
Learn
  ↓
Understand
  ↓
Code
  ↓
Practice
  ↓
Solve Problems
  ↓
Document
  ↓
Repeat
```

Each day's code focuses on understanding the concept through practical examples rather than only learning theory.

---

# 📝 What Each Day Contains

Each learning day may include:

* 📖 Topic explanation
* 💻 Python examples
* 🧠 Important concepts
* 📌 Important notes
* 🧪 Practical examples
* 📝 Practice questions
* 🚀 Small coding challenges

---

# 🎯 Future Goals

After completing the Python fundamentals, I plan to continue my journey toward:

```text
Python Fundamentals
        ↓
Advanced Python
        ↓
NumPy
        ↓
Pandas
        ↓
Data Visualization
        ↓
Data Analysis
        ↓
Statistics & Probability
        ↓
Machine Learning
        ↓
Deep Learning
        ↓
Artificial Intelligence
```

The ultimate goal is to build a strong foundation for **AI, Machine Learning, and Data Science**.

---

# 📊 Progress

**Current Progress: 4 / 16 topics completed**

```text
████████████░░░░ 25%
```

### Completed

* ✅ Day 01 — Data Types
* ✅ Day 02 — Operators
* ✅ Day 03 — Input & Output
* ✅ Day 04 — Conditional Statements

### Up Next

* ⏳ Day 05 — Loops
* ⏳ Day 06 — Strings
* ⏳ Day 07 — Lists
* ⏳ Day 08 — Tuples
* ⏳ Day 09 — Sets
* ⏳ Day 10 — Dictionaries
* ⏳ Day 11 — Functions
* ⏳ Day 12 — Recursion
* ⏳ Day 13 — Modules & Packages
* ⏳ Day 14 — Exception Handling
* ⏳ Day 15 — File Handling
* ⏳ Day 16 — Regular Expressions

---

# 🚀 Learning in Public

I am documenting this journey publicly to stay consistent, track my progress, and share what I learn with others.

Every completed day represents one more step toward becoming a better programmer.

> **Consistency beats perfection. Keep learning. Keep coding. Keep building. 🚀**

---

## ⭐ Follow My Journey

If you're also learning Python, Data Science, Machine Learning, or AI, feel free to explore this repository and learn along with me.

**100 Days of Code. One day at a time. One concept at a time. 🐍💻**
