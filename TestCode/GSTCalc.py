import locale
locale.setlocale(locale.LC_ALL, '')

def GSTCalculator(total):
    GST = 3*(total/23)
    return GST

def display(total):
    print("\t\t-------------------------")
    print("\t\tTotal:\t\t",locale.currency(total))
    print("\t\tGST Amount:\t",locale.currency(GSTCalculator(total)))
    print("\t\tSub Total:\t",locale.currency(total-GSTCalculator(total)))
    print("\t\t-------------------------\n")

many = input("Is there more than one? (Y/N) ")
print()
if (many == "y" or many == "Y"):
    while(True):
        totalAmount = input("\tPlease Enter the Total amount or enter to cancel: ")
        display(abs(float(totalAmount)))
else:
    totalAmount = input("\tPlease Enter the Total amount: ")
    display(abs(float(totalAmount)))
    input("Press Enter To Exit")
