# expense.py
# This file defines the Expense class that represents a single expense.

class Expense:
    def __init__(self, amount, category, date):
        self.amount = amount  # Store the amount of money spent
        self.category = category  # Store the category of the expense
        self.date = date  # Store the date of the expense (dd-mm-yyyy format)

    def format_expense(self):
        # Return the expense as a string (for saving to file)
        return f"{self.amount},{self.category},{self.date}"

    @staticmethod
    def from_string(expense_str):
        # Convert a line from the file back into an Expense object
        amount, category, date = expense_str.strip().split(",")
        return Expense(float(amount), category, date)
