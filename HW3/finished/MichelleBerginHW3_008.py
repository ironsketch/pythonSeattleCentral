'''
8.  Write a function, is_sorted(L), which takes a list as a
    parameter & returns True if the list is sorted, OTW
    returns False.

    I am not quite sure what is being asked of me but I
    assume you are asking us to check to see if a list
    given is numerical or alphabetical and if it is
    in numerical order or alphabetical order?
'''

# Setting up a false list
alphaList = ['apple','zears','dsshole']

# Setting up my comparitor to find if the order is alphabetical
alphaCheck = 'abcdefghijklmnopqrstuvwxyz'

# Setting up a false list (Will return False)
numCheck = [0,1,2,3,60,5,6,7,8,50]

# Checks to see if number is in order
def numOrder(check):
    indx = 0
    indx2 = 0

    # For number in the range of the list length
    for i in range (len(check)):

        # Assign indx to be what the first item in the list Check is
        indx = check[i]

        # If indx is bigger than or equal to indx2 (which at the
        # beginning it is designed to be) 
        if indx >= indx2:

            # Then assign indx2 with what indx is. That way the next
            # time around if what is in check is smaller than indx2
            # You will know that it is NOT in numerical order
            indx2 = indx
        else:

            # Returns false if the above conditions are met
            return False
    # Returns true if and only if all iterations of the List have been
    # completed without going to the else 
    return True

# Same idea as the above numerical one except I compare the letter to a
# string of alphabet and use the index to compare.
def alphaOrder(check):
    indx = 0
    indx2 = 0
    for item in check:
        indx = alphaCheck.find(item[0])
        if indx >= indx2:
            indx2 = indx
        else:
            return False
    return True
def main():
    print(numOrder(numCheck))
    print(alphaOrder(alphaList))

main()
