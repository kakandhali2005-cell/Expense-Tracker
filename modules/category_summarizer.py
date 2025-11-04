# category_summarizer.py
# This file summarizes expenses by category.

def summarize_by_category(expenses):
    summary = {}  # Dictionary to store category totals
    for expense in expenses:
        if expense.category in summary:
            summary[expense.category] += expense.amount
        else:
            summary[expense.category] = expense.amount
    return summary
