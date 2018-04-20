

def getOrder():
    orders = {}
    print('What is the food item, number ordered and cost')
    print('EX: vanillashake 4 3.75')
    print('Spaces dictate separate entries')
    print('Hit enter to submit')
    userInput = 'meow'
    while userInput != '':
        userInput = input('Order: ')
        uIprocess = userInput.split(' ')
        item,amount,cost = uIprocess[0],uIprocess[1],uIprocess[2]
        if uIprocess[0] in orders:
            orders[item][0] += int(amount)
        else:
            orders[item] = float(amount),float(cost)
    return orders

def main():
    order = getOrder()
    print('{:<30}{:>20}{:>20}'.format('Item','# Ordered','Cost'))
    print('{}'.format('-'*50))
    for item in order:
        print('{:<30}{:>20}{:>20}'.format(item,item[0],item[0] * item[1]))

main()
