def removeDupsFrom1(L):
    '''
Takes a list L and returns a list without duplicates.
Modifies orig list.
'''
    a = removeDupsFrom2(L)
    L[:] = a # Note that L = a does not work.
             
    
def removeDupsFrom2(L):
    '''
Takes a list L and returns a list without duplicates.
create empty list accumulator 
for each element in L
  if element not in L
      put element into list accumulator
return list accumulator  .
Does not modify orig list.    
'''
    L1 = []  ## initialize list to return
    for el in L:
        if el not in L1:  ## put in L1 only if not already there
            L1.append(el)
    return L1  ## in same order as L
        
#L = [1,2,2,3]
#print('L = ',L)
#removeDupsFrom1(L)
#print('L = ',L)
#print()
#L = [1,2,2,3]
#print('L = ',L)
#removeDupsFrom2(L)
#print('L = ',L)
#print()
#
#L =  [1, 2, 2, 3]
#L =  [1, 2, 3]
#
#L =  [1, 2, 2, 3]
#L =  [1, 2, 2, 3]