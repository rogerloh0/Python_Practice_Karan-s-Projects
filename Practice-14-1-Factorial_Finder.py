def factFunc(num):
    if num >= 2:
        #print(num)
        #print(type(num))
        return num * int(factFunc(num - 1))
    else:
        return num

print("Welcome to the Factorial Finder")
print("=====================================")
ini_num = int(input("Please enter the initial integer: "))
result = 0
if ini_num == 0:
    print(1)
elif ini_num > 0:
    print(factFunc(ini_num))
else:
    print("The initial integer must be an integer larger than zero.")
