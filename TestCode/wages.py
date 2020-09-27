import locale
locale.setlocale(locale.LC_ALL, '')

print("\t PaySlip")
print

rate = 18.00
hours = (float)(input("Hours worked:\t\t "))
wages = rate * hours
casual = wages * 0.08
gross = wages + casual
kiwisaver = gross * 0.03
tax = gross * 0.118868549264
tithing = gross * 0.1
home = gross - kiwisaver - tax - tithing

print("Rate:\t\t\t"+locale.currency(rate))
print("Wages:\t\t\t"+locale.currency(wages))
print("Casual Holiday Pay:\t"+locale.currency(casual))
print("Gross:\t\t\t"+locale.currency(gross))
print("Kiwi Saver (3%):\t"+locale.currency(kiwisaver))
print("Tax:\t\t\t"+locale.currency(tax))
print("Tithing:\t\t"+locale.currency(tithing))
print("Take Home Pay:\t\t"+locale.currency(home))
print

print("Expenditures")

input("Press Enter to Close Program")
