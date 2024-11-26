# Exercise-1: Logical and operator

''' If Client has high income And good credit then
        Eligible for Loan.
'''

high_income = True
good_credit = False

if high_income and good_credit: # use 'and' operator when both conditions are required
    print("Client Eligible for Loan.")
else:
    print("Client Not Eligible for Loan.")

# Exercise-2: Logical or operator

''' If Client has high income or good credit then
        Eligible for Loan.
'''

if high_income or good_credit:  # use 'and' operator when both conditions are required
    print("Client Eligible for Loan.")
else:
    print("Client Not Eligible for Loan.")

# Exercise-3: Logical Not gate

''' If Applicant has good credit and doesn't have criminal record then
Eligible for Loan.'''

good_credit = True
criminal_record = True
if good_credit and not criminal_record: # use not operator to change the boolean value
    print("Client Eligible for Loan.")
else:
    print("Client Not Eligible for Loan.")










