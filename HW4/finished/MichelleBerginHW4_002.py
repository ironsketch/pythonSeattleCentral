'''An acronym is a word formed by taking the first letters of the
words in a phrase and making a word from them. For example, RAM is
an acronym for “random access memory.” Write a program that allows
the user to type in a phrase and then outputs the acronym for that
phrase. Note: the acronym should be all uppercase, even if the
words in the phrase are not capitalized.'''

#02
################################################
##            Zelle 6.10 – acronym            ##
################################################

# Definition to process the user input with 1 parameter
def acro(userString):

    # Initializing variable to store acronym
    acronym = ''

    # Splitting the string with spaces
    manipulate = userString.split(' ')

    # Running through each word that was split
    for word in manipulate:

        # Taking the first character of each word and appending
        # it to acronym
        acronym += word[0]

    # Returning the result and making it uppercase
    return acronym.upper()

def main():

    # Getting user input
    userString = input('Enter in a phrase: ')

    # Printing result of passed data
    print(acro(userString))

main()

