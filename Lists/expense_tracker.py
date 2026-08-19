expenses = []
def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    expense = {
        "name": name,
        "amount": amount
    }
    expenses.append(expense)
    print("Expense added successfully!")
def view_expenses():
    if not expenses:
        print("No expenses found.")
        return
    print("\n--- Expenses ---")
    for expense in expenses:
        print(expense["name"], ":", expense["amount"])
def calculate_total():
    total = 0
    for expense in expenses:
        total += expense["amount"]
    print("Total Expense:", total)
while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        calculate_total()
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")