import csv
from datetime import date

expenses = []
file_name = "expenses.csv"

def load_expenses():
    try:
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                expenses.append({
                    "amount": float(row[0]),
                    "category": row[1],
                    "date": row[2]
                })
    except FileNotFoundError:
        pass


def save_expenses():
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        for exp in expenses:
            writer.writerow([exp["amount"], exp["category"], exp["date"]])

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food/Transport/etc): ")
    exp_date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")

    if exp_date == "":
        exp_date = str(date.today())

    expense = {
        "amount": amount,
        "category": category,
        "date": exp_date
    }

    expenses.append(expense)
    print(" Expense Added Successfully!\n")

def view_expenses():
    if not expenses:
        print("No expenses found.\n")
        return

    print("\nAll Expenses:\n")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['amount']} | {exp['category']} | {exp['date']}")
    print()


            


 