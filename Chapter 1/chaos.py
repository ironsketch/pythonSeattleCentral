# Start the main definition
def main():
    x2 = 3.444

# Just a message printed out that explains to the user
    print ("A chaotic function")

# Asking and getting user input on how many iteratetions they would like
# and placing that in the variable numerate
    numerate = input("How many times would you like to run the numbers?: ")

# Asking the user to input a number and placing the amount in a variable x
    x = (input("Input a number from 0 to 1: "))

# A for loop using a range defined by the user
    for i in range(numerate):

# The mathmatical equation that we will use to process the user x input
        x = 3.9 * x * (1 - x)

# Prints out the out put after the equation has processed
        print("%.3f" % x)

# Now we call the main definition and it processes! everything above!
main()
