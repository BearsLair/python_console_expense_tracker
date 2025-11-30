from storage import load_expenses, save_expenses
from expenses import add_expense, list_expenses, summarize

def main_menu():
    print("\n==== Personal Expense Tracker ====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Summary")
    print("4. Exit")
    choice = input("Choose an option(1-4): ")
    return choice

def handle_add_expense(expenses):
    print("\n--- Add Expense ---")
    try:
        amount = float(input("Amount: $"))
    except ValueError:
        print("Invalid amount. Please Enter a number.")
        return
    
    category = input("Category (e.g. Food, Transport, ect.):")
    description = input("Description: ")
    date = input("Date (YYYY-MM-DD) or leave blank for today: ")

    if date.strip() == "":
        date = None

    add_expense(expenses, amount, category, description, date)
    save_expenses(expenses)
    print("Expense added successfully:")

    def handle_view_expenses(expenses):
        print("\n--- All Expenses ---")
        print(list_expenses(expenses))

    def handle_summary(expenses):
        print("\n--- Summary ---")
        print(summarize(expenses))