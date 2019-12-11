


def intInput():
    good_input = False
    while good_input == False:
        good_value = input()
        try:
            val = int(good_value)
            good_input = True
        except ValueError:
            print("Please enter a number.")
    return good_value

def percent(part, denom):
    if denom != 0: #never divide by zero even if user tries
        return (float(part) / float(denom))

def prompt(expense):
    bill = [
    "Facility Rent", "renters insurance", "Employee Fees", "electricity", "natural gas",
    "RX Medicine Orders", "Provider Insurance", "Emergency Funds",
    "Please enter the average amount you will lose in insurance writeoffs:",
    "Facility Lawsuits",
    "Facility Donations",
    "Please enter the average amount of your miscellaneous expenses each month:"    ]
    if expense == 0 or expense == 1:
        print("Please enter the amount you will pay for " +
                bill[expense] + " each month:")
    elif expense > 1 and expense < 8:
        print("Please enter the average amount you will pay for "
                + bill[expense] + " each month:")
    elif expense == 9 or expense == 10:
        print("Please enter the average amount you will spend on " +
                bill[expense] + " this month:")
    elif expense == 8 or expense == 11:
        print(bill[expense])
    elif expense > 99 and expense < 108 or expense == 109 or expense == 110:
        print("Percentage of "+bill[expense-100]+" to total expenses: " +
        str(percent(monthly_total[expense-100], sum(monthly_total))))
    elif expense == 108:
        print("Percentage of insurance writeoffs: " +
        str(percent(monthly_total[expense-100], sum(monthly_total))))
    else:
        print("Percentage of miscellaneous purchases to total expenses: "+
        str(percent(monthly_total[expense-100], sum(monthly_total))))

#main program
name = input("Please enter your name: ")
monthly_total = []
for i in range(12):
    prompt(i)
    monthly_total.insert(i, int(intInput()))
income_req = ((sum(monthly_total)) * 12) / .7
print("\nBudget Analysis Prepared For: " + name)
print("Your total monthly expense is: " + str(sum(monthly_total)))
for i in range(100,112):
    prompt(i)
print("Your total expenses for the year are:\n" + str(sum(monthly_total * 12)))
print("Given a 30% tax rate, to cover the office expenses"+
      " you must make a profit of:\n" + str(income_req))
