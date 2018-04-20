fruitInventory = {"apples": [430,0.85], "bananas": [312,0.11],
                  "oranges": [525,0.65], "pears": [217,0.70]}

totalCost = 0

for fruit in fruitInventory:
    totalCost += fruitInventory[fruit][0] * fruitInventory[fruit][1]
print(totalCost)
for poop in fruitInventory.items():
    print(poop)
for poop in fruitInventory.values():
    print(poop)
