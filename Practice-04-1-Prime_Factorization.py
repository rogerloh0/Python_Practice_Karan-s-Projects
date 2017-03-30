def primeTest(num):
    fact = num - 1
    while fact > 1:
        if num % fact != 0:
            fact -= 1
        else:
            return False
    if fact == 1:
        return True

X = input("Enter the number you wish to test: ")
testNum = int(X)
Factlist = []
testFact = testNum - 1
n = 1
print(type(testFact))
while testFact > 1:
    if testNum % testFact == 0 and primeTest(testFact):
        print(testFact)
        Factlist.append(testFact)
        n += 1
    testFact -= 1
print(Factlist)
print(Factlist[::-1])
    
