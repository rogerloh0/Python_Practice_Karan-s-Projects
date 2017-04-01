def primeTest(num):
    fact = num - 1
    while fact > 1:
        if num % fact != 0:
            fact -= 1
        else:
            return True
    if fact == 1:
        return False
num = 2
ans = input("Do you wish to know the next prime number?(Y/n)")
while ans == "Y":
    while primeTest(num):        
        num+=1
    print(num)
    num+=1
    ans = input("Do you wish to know the next prime number?(Y/n)")
    if ans == "n":
        break
