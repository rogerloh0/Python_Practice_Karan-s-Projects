import random
choice = "Y"
results = {"head": 0, "tail": 0}
while choice != "n":
    choice = input("Flip the coin?(Y/n))")
    if choice == "Y" or choice == "y":
        rand = random.randint(0,1)
        if rand == 1:
            results["head"] += 1
        elif rand == 0:
            results["tail"] += 1
    print(results)
