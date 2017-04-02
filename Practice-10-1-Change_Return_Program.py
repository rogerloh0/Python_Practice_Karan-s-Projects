cost = float(input("Please enter the cost of the prodcut: "))
pay = float(input("Please enter the amount of money paid: "))
change = pay - cost
coinVal = {'quarter': 0.25, 'dime': 0.1, 'nickel': 0.05, 'penny': 0.01}
coinAmnt = {'quarter': 0, 'dime': 0, 'nickel': 0, 'penny': 0}
coinList = ['quarter', 'dime', 'nickel','penny']
n = 0
while n < 4:
    #print(coinVal[coinList[n]])
    #print(change)
    if change >= coinVal[coinList[n]]:
        #print("I'm here")
        coinAmnt[coinList[n]] = change//coinVal[coinList[n]]
        change = change % coinVal[coinList[n]]
    print(str(coinList[n]) + ": " + str(int(coinAmnt[coinList[n]])))
    n += 1
