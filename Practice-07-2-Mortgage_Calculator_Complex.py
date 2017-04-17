interval = input("How often would you like your paying interval?(weekly, monthly, daily, continually)")
intrRate = float(input("Please enter interest rate: "))
mortG = float(input("Please enter fixed term mortgage: "))
montP = int(input("Please enter the amount you plan to pay in each interval: "))
payBack = 0
time = 0
intv = {"Weekly": "week(s)", "Monthly": "month(s)", "Daily": "day(s)", "Continually": "instance(s)"}
while mortG > payBack:
    payBack *= (1+intrRate)
    payBack += montP
    time += 1
print("It will take you " + str(time) + " " + intv[interval] + " to pay back the mortgage.")
