def gcd(a,b):

    # While b does not = 0
    while b != 0:

        # a will equal b and
        # b will equal the remainder of a % b
        a,b = b,a%b
    return a

def str2ints(LOfa_b):
    L = []

    # For each item in the string 
    for item in LOfa_b:

        # Append it to the list as an integer 
        L.append(int(item))

    # Return it as a tuple
    return tuple(L)

def int2strgs(a,b):

    # Adding two int as string with a / in the middle
    string = str(a) + '/' + str(b)
    return string

def reduce(frac):

    # Split the string
    frac = frac.split('/')

    # Create the tuple
    tup = str2ints(frac)

    # Break apart that tuple
    a,b = tup

    # Get the Greatest Common Denominator
    great = gcd(a,b)

    # A will now = the division of it by great
    a /= great

    # B ""
    b /= great

    # Turn it back to a fract
    fraction = int2strgs(int(a),int(b))
    return fraction

def add(frac1,frac2):

    # Split both at /
    frac1 = frac1.split('/')
    frac2 = frac2.split('/')

    # Get int from each
    frac1 = str2ints(frac1)
    frac2 = str2ints(frac2)

    # Times each by denom of other
    a = frac2[1] * frac1[0]
    b = frac1[1] * frac2[0]

    # Add those
    top = a + b

    # Get the new bottom
    bottom = frac2[1] * frac1[1]

    # Turn to string
    fraction = int2strgs(top,bottom)

    # Reduce it
    fraction = reduce(fraction)
    return fraction

def mul(frac1,frac2):

    # Split both at /
    frac1 = frac1.split('/')
    frac2 = frac2.split('/')

    # Get int from each
    frac1 = str2ints(frac1)
    frac2 = str2ints(frac2)

    # Times the top of both to get new top
    top = frac1[0] * frac2[0]

    # Times bottom of both to get new bottom
    bottom = frac1[1] * frac2[1]

    # Make into string
    fraction = int2strgs(top,bottom)

    # Reduce
    fraction = reduce(fraction)
    return fraction

def reciprocal(frac):

    # Split at /
    frac = frac.split('/')

    # Get int
    frac = str2ints(frac)

    # Flipping it
    bottom = frac[0]
    top = frac[1]

    # Getting string
    fraction = int2strgs(top,bottom)

    # Reducing if necessary
    fraction = reduce(fraction)
    return fraction

def div(frac1,frac2):

    # Splitting both at /
    frac1 = frac1.split('/')
    frac2 = frac2.split('/')

    # Getting int for both
    frac1 = str2ints(frac1)
    frac2 = str2ints(frac2)

    # essentially flipping second fract so to times it to first
    top = frac1[0] * frac2[1]
    bottom = frac1[1] * frac2[0]

    # Turning to string
    fraction = int2strgs(top,bottom)

    # Reducing
    fraction = reduce(fraction)
    return fraction

def addFracts(TplOfFracts):

    # Initializing counter
    counter = 1

    # Initializing first frac
    new = TplOfFracts[0]

    # For length - 1 since 1 is done
    for i in range (len(TplOfFracts) - 1):

        # the answer will equal the last one added to the last
        total = add(new,TplOfFracts[counter])

        # assigning last add to new, new
        new = total

        # adding to counter
        counter += 1
    return total
    
print(addFracts(('1/2','1/4','1/8','1/16','1/32')))
    
