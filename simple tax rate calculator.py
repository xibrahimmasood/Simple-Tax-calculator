income = float(input('Enter your income'))
tax_rate = float(input('Enter tax rate %'))
my_taxes = income * tax_rate/100
print(f'Your taxes are {my_taxes}')
in_hand = income - my_taxes
print(f'Your income after taxes is {in_hand}')