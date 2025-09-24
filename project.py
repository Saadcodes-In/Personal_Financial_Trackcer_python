from datetime import datetime
import json
import time


print("Hello, Welcome to your Financial Tracker,\n\t How can i help you?")
print("1.income\n2.Add expense\n3.view_report\n4.Previous Expense data\n5.Exit")


class Financial:
    def __init__(self):

        ...

        def __str__(self):

            pass

    def add_income(n, income):

        with open("Income.json", "w") as f:
            json.dump({"income": income}, f, indent=4)

    def add_expenses(n, total_expense):

        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        data.append(total_expense)

        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

    def money_left(n):
        with open("Income.json", "r") as f:
            data = json.load(f)
        with open("Total.json", "r") as f:
            data_ = json.load(f)
        Money_left = data["income"] - data_["Total"]

        Money_spent_perc = (data_["Total"]/data["income"])*100
        print(f"You have spent {round(Money_spent_perc)}% of your money.")
        if Money_left > 0:

            print(f"There are {Money_left}$ left.")
        if Money_left < 0:
            Money_debt = abs(Money_left)
            print(f"You have a debt of {Money_debt}$")

    def total_money_spent(n):
        with open("data.json", "r") as f:

            data = json.load(f)

            total = 0

            for item in data:
                if isinstance(item, dict):

                    total += int(item["price"])

                else:
                    print(item)
        with open("Total.json", "w") as f:
            json.dump({"Total": total}, f)

        print(f"Total money spent is {total}$")

    def list_of_items(n):

        with open("data.json", "r") as f:

            data = json.load(f)
        for item in data:
            if isinstance(item, dict):
                print(f"{item["thing"]} : {item["price"]}")

    def delete_previous_data(n):

        open("data.json", "w").close()
        print("Your previous data has been deleted")

    def complete_history():
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


f = Financial()
menu = int(input("Enter the Menu number:"))
if menu == 1:
    while True:
        try:

            income = int(input("Enter your income: "))
            break
        except ValueError:
            print("Your Income should be in numbers.")
    f.add_income(income)

elif menu == 2:
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
        except (ValueError, TypeError):
            print("Invalid Format, Please use the given format")
    f.add_expenses(total_expense)

elif menu == 3:

    print("1.Money left\n2.Total_money_spent\n3.List of items\n4.Exit")
    report_menu = int(input(""))
    if report_menu == 1:
        f.money_left()
    elif report_menu == 2:
        f.total_money_spent()
    elif report_menu == 3:
        f.list_of_items()
    elif report_menu == 4:
        print("Exit")

    else:
        print("There was something wrong")


elif menu == 4:
    print("Enter 1 to clear previous Expense History\nEnter 2 to see the Complete History")
    value = int(input(""))
    if value == 1:
        f.delete_previous_data()
    elif value == 2:
        f.complete_history()
    else:
        print("You Entered the wrong value!")

elif menu == 5:
    print("Thanks")


else:
    print("There is a problem")
