def main():

    # Setting up a blank variable
    acronym = ''

    # Getting the phrase from the user and it will be stored as a string
    phrase = input('Please input a phrase to make into an acronym. ')

    # I am going to process the string and split the words at the spaces
    # This turns it into a list
    process = phrase.split(' ')

    # Running through the list for each word
    for word in process:

        # Adding the first letter of each word to the variable acronym
        acronym += word[0]

    # Printing out the rest in upper case
    print(acronym.upper())
    
main()
