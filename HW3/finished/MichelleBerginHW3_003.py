def main():

    # Setting up a variable with the alphabet so that I can use it
    # to count 1 - 26 for the program (faster and less code)
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    # Setting up a variable to start at 0
    added = 0

    # take in users word
    word = input('Please enter a word to calculate. ')

    # Iterating through all letters in the word entered
    for letter in word:

        # using place as a variable to store the index of the
        # letter found
        place = alpha.find(letter)

        # Adding it to the variable added. But adding 1 place
        # since an index starts at 0 not 1
        added += (place + 1)

    # Printing result
    print (added)

main()
