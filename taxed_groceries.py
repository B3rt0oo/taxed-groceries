# This program will provide the total after sales tax
# on any purchase in alabama
# assuming an eight percent sales tax added to all sales.

# Get the users pre-taxed dollar amount spent on groceries
sale = float(input('How much did you spend on groceries before taxes today?: '))
# Take the pre-taxed dollar amount and add eight percent sales tax
al_tax = 0.08
tax = sale * al_tax
total = sale + tax
#Display after user input and calculations
print('You typed in', sale)
print("Assuming you're in Alabama, the sales tax is eight percent.")
print(f"The total for your purchases today after sales tax is: ${total:.2f}")
total = f"${sale * al_tax: .2f}"
