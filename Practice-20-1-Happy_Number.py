num = 1
hpNumCount = 0
hpNumList = []
while hpNumCount <= 8:
    digList = list(str(num))
    newNum = 0
    print(num)
    while len(digList) >= 1:
        for i in digList:
            newNum += int(i)
        digList = list(str(newNum))
        print(digList)
        if len(digList) > 1:
            newNum = 0
        elif len(digList) == 1:
            break
    if newNum == 1:
        hpNumCount += 1
        hpNumList.append(str(num))
    num += 1
    newNum = 0
print(hpNumList)
