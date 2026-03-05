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
