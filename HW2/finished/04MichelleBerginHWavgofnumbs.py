
# Creating the main definition
def main():

    # Telling the user what this does
    print('This will calculate the average of your numbers')

    # Initializing how many times we will need to run a loop to gather data
    times = eval(input('How many numbers will you be inputting?: '))

    # Initializing variable to add all numbs together
    allTogether = 0

    # For loop in the range defined by user, earlier
    for i in range (times):

        # Asking for input from user each time it runs through
        num = eval(input('Enter your number: '))

        # Adding to allTogether that number which started at 0
        # Each itteration adding a new number submited by user
        # To it's self, allTogether
        allTogether += num

    # Dividing all the added numbers by time number of times
    # The user previously stated
    allTogether /= times

    # Printing divded number
    print('\nThe sum for all yer numbers is: ', allTogether)

# Calling main method
main()
