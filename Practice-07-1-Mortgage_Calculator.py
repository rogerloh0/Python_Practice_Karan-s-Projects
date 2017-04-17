intrRate = float(input("Please enter interest rate: "))
mortG = float(input("Please enter fixed term mortgage: "))
montP = int(input("Please enter the amount you plan to pay monthly: "))
payBack = 0
month = 0
while mortG > payBack:
    payBack *= (1+intrRate)
    payBack += montP
    month += 1
print("It will take you " + str(month) + " month(s) to pay back the mortgage.")
