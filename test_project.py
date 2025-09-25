from project import Financial
def test_add_income():
    f = Financial()
    assert f.add_income(100) == 100

def test_add_expense():
    f = Financial()
    expense = {"thing": "Eggs", "price": 1000, "time": "2025-09-23 17:00"}
    assert f.add_expenses(expense) == expense


def test_total_money_spent():
    f = Financial()
    f.add_expenses({"thing": "Book", "price": 2000, "time": "2025-09-23 17:10"})
    total = f.total_money_spent()
    assert total >= 2000
test_add_income()
test_add_expense()
test_total_money_spent()