print("Welcome to the GCD(Greatest Common Divisor) calculator.")
num1 = int(input("Please enter your first number: "))
num2 = int(input("Now enter your second number: "))
if num2 > num1:
    num1, num2 = num2, num1
while num1 % num2 != 0:
    num2 -= 1
print("The greatest common divisor between the two number is " + str(num2))
