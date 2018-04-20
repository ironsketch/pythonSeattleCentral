'''Write and test a function to meet this specification.
toNumbers(strList) strList is a list of strings, each of
which represents a number. Modifies each entry in the
list by converting it to a number.'''

#04
################################################
##          Zelle 6.13 - toNumbers            ##
################################################

# Setting up a dictionary to easily switch from the text
# format of a number to it's int equivalence
numbDict = {'one': 1, 'two': 2, 'three': 3, 'four': 4,
            'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
            'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12};

# The initial List to modify
L = ['one','two','three','Four','five','ten','sIX','seven']

# The def that will manipulate list (1 param)
def toNumbers(List):

    # Initializing counter for use in updating List
    counter = 0

    # Iterating through the list to modify each entry
    for item in List:

        # Updating item to reflect the corrasponding result
        # of each dictionary lookup
        item = numbDict[item.lower()]

        # Updating the list to the new data
        List[counter] = item
        counter += 1

    # Returning the new List
    return List

# Printing the List before
print(L)

# updating the old list to the new one
L = toNumbers(L)

# Printing the new one
print(L)
