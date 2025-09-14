
print("Hello, Welcome to your Financial Tracker,\n\t How can i help you?")
print("1.income\n2.expense\n3.view_report\n4.Exit")



class Financial:
    def __init__(self):
        # self.name = name
        # self.income = income
        # self.expense = expense
        
        

     def __str__(self):
        
            pass

    def add_income(n):
        try:
            income = int(input("Enter your income: "))
        except ValueError:
            pass

    def add_expenses(n):
        total_expense = []

        

        while True:
            try:
                expense = input("Enter the thing you spend on(price/thing_category): ")
                price,thing = expense.split(" ")
                now = datetime.now()
                now_rounded_to_mins = now.strftime("%Y-%m-%d %H:%M")
                total_expense.append({"price": price,"thing": thing, "time": now_rounded_to_mins})
                

            except (ValueError,TypeError):
                print(total_expense)
                break
    def report():
        ...

f = Financial()
f.add_income()
f.add_expenses()