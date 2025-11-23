#Personal Expense Tracker

expenses=[]
print("Welcome to Personal Expense Tracker")

while(True):
    print("-------MENU-------")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Expense")
    print("4. Exit")

    choice=int(input("Enter your choice: "))

    # Add Expense
    if choice==1:
        date=input("Enter the date (YYYY-MM-DD): ")
        category=input("Enter the category (e.g., Food, Transport): ")
        item=input("Enter the item name: ")
        amount=float(input("Enter the amount spent: "))
        # expense.append((date, category, item, amount))
        # print(f"Expense added: {item} - ${amount:.2f}")

        expense={
            "date": date,
            "category": category,
            "item": item,
            "amount": amount
        }
        expenses.append(expense)
        print(f"Expense added Successfully: {item} - {amount:.2f}")  

    # View Expenses
    elif choice==2:
        if not expenses:
            print("No expenses recorded.")
        else:
            print("Date\tCategory\tItem\tAmount")
            print("-"*50) #separator line
            count = 0
            for exp in expenses:
                print(f"{exp['date']}\t{exp['category']}\t{exp['item']}\t{exp['amount']:.2f}")
                count += 1
            print(f"Total expenses recorded: {count}")

    # View Total Expense
    elif choice==3:
        total = 0
        for exp in expenses:
            total += exp['amount']
        print(f"Total Expense: {total:.2f}")
    # Exit
    elif choice==4:
        print("Exiting Personal Expense Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

