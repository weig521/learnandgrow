# There are 4 diff tax status, 1-single, 2-MFJ, 3-MFS, and 4-head of household. single and MFS have the same tax bracket and tax rate
# We assign the tax bracket and tax rate seperately so that in future years we can easily change the data to use the program

# the year of the tax return, change the varialbe for the appropriate year
year = 2024

# The tax rate and tax bracket might change, especially the tax bracket. So we assign them with varialbes so that we can make changes for future use
# The different tax rates, from tier one tot tier 7
tax_rate_tier1 = 0.1
tax_rate_tier2 = 0.12
tax_rate_tier3 = 0.22
tax_rate_tier4 = 0.24
tax_rate_tier5 = 0.32
tax_rate_tier6 = 0.35
tax_rate_tier7 = 0.37

# There are different tax brackets for the different tax statuses. Only single is the same as MFS
tax_bracket_1_tier1 = tax_bracket_3_tier1 = 11600
tax_bracket_1_tier2 = tax_bracket_3_tier2 = 47150
tax_bracket_1_tier3 = tax_bracket_3_tier3 = 100525
tax_bracket_1_tier4 = tax_bracket_3_tier4 = 191950
tax_bracket_1_tier5 = tax_bracket_3_tier5 = 243725
tax_bracket_1_tier6 = tax_bracket_3_tier5 = 609350

tax_bracket_2_tier1 = 23200
tax_bracket_2_tier2 = 94300
tax_bracket_2_tier3 = 201050
tax_bracket_2_tier4 = 383900
tax_bracket_2_tier5 = 487450
tax_bracket_2_tier6 = 731200

tax_bracket_4_tier1 = 16550
tax_bracket_4_tier2 = 63100
tax_bracket_4_tier3 = 100500
tax_bracket_4_tier4 = 191950
tax_bracket_4_tier5 = 243700
tax_bracket_4_tier6 = 609350



status = input(f'Please choose your tax status: 1 single; 2 Married file jointly; 3 married filling separately; 4 Head of household: ')
income = float(input('Please enter your income: '))


# 3 conditions based on marital status, then calculate the tax according to the tax bracket and tax rate
if status == '2':
    if income <= tax_bracket_2_tier1:
        tax = tax_rate_tier1 * income
    elif income <= tax_bracket_2_tier2:
        tax = tax_rate_tier1 * tax_bracket_2_tier1 + (income-tax_bracket_2_tier1) * tax_rate_tier2
    elif income <= tax_bracket_2_tier3:
        tax = tax_rate_tier1 * tax_bracket_2_tier1 + tax_rate_tier2 * (tax_bracket_2_tier2 -  tax_bracket_2_tier1) + (income-tax_bracket_2_tier2) * tax_rate_tier3
    elif income <= tax_bracket_2_tier4:
        tax = tax_rate_tier1 * tax_bracket_2_tier1 + tax_rate_tier2 * (tax_bracket_2_tier2 -  tax_bracket_2_tier1) + (tax_bracket_2_tier3-tax_bracket_2_tier2) * tax_rate_tier3 + (income - tax_bracket_2_tier3) * tax_rate_tier4
    elif income <= tax_bracket_2_tier5:
        tax = tax_rate_tier1 * tax_bracket_2_tier1 + tax_rate_tier2 * (tax_bracket_2_tier2 -  tax_bracket_2_tier1) + (tax_bracket_2_tier4-tax_bracket_2_tier3) * tax_rate_tier3 + (tax_bracket_2_tier4 - tax_bracket_2_tier3) * tax_rate_tier4 + (income - tax_bracket_2_tier4) * tax_rate_tier5
    elif income <= tax_bracket_2_tier6:
        tax = tax_rate_tier1 * tax_bracket_2_tier1 + tax_rate_tier2 * (tax_bracket_2_tier2 -  tax_bracket_2_tier1) + (tax_bracket_2_tier4-tax_bracket_2_tier3) * tax_rate_tier3 + (tax_bracket_2_tier4 - tax_bracket_2_tier3) * tax_rate_tier4 + (tax_bracket_2_tier5 - tax_bracket_2_tier4) * tax_rate_tier5 + (income - tax_bracket_2_tier5) * tax_rate_tier6
    else:
        tax = tax_rate_tier1 * tax_bracket_2_tier1 + tax_rate_tier2 * (tax_bracket_2_tier2 -  tax_bracket_2_tier1) + (tax_bracket_2_tier4-tax_bracket_2_tier3) * tax_rate_tier3 + (tax_bracket_2_tier4 - tax_bracket_2_tier3) * tax_rate_tier4 + (tax_bracket_2_tier5 - tax_bracket_2_tier4) * tax_rate_tier5 + (tax_bracket_2_tier6 - tax_bracket_2_tier5) * tax_rate_tier6 + (income - tax_bracket_2_tier6) * tax_rate_tier7
elif status == '4':
    if income <= tax_bracket_4_tier1:
        tax = tax_rate_tier1 * income
    elif income <= tax_bracket_4_tier2:
        tax = tax_rate_tier1 * tax_bracket_4_tier1 + (income-tax_bracket_4_tier1) * tax_rate_tier2
    elif income <= tax_bracket_4_tier3:
        tax = tax_rate_tier1 * tax_bracket_4_tier1 + tax_rate_tier2 * (tax_bracket_4_tier2 -  tax_bracket_4_tier1) + (income-tax_bracket_4_tier2) * tax_rate_tier3
    elif income <= 383900:
        tax = tax_rate_tier1 * tax_bracket_4_tier1 + tax_rate_tier2 * (tax_bracket_4_tier2 -  tax_bracket_4_tier1) + (tax_bracket_4_tier3-tax_bracket_4_tier2) * tax_rate_tier3 + (income - tax_bracket_4_tier3) * tax_rate_tier4
    elif income <= 487450:
        tax = tax_rate_tier1 * tax_bracket_4_tier1 + tax_rate_tier2 * (tax_bracket_4_tier2 -  tax_bracket_4_tier1) + (tax_bracket_4_tier4-tax_bracket_4_tier3) * tax_rate_tier3 + (tax_bracket_4_tier4 - tax_bracket_4_tier3) * tax_rate_tier4 + (income - tax_bracket_4_tier4) * tax_rate_tier5
    elif income <= 731200:
        tax = tax_rate_tier1 * tax_bracket_4_tier1 + tax_rate_tier2 * (tax_bracket_4_tier2 -  tax_bracket_4_tier1) + (tax_bracket_4_tier4-tax_bracket_4_tier3) * tax_rate_tier3 + (tax_bracket_4_tier4 - tax_bracket_4_tier3) * tax_rate_tier4 + (tax_bracket_4_tier5 - tax_bracket_4_tier4) * tax_rate_tier5 + (income - tax_bracket_4_tier5) * tax_rate_tier6
    else:
        tax = tax_rate_tier1 * tax_bracket_4_tier1 + tax_rate_tier2 * (tax_bracket_4_tier2 -  tax_bracket_4_tier1) + (tax_bracket_4_tier4-tax_bracket_4_tier3) * tax_rate_tier3 + (tax_bracket_4_tier4 - tax_bracket_4_tier3) * tax_rate_tier4 + (tax_bracket_4_tier5 - tax_bracket_4_tier4) * tax_rate_tier5 + (tax_bracket_4_tier6 - tax_bracket_4_tier5) * tax_rate_tier6 + (income - tax_bracket_4_tier6) * tax_rate_tier7
else:
    if income <= tax_bracket_1_tier1:
        tax = tax_rate_tier1 * income
    elif income <= tax_bracket_1_tier2:
        tax = tax_rate_tier1 * tax_bracket_1_tier1 + (income-tax_bracket_1_tier1) * tax_rate_tier2
    elif income <= tax_bracket_1_tier3:
        tax = tax_rate_tier1 * tax_bracket_1_tier1 + tax_rate_tier2 * (tax_bracket_1_tier2 -  tax_bracket_1_tier1) + (income-tax_bracket_1_tier2) * tax_rate_tier3
    elif income <= tax_bracket_1_tier4:
        tax = tax_rate_tier1 * tax_bracket_1_tier1 + tax_rate_tier2 * (tax_bracket_1_tier2 -  tax_bracket_1_tier1) + (tax_bracket_1_tier3-tax_bracket_1_tier2) * tax_rate_tier3 + (income - tax_bracket_1_tier3) * tax_rate_tier4
    elif income <= tax_bracket_1_tier5:
        tax = tax_rate_tier1 * tax_bracket_1_tier1 + tax_rate_tier2 * (tax_bracket_1_tier2 -  tax_bracket_1_tier1) + (tax_bracket_1_tier4-tax_bracket_1_tier3) * tax_rate_tier3 + (tax_bracket_1_tier4 - tax_bracket_1_tier3) * tax_rate_tier4 + (income - tax_bracket_1_tier4) * tax_rate_tier5
    elif income <= tax_bracket_1_tier6:
        tax = tax_rate_tier1 * tax_bracket_1_tier1 + tax_rate_tier2 * (tax_bracket_1_tier2 -  tax_bracket_1_tier1) + (tax_bracket_1_tier4-tax_bracket_1_tier3) * tax_rate_tier3 + (tax_bracket_1_tier4 - tax_bracket_1_tier3) * tax_rate_tier4 + (tax_bracket_1_tier5 - tax_bracket_1_tier4) * tax_rate_tier5 + (income - tax_bracket_1_tier5) * tax_rate_tier6
    else:
        tax = tax_rate_tier1 * tax_bracket_1_tier1 + tax_rate_tier2 * (tax_bracket_1_tier2 -  tax_bracket_1_tier1) + (tax_bracket_1_tier4-tax_bracket_1_tier3) * tax_rate_tier3 + (tax_bracket_1_tier4 - tax_bracket_1_tier3) * tax_rate_tier4 + (tax_bracket_1_tier5 - tax_bracket_1_tier4) * tax_rate_tier5 + (tax_bracket_1_tier6 - tax_bracket_1_tier5) * tax_rate_tier6 + (income - tax_bracket_1_tier6) * tax_rate_tier7

# Now print the year and the tax. 
print(f"Your tax for year {year} is : {tax}")

# Above we developed the program step by step, but we can wrap it up as a function and call it when need.
def gettax(status,income = 5000):
    year = 2024
    tax_rate_tier1 = 0.1
    tax_rate_tier2 = 0.12
    tax_rate_tier3 = 0.22
    tax_rate_tier4 = 0.24
    tax_rate_tier5 = 0.32
    tax_rate_tier6 = 0.35
    tax_rate_tier7 = 0.37

    tax_bracket_1_tier1 = tax_bracket_3_tier1 = 11600
    tax_bracket_1_tier2 = tax_bracket_3_tier2 = 47150
    tax_bracket_1_tier3 = tax_bracket_3_tier3 = 100525
    tax_bracket_1_tier4 = tax_bracket_3_tier4 = 191950
    tax_bracket_1_tier5 = tax_bracket_3_tier5 = 243725
    tax_bracket_1_tier6 = tax_bracket_3_tier5 = 609350

    tax_bracket_2_tier1 = 23200
    tax_bracket_2_tier2 = 94300
    tax_bracket_2_tier3 = 201050
    tax_bracket_2_tier4 = 383900
    tax_bracket_2_tier5 = 487450
    tax_bracket_2_tier6 = 731200

    tax_bracket_4_tier1 = 16550
    tax_bracket_4_tier2 = 63100
    tax_bracket_4_tier3 = 100500
    tax_bracket_4_tier4 = 191950
    tax_bracket_4_tier5 = 243700
    tax_bracket_4_tier6 = 609350
    if status == ('1' or '3'):
        if income <= tax_bracket_1_tier1:
            tax = tax_rate_tier1 * income
        elif income <= tax_bracket_1_tier2:
            tax = tax_rate_tier1 * tax_bracket_1_tier1 + (income-tax_bracket_1_tier1) * tax_rate_tier2
        elif income <= tax_bracket_1_tier3:
            tax = tax_rate_tier1 * tax_bracket_1_tier1 + tax_rate_tier2 * (tax_bracket_1_tier2 -  tax_bracket_1_tier1) + (income-tax_bracket_1_tier2) * tax_rate_tier3
        elif income <= tax_bracket_1_tier4:
            tax = tax_rate_tier1 * tax_bracket_1_tier1 + tax_rate_tier2 * (tax_bracket_1_tier2 -  tax_bracket_1_tier1) + (tax_bracket_1_tier3-tax_bracket_1_tier2) * tax_rate_tier3 + (income - tax_bracket_1_tier3) * tax_rate_tier4
        elif income <= tax_bracket_1_tier5:
            tax = tax_rate_tier1 * tax_bracket_1_tier1 + tax_rate_tier2 * (tax_bracket_1_tier2 -  tax_bracket_1_tier1) + (tax_bracket_1_tier4-tax_bracket_1_tier3) * tax_rate_tier3 + (tax_bracket_1_tier4 - tax_bracket_1_tier3) * tax_rate_tier4 + (income - tax_bracket_1_tier4) * tax_rate_tier5
        elif income <= tax_bracket_1_tier6:
            tax = tax_rate_tier1 * tax_bracket_1_tier1 + tax_rate_tier2 * (tax_bracket_1_tier2 -  tax_bracket_1_tier1) + (tax_bracket_1_tier4-tax_bracket_1_tier3) * tax_rate_tier3 + (tax_bracket_1_tier4 - tax_bracket_1_tier3) * tax_rate_tier4 + (tax_bracket_1_tier5 - tax_bracket_1_tier4) * tax_rate_tier5 + (income - tax_bracket_1_tier5) * tax_rate_tier6
        else:
            tax = tax_rate_tier1 * tax_bracket_1_tier1 + tax_rate_tier2 * (tax_bracket_1_tier2 -  tax_bracket_1_tier1) + (tax_bracket_1_tier4-tax_bracket_1_tier3) * tax_rate_tier3 + (tax_bracket_1_tier4 - tax_bracket_1_tier3) * tax_rate_tier4 + (tax_bracket_1_tier5 - tax_bracket_1_tier4) * tax_rate_tier5 + (tax_bracket_1_tier6 - tax_bracket_1_tier5) * tax_rate_tier6 + (income - tax_bracket_1_tier6) * tax_rate_tier7
    elif status == '2':
        if income <= tax_bracket_2_tier1:
            tax = tax_rate_tier1 * income
        elif income <= tax_bracket_2_tier2:
            tax = tax_rate_tier1 * tax_bracket_2_tier1 + (income-tax_bracket_2_tier1) * tax_rate_tier2
        elif income <= tax_bracket_2_tier3:
            tax = tax_rate_tier1 * tax_bracket_2_tier1 + tax_rate_tier2 * (tax_bracket_2_tier2 -  tax_bracket_2_tier1) + (income-tax_bracket_2_tier2) * tax_rate_tier3
        elif income <= tax_bracket_2_tier4:
            tax = tax_rate_tier1 * tax_bracket_2_tier1 + tax_rate_tier2 * (tax_bracket_2_tier2 -  tax_bracket_2_tier1) + (tax_bracket_2_tier3-tax_bracket_2_tier2) * tax_rate_tier3 + (income - tax_bracket_2_tier3) * tax_rate_tier4
        elif income <= tax_bracket_2_tier5:
            tax = tax_rate_tier1 * tax_bracket_2_tier1 + tax_rate_tier2 * (tax_bracket_2_tier2 -  tax_bracket_2_tier1) + (tax_bracket_2_tier4-tax_bracket_2_tier3) * tax_rate_tier3 + (tax_bracket_2_tier4 - tax_bracket_2_tier3) * tax_rate_tier4 + (income - tax_bracket_2_tier4) * tax_rate_tier5
        elif income <= tax_bracket_2_tier6:
            tax = tax_rate_tier1 * tax_bracket_2_tier1 + tax_rate_tier2 * (tax_bracket_2_tier2 -  tax_bracket_2_tier1) + (tax_bracket_2_tier4-tax_bracket_2_tier3) * tax_rate_tier3 + (tax_bracket_2_tier4 - tax_bracket_2_tier3) * tax_rate_tier4 + (tax_bracket_2_tier5 - tax_bracket_2_tier4) * tax_rate_tier5 + (income - tax_bracket_2_tier5) * tax_rate_tier6
        else:
            tax = tax_rate_tier1 * tax_bracket_2_tier1 + tax_rate_tier2 * (tax_bracket_2_tier2 -  tax_bracket_2_tier1) + (tax_bracket_2_tier4-tax_bracket_2_tier3) * tax_rate_tier3 + (tax_bracket_2_tier4 - tax_bracket_2_tier3) * tax_rate_tier4 + (tax_bracket_2_tier5 - tax_bracket_2_tier4) * tax_rate_tier5 + (tax_bracket_2_tier6 - tax_bracket_2_tier5) * tax_rate_tier6 + (income - tax_bracket_2_tier6) * tax_rate_tier7
    elif status == '4':
        if income <= tax_bracket_4_tier1:
            tax = tax_rate_tier1 * income
        elif income <= tax_bracket_4_tier2:
            tax = tax_rate_tier1 * tax_bracket_4_tier1 + (income-tax_bracket_4_tier1) * tax_rate_tier2
        elif income <= tax_bracket_4_tier3:
            tax = tax_rate_tier1 * tax_bracket_4_tier1 + tax_rate_tier2 * (tax_bracket_4_tier2 -  tax_bracket_4_tier1) + (income-tax_bracket_4_tier2) * tax_rate_tier3
        elif income <= 383900:
            tax = tax_rate_tier1 * tax_bracket_4_tier1 + tax_rate_tier2 * (tax_bracket_4_tier2 -  tax_bracket_4_tier1) + (tax_bracket_4_tier3-tax_bracket_4_tier2) * tax_rate_tier3 + (income - tax_bracket_4_tier3) * tax_rate_tier4
        elif income <= 487450:
            tax = tax_rate_tier1 * tax_bracket_4_tier1 + tax_rate_tier2 * (tax_bracket_4_tier2 -  tax_bracket_4_tier1) + (tax_bracket_4_tier4-tax_bracket_4_tier3) * tax_rate_tier3 + (tax_bracket_4_tier4 - tax_bracket_4_tier3) * tax_rate_tier4 + (income - tax_bracket_4_tier4) * tax_rate_tier5
        elif income <= 731200:
            tax = tax_rate_tier1 * tax_bracket_4_tier1 + tax_rate_tier2 * (tax_bracket_4_tier2 -  tax_bracket_4_tier1) + (tax_bracket_4_tier4-tax_bracket_4_tier3) * tax_rate_tier3 + (tax_bracket_4_tier4 - tax_bracket_4_tier3) * tax_rate_tier4 + (tax_bracket_4_tier5 - tax_bracket_4_tier4) * tax_rate_tier5 + (income - tax_bracket_4_tier5) * tax_rate_tier6
        else:
            tax = tax_rate_tier1 * tax_bracket_4_tier1 + tax_rate_tier2 * (tax_bracket_4_tier2 -  tax_bracket_4_tier1) + (tax_bracket_4_tier4-tax_bracket_4_tier3) * tax_rate_tier3 + (tax_bracket_4_tier4 - tax_bracket_4_tier3) * tax_rate_tier4 + (tax_bracket_4_tier5 - tax_bracket_4_tier4) * tax_rate_tier5 + (tax_bracket_4_tier6 - tax_bracket_4_tier5) * tax_rate_tier6 + (income - tax_bracket_4_tier6) * tax_rate_tier7
    print(f"Your tax for year {year} is : {tax}")




status = input(f'Please choose your tax status: 1 single; 2 Married file jointly; 3 married filling separately; 4 Head of household: ')
income = float(input('Please enter your income: '))

gettax(status,income)

gettax('1',50000)
gettax('2',50000)
gettax('4',50000)

