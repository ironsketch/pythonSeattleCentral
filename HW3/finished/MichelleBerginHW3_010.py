# My stupid list
L = [0,0,1,1,1,2,3,4,5,6,6,6,6,7,8,9,1,9,9,9,9,9,9,9]

L2 = ['bear','bear','cat']

def removeDupsFrom(L):

    # We don't want to somehow affect the original List
    # To stay on the safe side I will assign a new variable
    A = L

    # Iterate through all items in list A
    for item in A:

        # Count how many times each item appears
        count = A.count(item)

        # If there is more than 1
        if count > 1:

            # Then for each of itteration of that item
            # remove it from the list, minus 1. We don't
            # want to remove them all
            for i in range(count - 1):

                # The command to remove the item
                A.remove(item)
    # Returning the new list A to see that it is working
    return A

print(L)
print(removeDupsFrom(L))
print(L2)
print(removeDupsFrom(L2))
