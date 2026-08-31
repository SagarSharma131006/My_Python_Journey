# ============================================================
# PYTHON JOURNEY - DAY 13
# File: math_operations.py
# ============================================================

"""
This file contains some functions that we can
reuse in another Python file.
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):

    if b == 0:
        return "Cannot divide by zero"

    return a / b