# Setting up the two lists to append to out side all functions
# So that they can be seen by all... scope?
negative = []
positive = []

# Creating a seperate definition to handle sorting
def sort(l):

    # Traversing through the list submitted as a parameter
    # Designated by l
    for i in l:

        # If i is less than 0, it has to be negative
        if i < 0:

            # Appending those mean negatives to a list called negative
            negative.append(i)

        # Which means all other possibilities are either + or 0
        else:

            # Appending the wayward +'s to a list called positive
            positive.append(i)

# Creating a main function to run the main program
def main():

    # Telling the user what we 'bout to do
    print('This will sort out all your negative numbers')
    print('and all your positive numbers into 2 lists')

    # Commanding the user to obey. Entering a list of numbers
    # Which python is so kind to already know to treat it as a list!
    sortme = eval(input('Enter numbers seperated only by commas: '))

    # Passing that new list, sortme, as a parameter to the def, sort
    sort(sortme)

    # Because I am lazy, printing the raw format of both lists
    print(negative)
    print(positive)

main()

