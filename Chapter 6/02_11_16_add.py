fruitInventory = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}
fruitCost = {"apples": 0.85, "bananas": 0.11, "oranges": 0.65, "pears": 0.70}
totalCost = 0
totalCost_2 = 0


valueOfFruit = 0

for fruit in  fruitInventory:
    valueOfFruit += fruitInventory[fruit] * fruitCost[fruit]
print(type(valueOfFruit))
print(valueOfFruit)

poop = fruitInventory['apples'] * fruitCost['apples']
print('---')
print(poop)

##for cost in fruitInventory.values():
##    totalCost += cost
##
##for fruit in fruitInventory:
##    totalCost_2 += fruitInventory[fruit]
##
##print(totalCost)
##
##print('------')
##
##print(totalCost_2)
