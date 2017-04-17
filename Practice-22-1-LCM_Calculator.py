print("Welcome to the LCM(Least Common Multiple) calculator.")
num1 = int(input("Please enter your first number: "))
num2 = int(input("Now enter your second number: "))
if num2 > num1:
    num1, num2 = num2, num1
testNum = num2
while num1 % testNum != 0:
    testNum -= 1
lcm = int((num1 / testNum) * (num2 / testNum) * testNum)
print("The least common multiple between the two number is " + str(lcm))
