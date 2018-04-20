def is_sorted(L):
    '''
Returns True if list L is sorted.
Othewise returns False.
make copy of list
sort the copy
if the copy and the original list are the same,
  the original list is sorted
'''
    L1 = L[:] ## make copy of L; L.sort() returns None
    L1.sort()
    return L == L1

def is_sorted1(L):
    Lng = len(L)
    for i in range(Lng-1):
        if L[i] > L[i+1]:
            return False
    return True ## notice this can't be in the for loop.

#L1 = [2,5,3]
#L2 = [2,3,5]
#print(is_sorted(L1))
#print(is_sorted(L2))
#print()
#print(is_sorted1(L1))
#print(is_sorted1(L2))
#
#False
#True
#
#False
#True
#>>> 