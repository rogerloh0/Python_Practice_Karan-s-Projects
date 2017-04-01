DecNum = int(input("Please enter the decimal number: "))
BinNum = []
n = 0
while 2**n < DecNum:
    n += 1
n -= 1
while n > -1:
    if DecNum >= 2**n:
        DecNum -= (2**n)
        BinNum.append('1')
    else:
        BinNum.append('0')
    n -= 1
print(int("".join(BinNum)))
#print("The binary form of this number is " + str(BinNum))
