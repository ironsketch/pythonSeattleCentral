# Creating a definition that takes in 3 parameters
def isTriangle(a,b,c):

    # Creating an if/else statement
    # If any of these conditions are met then print
    if a >= b + c or b >= a + c or c >= a + b:
        print('This triangle is not possible, you FOOL!')
    # Otherwise all others print this
    else:
        print('This is a lovely little triangle')

# Calling the def isTriangle 3 times. Each time testing
# the outcome
isTriangle(3,4,5)
isTriangle(2,2,2)
isTriangle(2,3,5)
