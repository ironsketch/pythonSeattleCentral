''' My YouTube video addy is:
    https://www.youtube.com/watch?v=GAaSUhPunzM&feature=youtu.be
'''

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

# The main function of the program
def main():
    print ('Find your average score!')
    print ()

    # Asking user for 3 inputs and consecutively assigning them to
    # the 3 variables to the left
    s1, s2, s3 = eval(input("Enter 3 scores separated by commas: "))

    # The math to find an average of 3 numbers
    a = (s1 + s2 + s3) / 3

    # Printed answer with truncation of the float
    print ("Your average is: %.2f" % a)

# Calling the main method to run app
main ()

# The main function of the program
def main():

    # Running a for loop 5 times
    for i in range(5):

        # Getting user input each time
        celsius = eval(input("Type in the temp in Celsius: "))

        # Cels to Fahr converter
        fahrenheit = 9.0 / 5.0 * celsius + 32

        # If else conditional to determine unnacceptable answers
        if (fahrenheit > 100):
            print("Gerd Dam dats hot!")
        elif (fahrenheit < 10):
            print("Damn dat cold!")
        else:
            print("meh")
        print("The temp is", fahrenheit, "degrees")
        print()
        
# Calling the main method to run app
main()

# The main function of the program
def main ():
    
    print('Calcuclate your yearly investment!')
    print()

    # Getting 3 inputs from the user and assigning each to a variable
    payment = eval(input('Enter your investment each year: '))
    intrate = eval(input('Enter your interest rate: '))
    years = eval(input('Enter the years that have or will pass: '))

    # Initializing the variable principal at 0.0
    principal = 0.0

    # For loop to calculate the principal based on user input
    for i in range(years):
        principal = (principal + payment) * (1 + intrate)
        
    # Print out of completion of the for loop
    # %.2f % prinicipal truncates the float to 2 decimal places
    print('In ', years, " years you'll have: %.2f" % principal)

main()

# Creating my main function
def main ():

    # Putting text out to inform user of what we will do
    print('Find out your average temprature!')

    # Empty line
    print()

    # Taking in 3 inputs from the user and assigning them to variables
    fahr1 = eval(input('Enter your first Fahrenheit: '))
    fahr2 = eval(input('Enter your second Fahrenheit: '))
    fahr3 = eval(input('Enter your third Fahrenheit: '))

    # The equation to average the 3 inputs and assigning it to a variable
    average = (fahr1 + fahr2 + fahr3) / 3

    # Printing out the variable average after it has been calculated
    print ('Your average is: %.1f' % average)

    # Sending the average to a def I have created that calculates
    # fahrenheit to celsius and prints it out
    # The %.1f prints out the float with 1 decimal place
    # conv(average) conv is the def I am calling, average is the
    # variable I am passing through
    print ('Your average in celsius: %.1f' % conv(average))
    print ('Here are your inputs in celsius: ')
    print ('%.1f' % conv(fahr1), '%.1f' % conv(fahr2), '%.1f' % conv(fahr3))

    
# The definition I created to calculate Fahr to Cels
# I created a definition because I was going to be using the
# math equation often and instead of writing it over and over
# I write it once and pass my data through it
def conv (fahrnum):

    # The math equation to convert fahr to cels it stores the output
    # to the variable cels
    cels = (fahrnum - 32) * 5 / 9

    # Returns data in the variable cels so that it may be printed
    return cels

main()

