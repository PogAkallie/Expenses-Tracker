class Expense:
    def __init__(self, date, descr, amount):
        self.date = date
        self.descr = descr
        self.amount = amount

class ExpenseTracker:
    def __init__(self):
        self.expenses = [] #list to put out expenses

    def add_expense(self, expense):
        self.expenses.append(expense) #adds element at the end of the list

    def remove_expense(self, index):
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            print("Expense removed.")
        else:
            print("Invalid index.")

    def view_expenses(self): #will show list of expenses
        if len(self.expenses) == 0:
            print("No expenses found :)")
        else:
            print("Expenses List:")
            for i, expense in enumerate(self.expenses, start=1):
                print(f"{i}. Date: {expense.date}, Description: {expense.descr}, Amount: lv{expense.amount:.2f}")

    def total_expenses(self):
        total = sum(expense.amount for expense in self.expenses)
        print(f"Total expenses: lv{total:.2f}")


def main():
    tracker = ExpenseTracker();

    while True:
        print("\nExpense Tracker Options:")
        print("1. Add Expense")
        print("2. Remove Expense")
        print("3. View Expenses")
        print("4. Total Expenses")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            descr = input("Enter description: ")
            amount = float(input("Enter the amount: "))
            expense = Expense(date, descr, amount)
            tracker.add_expense(expense)
            print("Expense added. :)")
        elif choice == "2":
            index = int(input("Enter the expense index to remove: ")) - 1
            tracker.remove_expense(index)
        elif choice == "3":
            tracker.view_expenses()
        elif choice == "4":
            tracker.total_expenses()
        elif choice == "5":
            print("Bye bye~ <3")
            break;
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
