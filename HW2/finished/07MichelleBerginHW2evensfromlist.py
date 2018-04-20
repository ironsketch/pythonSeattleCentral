# Creating a def called, evensFromList that uses one parameter, listed
def evensFromList(listed):

    # Telling the user what is happening
    print('This will only print out the even numbers in a given int list.')

    # Creating a for loop using the list put in by the parameter
    # listed and traversing it with i
    for i in listed:

        # If the remainder left by dividing 2 in to the number
        # equals 0, then print the number with no ending line
        if i % 2 == 0 :

            # Printing each number with no new line character
            # Overiding what is by default a \n with _ one space
            print(i, end=' ')

    # Sometimes using end will have the program wait for next line
    # (how python knows to keep going) To combat that, printing
    # another line
    print('\nAll the EVENS!')

# Calling definition evensFromList and submitting one parameter,
# a list with range 10 numbers 0 - 9
evensFromList(list(range(10)))
