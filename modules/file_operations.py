# file_operations.py
# This file handles reading, writing, and deleting expense data.

import os
from .expense import Expense

FILE_PATH = "data/expenses.txt"  # Path to store the expenses

def save_expense(expense):
    # Append a new expense to the file
    with open(FILE_PATH, "a") as f:
        f.write(expense.format_expense() + "\n")

def load_expenses():
    # If the file doesn't exist, return an empty list
    if not os.path.exists(FILE_PATH):
        return []
    # Read all expenses from the file
    with open(FILE_PATH, "r") as f:
        lines = f.readlines()
        return [Expense.from_string(line) for line in lines if line.strip()]

def delete_expense(index):
    # Delete an expense by its number (1-based index)
    expenses = load_expenses()
    if 1 <= index <= len(expenses):
        del expenses[index - 1]  # Remove the chosen expense
        with open(FILE_PATH, "w") as f:
            for expense in expenses:
                f.write(expense.format_expense() + "\n")
        return True
    return False
