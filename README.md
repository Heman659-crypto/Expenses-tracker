💰 Expense Tracking System

A simple menu-driven Expense Tracker built with Python. The application stores expense records in a CSV file and allows users to add expenses, view all expenses with total spending, and generate a category-wise spending summary.

🚀 Features

- Add new expenses
- Store expenses permanently in a CSV file
- View all recorded expenses
- Calculate total amount spent
- Generate category-wise spending summary
- Validate user input
- Handle invalid amounts gracefully
- Optional notes for expenses
- Simple menu-driven command-line interface

🛠️ Technologies Used

- Python 3
- CSV File Handling
- "csv" module
- "os" module
- Functions
- Exception Handling
- Dictionaries
- Loops and Conditional Statements

📂 Project Structure

expense-tracker/
│
├── expense_tracker.py
├── expenses.csv
├── README.md
└── .gitignore

▶️ How to Run

1. Clone the repository

git clone https://github.com/YOUR-USERNAME/expense-tracker.git

2. Open the project directory

cd expense-tracker

3. Run the application

python expense_tracker.py

On some Windows systems:

py expense_tracker.py

🎮 How to Use

After running the program, the following menu will appear:

========================================
          EXPENSE TRACKER
========================================
1. Add Expense
2. View All Expenses
3. Category-wise Summary
4. Exit

Add Expense

Select option "1" and enter:

- Date
- Category
- Amount
- Optional note

View Expenses

Select option "2" to display all saved expenses and the total amount spent.

Category Summary

Select option "3" to see how much has been spent in each category.

Exit

Select option "4" to close the application.

📄 CSV Data Format

Expense data is stored in the following format:

Date,Category,Amount,Note
13-08-2026,Food,250.00,Dinner
13-08-2026,Travel,100.00,Bus
12-08-2026,Shopping,500.00,Stationery

🧠 Concepts Practiced

This project demonstrates:

- Python functions
- File handling
- CSV data storage
- Reading and writing files
- Exception handling
- Input validation
- Dictionaries
- Loops
- Conditional statements
- Basic data aggregation

🔮 Future Improvements

Possible future upgrades:

- Delete expenses
- Edit existing expenses
- Search expenses by date or category
- Monthly spending reports
- Budget limits
- Data visualization
- SQLite database integration
- Tkinter graphical user interface
- Export reports

👨‍💻 Author
 Heman
