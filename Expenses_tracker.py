"""
Expense Tracking System
-----------------------
A menu-driven expense tracker that stores expense records
in a CSV file.
"""

import csv
import os


FILE_NAME = "expenses.csv"


def initialize_file():
    """Create the CSV file with headers if it doesn't exist."""

    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Note"])


def get_valid_amount():
    """Get a valid positive amount from the user."""

    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount > 0:
                return amount

            print("Amount must be greater than 0.")

        except ValueError:
            print("Invalid amount. Please enter a valid number.")


def add_expense():
    """Add a new expense to the CSV file."""

    print("\n===== ADD EXPENSE =====")

    date = input("Enter date (DD-MM-YYYY): ").strip()

    while not date:
        print("Date cannot be empty.")
        date = input("Enter date (DD-MM-YYYY): ").strip()

    category = input("Enter category: ").strip()

    while not category:
        print("Category cannot be empty.")
        category = input("Enter category: ").strip()

    amount = get_valid_amount()

    note = input("Enter note (optional): ").strip()

    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, f"{amount:.2f}", note])

    print("Expense added successfully!")


def view_expenses():
    """Display all expenses and calculate total spending."""

    print("\n===== ALL EXPENSES =====")

    total = 0

    try:
        with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            expenses = list(reader)

            if not expenses:
                print("No expenses recorded yet.")
                return

            print(
                f"{'Date':<15}"
                f"{'Category':<15}"
                f"{'Amount':<12}"
                f"{'Note'}"
            )

            print("-" * 60)

            for expense in expenses:
                amount = float(expense["Amount"])

                print(
                    f"{expense['Date']:<15}"
                    f"{expense['Category']:<15}"
                    f"₹{amount:<11.2f}"
                    f"{expense['Note']}"
                )

                total += amount

            print("-" * 60)
            print(f"Total Spent: ₹{total:.2f}")

    except FileNotFoundError:
        print("Expense file not found.")


def category_summary():
    """Display total spending for each category."""

    print("\n===== CATEGORY-WISE SUMMARY =====")

    summary = {}

    try:
        with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for expense in reader:
                category = expense["Category"]
                amount = float(expense["Amount"])

                if category in summary:
                    summary[category] += amount
                else:
                    summary[category] = amount

    except FileNotFoundError:
        print("Expense file not found.")
        return

    if not summary:
        print("No expenses recorded yet.")
        return

    print(f"{'Category':<20}{'Total Spent'}")
    print("-" * 35)

    for category, total in summary.items():
        print(f"{category:<20}₹{total:.2f}")


def main():
    """Run the Expense Tracker application."""

    initialize_file()

    while True:
        print("\n" + "=" * 40)
        print("          EXPENSE TRACKER")
        print("=" * 40)

        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Category-wise Summary")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            category_summary()

        elif choice == "4":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()




