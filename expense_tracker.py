import json
from datetime import datetime
from pathlib import Path

DATA_FILE = Path("expenses.json")

def load_expenses():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

def save_expenses(expenses):
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense(description, amount):
    expenses = load_expenses()
    expenses.append({
        "description": description,
        "amount": amount,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    save_expenses(expenses)
    print(f"✅ Added: {description} - ₹{amount}")

def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded.")
        return
    total = 0
    print("\n📒 Expense List:")
    for e in expenses:
        print(f"- {e['date']} | {e['description']} | ₹{e['amount']}")
        total += e["amount"]
    print(f"\n💰 Total: ₹{total}")

def main():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            desc = input("Enter description: ")
            try:
                amt = float(input("Enter amount: ₹"))
                add_expense(desc, amt)
            except ValueError:
                print("❌ Amount must be a number.")
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
