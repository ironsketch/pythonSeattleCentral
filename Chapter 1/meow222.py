
# The main function of the program
def main():

    #Setting up my variables to be used
    threeNine = 3.9
    twoZero = 2.0
    x = .153
    y = .153
    lineNum = 1

    print ('A Chaotic Function')

    # Taking user input (evaluated is for integers)
    butt = eval(input('How many times shall I run the numbers, Sir?'))

    print ('\tFirst', '\tUsing 2.0 in Chaos')
    print('--------------------------------------')

    # For loop witht he range set previously by user
    for i in range (butt):

        # The math for doing Chaos at 3.9 and then at 2.0
        x = 3.9 * x * (1 - x)
        y = 2.0 * y * (1 - y)

        # Printing the line number then the outcome of x
        # Then the out come of y. Why? because you gotta.
        print(lineNum, '\t%.3f' % x, end=" ")
        print('|', end=" ")
        print(y)

        # increasing line number for each itteration
        lineNum = lineNum + 1

# Calling the primary definition to run this program
main ()
