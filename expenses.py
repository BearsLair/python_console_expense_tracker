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
    
def summarize(expenses):
    if not expenses:
        return "No expenses to summarize."
    
    # ???
    total = sum(exp["amount"] for exp in expenses)

    categories = {}
    for exp in expenses:
        cat = exp["category"]
        categories[cat] = categories.get(cat, 0) + exp["amount"]

    summary_lines = [
        f"Total spent: ${total:.2f}",
        "",
        "By category:"
    ]

    for cat, amount in categories.items():
        summary_lines.append(f"  {cat}: ${amount:.2f}")

    for cat, amount in categories.items():
        summary_lines.append(f"  {cat}: ${amount:.2f}")

    return "\n".join(summary_lines)

def edit_expense(expenses, index, amount=None, category=None, description=None, date=None):
    if index < 0 or index >= len(expenses):
        return False
    
    expense = expenses[index]

    if amount is not None:
        expense["amount"] = amount
    if category is not None:
        expense["category"] = category
    if description is not None:
        expense["description"] = description
    if date is not None:
        expense["date"] = date

    return True