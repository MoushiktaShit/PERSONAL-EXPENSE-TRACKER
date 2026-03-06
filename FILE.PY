import csv
from datetime import date

expenses = []
file_name = "expenses.csv"
# Load expenses from file##
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
# Save expenses to file##
def save_expenses():
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        for exp in expenses:
            writer.writerow([exp["amount"], exp["category"], exp["date"]])
# Add Expense##
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
    print("Expense Added Successfully!\n")
# View Expenses ##
def view_expenses():
    if not expenses:
        print("No expenses found.\n")
        return

    print("\nAll Expenses:\n")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['amount']} | {exp['category']} | {exp['date']}")
    print()
# Show Summary #
def show_summary():
    if not expenses:
        print("No expenses to summarize.\n")
        return

    total = sum(exp["amount"] for exp in expenses)

    category_total = {}
    for exp in expenses:
        cat = exp["category"]
        category_total[cat] = category_total.get(cat, 0) + exp["amount"]

    average = total / len(expenses)

    print("\nExpense Summary\n")
    print(f"Total Spent: {total}")

    print("\nSpending by Category:")
    for cat, amt in category_total.items():
        print(f"{cat}: {amt}")

    print(f"\nAverage Expense: {average:.2f}\n")

# Delete Expense#
def delete_expense():
    view_expenses()

    if not expenses:
        return

    try:
        index = int(input("Enter index to delete: "))
        removed = expenses.pop(index - 1)
        print(f"Deleted expense: {removed['amount']} ({removed['category']})\n")
    except:
        print("Invalid index!\n")

# Main Menu #
def main():
    load_expenses()

    while True:
        print("Personal Expense Tracker := ")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Summary")
        print("4. Delete Expense")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            show_summary()

        elif choice == "4":
            delete_expense()

        elif choice == "5":
            save_expenses()
            print("Data saved")
            break

        else:
            print("Invalid choice!\n")

main()
 
 