print("Welcome to return on Investment calculator")

rental_income = (float(input("What is your projected monthly rental income from property $ :  ")))
misc_income = (float(input("What is your projected monthly income from misc(laundry,storage, etc) $ :  ")))
total_yearly_income = (rental_income + misc_income)*12

tax_exp = (float(input("What is your monthly taxes on property $ :")))
ins_exp = (float(input("What is your monthly insurance expense $ :")))
utility_exp = (float(input("What is your monthly utilities expense incude gas, electric, water, trash total $ :")))
garden_snow = (float(input("WEhat are your monthly gardening costs $ :")))
vacancy = float(input("How much do you plan to put aside a month for vacancy $ : "))
cap_repair = float(input("What do you plan on setting aside a month for repairs and capital repairs $ :  "))
prop_mgmt = float(input("What are your monthly expenses for property management $ :"))
mortgage = float(input("What is your projected monthly mortgage $ :"))
total_yearly_expenses = (tax_exp + ins_exp + utility_exp + garden_snow + vacancy + cap_repair + prop_mgmt + mortgage)*12



down_payment = (float(input("Enter your downpayment on property in $ :  ")))
closing_cost = (float(input("Enter your closing costs $ :  ")))
repair_budget = (float(input("Enter your repair budget $ :")))
misc_exp = (float(input("How much are your misc expenses $ :  ")))
total_inv = (down_payment + closing_cost + repair_budget + misc_exp)

def roi(total_inv, total_yearly_income, total_yearly_expenses):
    cash_flow = (total_yearly_income - total_yearly_expenses)
    roi = (cash_flow / total_inv)*100
    return roi
print(roi(total_inv, total_yearly_income, total_yearly_expenses))

