'''Find all perfect numbers <=10,000.
   A positive int > 1 is perfect if it equals
   the sum of its factors starting with 1 but not
   including the number itself.
   For EX. 8 is not since 1+2+4 != 8.'''

#YouTube
################################################
##                   YouTube                  ##
################################################

def factorsOf(n):
    factors = []

    # for each number leading up to n
    for i in range(1,n):

        # See if the remainder is 0
        if n % i == 0:

            # Yes: append it to list factors
            factors.append(i)

    # Then return the list
    return factors

def isPerfect(n):

    # This will return all factors of n
    factors = factorsOf(n)
    added = 0

    # For each factor of the original n add them up to see
    # if they:
    for i in factors:
        added += i

    # equal the original number
    if added == n:

        # If they do thenn we return true and the factors and the added amount
        return factors,True,added
    else:

        # We return not true etc.
        factors = 'Not a Perfect'
        return factors,False,added

def ListOfPerfectNums():

    # Formated
    print('{:^7}:  {:^60}  :{:^7}:  {:^7}'.format('Numb','Factors','Perfect?','Equals too'))
    print("-"*100)

    # From number 1 to 10000
    for i in range(1,10001):

        # Storing the passed variables from isPerfect to fact,yes and total
        fact,yes,total = isPerfect(i)

        # I decided to only print True
        if yes == True:
            print('{:^7}:  {:^60}  :{:^7}:  {:^7}'.format(str(i),str(fact),str(yes),str(total)))

ListOfPerfectNums()
