import os
from time import sleep
clear = lambda:  os.system('cls')
# rental_income

#ri_ex: 2,000 (/m)
# expenses
# cashflow = income - expenses

class Property:
    def __init__(self):
        self.expenses = Expenses()
        self.income = Income()
        self.investment = Investment()
        self.total_monthly_expenses = 0
        self.monthly_totals = {
            'income': 0,
            'expenses': 0
        }
        self.total_investment = 0
        self.cash_flow = { "monthly": 0, "annual": 0}
        self.cash_on_cash_roi = 0
    
    def get_attributes(self, obj):
        clear()
        print(f"Enter {obj.__class__.__name__} Details".center(30, "-"))
        for attr in vars(obj):
            setattr(obj,attr, float(input(f'{attr.replace("_", " ").title()}: $'))) 
            
    def get_expenses(self):
        self.get_attributes(self.expenses)
    
    def get_income(self):
        self.get_attributes(self.income)
        
    def get_total(self, obj):
        return sum([getattr(obj, attr) for attr in vars(obj)])
            
    def calc_all(self):
        self.get_monthly_totals()
        self.get_total_investment()
        self.get_cash_flow()
        self.get_cash_on_cash_roi()
        
    def get_monthly_totals(self):
        for key in self.monthly_totals:
            self.monthly_totals[key] = self.get_total(self.__getattribute__(key))
            
    def get_total_investment(self):
        self.total_investment = sum([getattr(self.investment, att) for att in vars(self.investment)])
    
    def get_cash_flow(self) -> None:
        self.cash_flow['monthly'] =  self.monthly_totals['income'] - self.monthly_totals['expenses']
        self.cash_flow['annual'] = self.cash_flow['monthly'] * 12
    
    def get_cash_on_cash_roi(self):
        self.cash_on_cash_roi = self.cash_flow["annual"] / self.total_investment * 100
        
    def display_monthly_totals(self):
        for total in self.monthly_totals:
            print(f"{total.title()}: ${self.monthly_totals[total]}")
    
    def display_cash_flows(self):
        print(f"Monthly Cash Flow: ${self.cash_flow['monthly']:,.2f}")
        print(f"Annual Cash Flow: ${self.cash_flow['annual']:,.2f}")
        print(f"Total Investment: ${self.total_investment:,.2f}")
        print(f"Cash on Cash ROI Flow: {self.cash_on_cash_roi:,.2f}%")
            
    
class Expenses:
    def __init__(self):
        self.mortgage = 0
        self.taxes = 0
        self.insurance = 0
        self.utilities = 0

class Income: 
    def __init__(self):
        self.rent = 0
        self.laundry = 0
        self.storage = 0
        self.misc = 0

class Investment:
    def __init__(self):   
        self.down_payment = 0
        self.closing_costs = 0
        self.rehab_budget = 0
        self.misc_other = 0
    
def run():
    property = Property()
    property.get_attributes(property.income)
    property.get_attributes(property.expenses)
    property.get_attributes(property.investment)
    property.calc_all()
    clear()
    property.display_monthly_totals()
    property.display_cash_flows()

run()