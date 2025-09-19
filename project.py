from datetime import datetime
import json
import time


print("Hello, Welcome to your Financial Tracker,\n\t How can i help you?")
print("1.income\n2.Add expense\n3.view_report\n4.Previous Expense data\n5.Exit")


class Financial:
    def __init__(self):
        # self.name = name
        # self.income = income
        # self.expense = expense

        def __str__(self):

            pass

    def add_income(n):
        while True:
            try:
                global income
                income = int(input("Enter your income: "))
                with open("Income.json", "w") as f:
                    json.dump({"income": income}, f, indent=4)

                break
            except ValueError:
                print("Your Income should be in numbers.")

    def add_expenses(n):

        while True:
            expense = input(
                "Enter the thing you spend moneyon(price/thing_category) or enter q to quit: ")
            if expense.lower() in ("q", "quit", "exit"):
                print("Your expenses have been saved")
                break
            try:
                thing, price = expense.split(" ")
                time_now = datetime.now()
                time_now_rounded_to_mins = time_now.strftime("%Y-%m-%d %H:%M")
                total_expense = {
                    "price": price,
                    "thing": thing,
                    "time": time_now_rounded_to_mins
                }
                try:
                    with open("data.json", "r") as file:
                        data = json.load(file)
                except (FileNotFoundError, json.JSONDecodeError):
                    data = []

                data.append(total_expense)

                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)

            except (ValueError, TypeError):
                print("Invalid Format, Please use the given format")
    def report(n):
        print("1.Money left\n2.Total_money_spent\n3.List of items\n4.Exit")
        report_menu = int(input(""))
        if report_menu == 1:
            f.Money_Left()
        elif report_menu == 2:
            f.Total_Money_Spent()
        elif report_menu == 3:
            f.List_of_Items()
        elif report_menu == 4:
            print("Exit")

        else:
            print("There was something wrong")

    def Money_Left(n):
        with open("Income.json", "r") as f:
            data = json.load(f)
        with open("Total.json", "r") as f:
            data_ = json.load(f)
        Money_left = data["income"] - data_["Total"]
        Money_spent_perc = (data_["Total"]/data["income"])*100
        print(f"You have spent {round(Money_spent_perc)}% of your money.")
        print(f"There are {Money_left}$ left.")

    def Total_Money_Spent(n):
        with open("data.json", "r") as f:

            data = json.load(f)

            global total
            total = 0

            for item in data:
                if isinstance(item, dict):

                    total += int(item["price"])

                else:
                    print(item)
        with open("Total.josn", "w") as f:
            json.dump({"Total": total}, f)
        print(total)
    def List_of_Items(n):
        with open("data.json", "r") as f:

            data = json.load(f)
        for item in data:
            if isinstance(item, dict):
                print(f"{item["thing"]} : {item["price"]}")
                
    def delete_previous_data(n):
        print(
            "Enter 1 to clear previous Expense History\nEnter 2 to see the Complete History")
        value = int(input(""))
        if value == 1:
            open("data.json", "w").close()
            print("Your previous data has been deleted")
        elif value == 2:
            with open("data.json", "r") as f:
                print("Your expense data is:")
                data = json.load(f)
                for item in data:
                    if isinstance(item, dict):
                        price = item.get("price")
                        thing = item.get("thing")
                        time = item.get("time")
                        print(f" {thing} was bought of  {price}$  on {time}")
                    else:
                        print(item)

        else:
            print("You Entered the wrong value!")






f = Financial()
menu = int(input("Enter the Menu number:"))
if menu == 1:
    f.add_income()

elif menu == 2:
    f.add_expenses()

elif menu == 3:
    f.report()

elif menu == 4:
    f.delete_previous_data()

elif menu == 5:
    print("Thanks")


else:
    print("There is a problem")
