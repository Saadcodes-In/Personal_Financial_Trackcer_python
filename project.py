from ast import Continue
from datetime import datetime
import json
from typing import ItemsView


print("Hello, Welcome to your Financial Tracker,\n\t How can i help you?")
print("1.income\n2.expense\n3.view_report\n4.Previous Expense data\n5.Exit")


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
                income = int(input("Enter your income: "))
                break
            except ValueError:
                print("Your Income should be in numbers.")
                
            

    def add_expenses(n):

        while True:
            expense = input(
                "Enter the thing you spend moneyon(price/thing_category) or enter q to quit: ")
            if expense.lower() in ("q", quit, exit):
                print("Your expenses have been saved")
                break
            try:
                price, thing = expense.split(" ")
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


    def delete_previous_data(n):
         print("Enter 1 to clear previous Expense History\nEnter 2 to see the Complete History")
         value = int(input(""))
         if value == 1:
            open("data.json", "w").close()
            print("Your previous data has been deleted")
         elif value ==2:
             with open("data.json", "r") as f:
                 print("Your expense data is:")
                 data = json.load(f)
                 for item in data:
                     if isinstance(item, dict):
                         for key, value, time in item.items():
                             print(f"{key} : {value} : {time}")
                     else:
                         print(item)    
                 
         else:
             print("You Entered the wrong value!")
         
    

    def report(n):
        print("1.Today's Report\n2.Weekly Report\n3.Monthly Report\n4.Exit")
        report_menu = int(input("Enter the number of report you want:"))
        if report_menu == 1:
            f.Todays_Report()
        elif report_menu == 2:
            f.Weekly_Report()
        elif report_menu == 3:
            f.Monthly_Report()
        elif report_menu == 4:
            pass
        else:
            print("There was something wrong")


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
