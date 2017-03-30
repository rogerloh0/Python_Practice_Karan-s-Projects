print("Please enter the dimension of each tile")
tileW = float(input("Enter tile width: "))
tileH = float(input("Enter tile height: "))
tileCost = float(input("Please enter the cost of each tile:(Unit: NTD) "))
print("///////////////////////////////////////")
print("Please enter room dimension")
roomW = float(input("Enter room width: "))
roomH = float(input("Enter room height: "))
roomArea = roomW * roomH
tileArea = tileW * tileH
tileNum = roomArea/tileArea
totalCost = tileNum * tileCost
print(totalCost)
