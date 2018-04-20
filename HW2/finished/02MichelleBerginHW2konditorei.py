# Friendly printout to tell you where you are.
print('Welcome to the Konditorei Coffee ordering program')

# Empty space
print()

# Submitting user input into variable pounds
pounds = eval(input('How many pounds of coffee will satiate your needs?: '))

# Definition to calculate cost with 1 parameter
def calcCost(pounds):

    # Calculate just the per pound cost
    coffeeCost = (pounds * 10.50)

    # Calculate shipping cost
    shippingCost = (pounds * .86) + 1.50

    # Adding both together to give customer total cost with coffee and shipping
    totalCost = coffeeCost + shippingCost

    # Print out of totals so customer is aware of impending doom
    print ('Your total cost for everything is: ${totalCost:.2f}'.format(**locals()))
    print ('Your total cost for coffee is: ${coffeeCost:.2f}'.format(**locals()))
    print ('Your total cost for shipping is: ${shippingCost:.2f}'.format(**locals()))

# Calling definition calcCost with input of one parameter as defined by user
calcCost(pounds)
