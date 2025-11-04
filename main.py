# main.py
# Entry point of the Expense Tracker application.

import re
from modules.expense import Expense
from modules.file_operations import save_expense, load_expenses, delete_expense
from modules.category_summarizer import summarize_by_category

def validate_date(date_str):
    # Validate date format (dd-mm-yyyy)
    pattern = r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-[0-9]{4}$"
    return re.match(pattern, date_str) is not None

def add_expense():
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        date = input("Enter date (dd-mm-yyyy): ")

        if not validate_date(date):
            print("❌ Invalid date format! Use dd-mm-yyyy")
            return

        expense = Expense(amount, category, date)
        save_expense(expense)
        print("✅ Expense added successfully!")
    except ValueError:
        print("❌ Invalid amount! Please enter a number.")

def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
        return
    print("\n📋 All Expenses:")
    for idx, expense in enumerate(expenses, start=1):
        print(f"{idx}. Amount: {expense.amount}, Category: {expense.category}, Date: {expense.date}")

def delete_expense_option():
    expenses = load_expenses()
    if not expenses:
        print("No expenses to delete.")
        return
    view_expenses()
    try:
        choice = int(input("Enter the expense number to delete: "))
        if delete_expense(choice):
            print("✅ Expense deleted successfully!")
        else:
            print("❌ Invalid choice.")
    except ValueError:
        print("❌ Please enter a valid number.")

def summarize_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses to summarize.")
        return
    summary = summarize_by_category(expenses)
    print("\n📊 Expenses by Category:")
    for category, total in summary.items():
        print(f"{category}: {total}")

def main():
    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Summarize by Category")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense_option()
        elif choice == "4":
            summarize_expenses()
        elif choice == "5":
            print("Goodbye 👋")
            break
        else:
            print("❌ Invalid choice, please try again.")

if __name__ == "__main__":
    main()
