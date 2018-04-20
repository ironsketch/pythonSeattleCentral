L = [1,2,3,4,5,6,7,8]
def productAcum(L):
    ''' Returns the product of the numbers in list L.  There is a bug in
this program.  Can you find it & fix it?
'''
    p = 1
    for n in L:
        p = p*n
    return p

print (productAcum(L))
