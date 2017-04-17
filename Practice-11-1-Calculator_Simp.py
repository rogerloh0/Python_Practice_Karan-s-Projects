num1 = float(input("Please enter the first number: "))
num2 = float(input("Please enter the second number: "))
oper = input("Please choose your operation:(add, subtract, multiply, division)")
add = lambda x, y: x + y
sub = lambda x, y: x - y
mul = lambda x, y: x * y
div = lambda x, y: x / y
if oper == 'add':
    ans = add(num1, num2)
elif oper == 'subtract':
    ans = sub(num1, num2)
elif oper == 'multiply':
    ans = mul(num1, num2)
elif oper == 'division':
    ans = div(num1, num2)
else:
    print("Operation not recognized")
print("The answer is: " + str(ans))
