# Setting up a true list
alphaList = ['apple','bears','dsshole']

# Setting up a false list (Will return False)
numCheck = [0,1,2,3,60,5,6,7,8,50]

def is_sorted(L):

    # Sorts the given list into a new list, new
    new = sorted(L)

    # Does the old list and new equal each other?
    if new == L:

        # Yes return true
        return True
    else:

        # No return False
        return False

print(is_sorted(alphaList))
print(is_sorted(numCheck))
