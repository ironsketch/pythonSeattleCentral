# Start the main definition
def main():
    threeNine = 3.9
    twoZero = 2.0
    x = .5
    y = .5
    
    def chaos(num, num2):
        x = num * x * (1 - x)
        y = num2 * y * (1 - y)

# Just a message printed out that explains to the user
    print ("A chaotic function")

# Asking and getting user input on how many iteratetions they would like
# and placing that in the variable numerate
    numerate = eval(input("How many times would you like to run the numbers?: "))

# Asking the user to input a number and placing the amount in a variable x
    print('\tFirst', '\tWith 2.0 instead of 3.9')
    print('-------------------------------')
    linenum = 1

# A for loop using a range defined by the user
    for i in range(numerate):

# The mathmatical equation that we will use to process the user x input
        chaos (threeNine, twoZero)
# Prints out the out put after the equation has processed
        
        print(linenum, '\t%.3f' % x, end=" ")
        print('|', end=" ")
        print('%.3f' % y, end=" ")
        print('\t2.0')
        linenum = linenum + 1

# Now we call the main definition and it processes! everything above!
    
main()
