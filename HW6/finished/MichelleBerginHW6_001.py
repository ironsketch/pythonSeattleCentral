#01
################################################
##                  Zelle 8.1                 ##
################################################

def fib(n):

    # Setting up the first two numbers of the Fibinacci sequence
    L = [1,1]

    # Go through n number of times
    for i in range(1,n):

        # A will equal the last two numbers of the List
        # and will iterate through the list using i
        a = L[i - 1] + L[i]

        # Then I append those numbers
        L.append(a)
        print(L)
        
fib(20)
