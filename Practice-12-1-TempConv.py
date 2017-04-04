#Temperature Converter
Uin = input("Please enter the unit you'll be entering in: ")
Uout = input("Please enter the unit you wish to convert to: ")
inV = float(input("Please enter your value: "))
uList = {'Celsius': 1, 'Fahrenheit': 2, 'Kelvin': 3}
convType = int(str(uList[Uin]) + str(uList[Uout]))
if convType == 12: 
    #C2F
    outV = (inV / 100) * 180 + 32
elif convType == 13:
    #C2K
    outV = inV + 273.15
elif convType == 21:
    #F2C
    outV = ((inV - 32) / 180)*100
elif convType == 23:
    #F2D
    outV = (((inV - 32) / 180)*100)+273.15
elif convType == 31:
    #K2C:
    outV = inV - 273.15
elif convType == 32:
    #K2F:
    outV = ((inV - 273.15) / 100) * 180 + 32
else:
    print("This conversion is invalid")
    
#print(convType)

if convType % 10 == 1:
    dispU = "degree Celsius"
elif convType % 10 == 2:
    dispU = "degree Fahrenheit"
elif convType % 10 == 3:
    dispU = "Kelvin"
else:
    print("The unit is unrecognizable.")
     
print("Result: " + str(outV) + " " + dispU)
