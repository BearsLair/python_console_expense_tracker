from storage import load_expenses, save_expenses
from expenses import add_expense, list_expenses, summarize, edit_expense, delete_expense

def main_menu():
    print("\n==== Personal Expense Tracker ====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Summary")
    print("4. Edit Expense")
    print("5. Delete Expense")
    print("6. Exit")
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

def handle_edit_expense(expenses):
    print("\n--- Edit Expense ---")
    print(list_expenses(expenses))

    try:
        index = int(input("\nEnter the number of the expense to edit: "))
    except ValueError:
        print("Invalid input.")
        return
    
    if index < 0 or index >= len(expenses):
        print("Expense not found.")
        return
    
    print("Leave a field blank to keep the current value.")

    current = expenses[index]

    amount_str = input(f"New amount (current: ${current['amount']:.2f}): ")
    category = input(f"New category (current: {current['category']}): ")
    description = input(f"New description (current: {current['description']}): ")
    date = input(f"New date (current: {current['date']}): ")

    amount = None
    if amount_str.strip():
        try:
            amount = float(amount_str)
        except ValueError:
            print("Invalid amount. Keep old value.")
            amount = None

    if category.strip() == "":
        category = None
    if description.strip() == "":
        description = None
    if date.strip() == "":
        date = None

    if edit_expense(expenses, index, amount, category, description, date):
        save_expenses(expenses)
        print("Expense updated successfully!")
    else: 
        print("Failed to update expense.")

def handle_delete_expense(expenses):
    print("\n--- Delete Expense ---")
    print(list_expenses(expenses))

    try:
        index = int(input("\nEnter the number of the expense to delete: "))
    except ValueError:
        print("Invalid input.")
        return
    
    if delete_expense(expenses, index):
        save_expenses(expenses)
        print("Expense delete.")
    else:
        print("Expense not found.")



def main():
     expenses = load_expenses()

     while True:
        choice = main_menu()

        if choice == "1":
            handle_add_expense(expenses)
        elif choice == "2":
            handle_view_expenses(expenses)
        elif choice == "3":
            handle_summary(expenses)
        elif choice == "4":
            handle_edit_expense(expenses)
        elif choice == "5":
            handle_delete_expense(expenses)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
             print("Invalid choice. Please try again.")

if __name__ == "__main__":
     main()


