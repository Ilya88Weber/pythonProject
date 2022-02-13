gains = int(input("Company's gain: "))
expenses = int(input("Company's expenses: "))


if gains > expenses:
    profit = gains - expenses
    rent_revenue = int(gains / profit)
    print(f"Excellent job. Your annual gain {profit} and rent_revenue {rent_revenue}")
    employees = int(input("Amount of employees: "))
    income = profit / employees
    print(f'usd {income} per employee')
elif gains == expenses:
    print("Just okay")
else:
    print("work harder!")
