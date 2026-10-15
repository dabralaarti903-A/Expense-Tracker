import csv
from datetime import datetime
FILENAME = "expenses.csv"
def add_expense(amount, category):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(FILENAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category])
    print(f"✅ Expense of ₹{amount} added under {category}.")
def view_summary():
    total = 0
    category_summary = {}

    try:
        with open(FILENAME, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                amount = float(row[1])
                category = row[2]
                total += amount
                category_summary[category] = category_summary.get(category, 0) + amount
    except FileNotFoundError:
        print("⚠️ No expenses recorded yet.")
        return

    print("\n📊 Expense Summary")
    print(f"Total spent: ₹{total}")
    for category, amt in category_summary.items():
        print(f"- {category}: ₹{amt}")
    print()
def main():
    while True:
        print("\n--- Daily Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                amount = float(input("Enter amount: ₹"))
                category = input("Enter category (Food/Rent/Personal Expenses/Savings/etx.:-");
                add_expense(amount, category)
            except ValueError:
                print("⚠️ Please enter a valid number for amount.")
        elif choice == "2":
            view_summary()
        elif choice == "3":
            print("👋 Exiting... Have a great day!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
