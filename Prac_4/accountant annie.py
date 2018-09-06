def main():
    total = []
    months = int(input("How many months would you like to log: "))
    for month in range(1, months+1):
        income = float(input("What was your income for month {}:  ".format(month)))
        total.append(income)

    display(total)

def display(total):
    sum = 0
    for month, income in enumerate(total):
        sum += income
        print("Month {:2} --- Income = {:12.2f} --- Income to date = {:12.2f}".format(month+1, income, sum))
main()