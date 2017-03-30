num1 = 0
num2 = 0
printNum = 1
Fibonacci = []
X = input("How many Fibonacci would you like: ")
seq = int(X)
while seq > 0:
    print(printNum)
    Fibonacci.append(printNum)
    num2 = num1
    num1 = printNum
    if num1 + num2 == 0:
        printNum = 1
    else:
        printNum = num1 + num2
    seq-=1
print(Fibonacci)
    
