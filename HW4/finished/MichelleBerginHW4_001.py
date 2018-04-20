'''Write definitions for the following two functions:
sumN(n) returns the sum of the first n natural numbers.
sumNCubes(n) returns the sum of the cubes of the first
n natural numbers. Then use these functions in a program
that prompts a user for n and prints out the sum of
the first n natural numbers and the sum of the cubes
of the first n natural numbers.'''

#01
################################################
##         Zelle 6.4.  sumN,sumNCubes         ##
################################################

# Takes one parameter and
def sumN(n):
    added = 0

    # Uses it as the range (+1 to get the actual total)
    for num in range(1,n + 1):

        # Adding the num from the range to the established variable
        added += num

    # Returns total added
    return added

# Takes one parameter and
def sumNCubes(n):
    added = 0

    # Uses it as the range (+1 to get the actual total)
    for num in range(1,n + 1):

        # First I cube each num
        cubed = num**3

        # And THEN I added it to the variable
        added += cubed

    # Then I return the total sum
    return added

def main():

    # Taking info from user
    userNum = eval(input('Please enter a number > than 0 and not a float: '))
    print('Your number with all previous natural numbers added up is:')

    # Calls definition and sends one parameter (user input)
    print(sumN(userNum))
    print('Your numbers cubed and added up')

    # Calls definition and sends one parameter (user input)
    print(sumNCubes(userNum))

main()
