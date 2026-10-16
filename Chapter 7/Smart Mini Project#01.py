#pythton project
print("-------------Smart Employee Salary and Expence Tracker System------------------")
company_tax_rate = 0.10
currency = "Rs."

def calculate_total_salary(base_salary, bonus = 5000):
    gross_salary = base_salary + bonus
    tax_amount = gross_salary * company_tax_rate
    net_salary = gross_salary - tax_amount
    return net_salary

def log_expense (**expense_details):
    daily_expense = {}
    for key, value in expense_details.item():
        daily_expense[key] = value
    print("Expese rercords successfully!")
    return daily_expense

def generate_payslip (employee_name, basic_salary , bonus = 5000, **expense_info):
    net_salary =  calculate_total_salary(basic_salary, bonus)
    print("\n" + "=" *35 )
    print("        office payslip         ")
    print("="*35)
    print(f"Employee name : {employee_name}")
    print(f"basic salary : {currency}{basic_salary}")
    print(f"Bonus : {currency}{bonus}")
    print(f"Tax rate : {int(company_tax_rate*100)}%")
    print(f"Net salary = {currency}{net_salary}")
    print("-" *35)

    if expense_info:
        print("Expense Details:")
        recorded_expense = log_expense(**expense_info)
        for k, v in recorded_expense.items():
            print(f"  - {k.capitalize()}: {v}")
    else:
        print("this month, no expense recorded.")
    
    print("=" * 35)

generate_payslip(
    employee_name="Ayesha", 
    basic_salary=60000, 
    bonus=7000, 
    category="Travel", 
    amount=1500, 
    date="2026-10-08"
)    
