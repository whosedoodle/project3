import time

def expenses():
    taxes = int(input('What are the property taxes?: '))
    insurance = int(input('What are the property insurance costs?: '))
    utilities = int(input('What are the property utilities?: '))
    hoa = int(input('What are the property hoa fees?: '))
    repairs = int(input('What are the property repair costs?(if none enter 0): '))
    mortgage = int(input('What is the mortgage cost?: '))
    expenses.total_monthly_expenses = taxes + insurance + utilities + hoa + repairs + mortgage
    print(f"Your total monthly expenses are ${expenses.total_monthly_expenses}")

def cash_flow():
    print('Welcome to the ROI Calculator.')
    rental_income = int(input('What is the rental income of the home?: '))
    time.sleep(2)
    expenses()
    time.sleep(2)
    cash_flow.total_monthly_cash_flow = (rental_income - expenses.total_monthly_expenses)
    print(f'Your total monthly cash flow is ${cash_flow.total_monthly_cash_flow}')

def total_investment():
    down_payment = int(input('What is your total downpayment?: '))
    closing_costs = int(input('What are the closing costs?: '))
    rehab = int(input('Are you planning to do any rehab work? (if none enter 0): '))
    total_investment.total_investment_cost = down_payment + closing_costs + rehab
    print(f'Your total investment costs are ${total_investment.total_investment_cost:.2f}')

def ROI():
    annual_cash_flow = cash_flow.total_monthly_cash_flow * 12
    ROI = (annual_cash_flow / total_investment.total_investment_cost) * 100
    print(f'Your cash on cash ROI is {ROI}%')

def run_calculator():
    cash_flow()
    time.sleep(2)
    total_investment()
    time.sleep(2)
    ROI()
    print(f'Thank you for using this calculator.')

run_calculator()
    