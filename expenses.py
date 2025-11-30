from datetime import datetime

def add_expense(expenses, amount, category, description, date=None):
    if date is None:
        # strftime?
        date = datetime.today().strftime("%Y-%m-%d")

        expense = {
            "amount": amount,
            "category": category,
            "description": description,
            "date": date
        }

        expenses.append(expense)
        return expenses
    
def list_expenses(expenses):
    if not expenses:
        return "No expenses recorded."
    
    lines = []
    # what the hell is going on in this block of code?
    for i, exp in enumerate(expenses, start=1):
        line = f"{i}. ${exp['amount']:.2f} - {exp['category']} - {exp['description']} ({exp['date']})"
        lines.append(line)

        return "\n".join(lines)
    
