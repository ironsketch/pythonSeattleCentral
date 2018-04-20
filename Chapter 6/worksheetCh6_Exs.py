# Explain the output from the following:
#####################

# addinterest1.py

def addInterest(balance, rate):
    newBalance = balance * (1+rate)
    balance = newBalance

def test():
    amount = 1000
    rate = 0.05
    addInterest(amount, rate)
    print(amount)
    
test()
##################

# Compare with the output from the following:
#########################
# addinterest2.py

def addInterest(balance, rate):
    newBalance = balance * (1+rate)
    return newBalance

def test():
    amount = 1000
    rate = 0.05
    amount = addInterest(amount, rate)
    print(amount)

test()

###########################

# In addinterest1.py, the function addInterest(balance, rate)
# computes the new balance & assigns it to balance.  Bit
# addInterest(balance, rate) does not return this newly
# computed balance, so when test() calls addInterest(amount, rate),
# nothing is passed to test().  amount was never changed by 
# addInterest(balance, rate)

# In addinterest2.py, , the function addInterest(balance, rate)
# computes a new balance, assigns the result to newBalance, and it
# returns newBalance.
# When test(), amount is assigned to addInterest(amount, rate),
# which actually is the updated balance.
# Moral:
# Variables (other than lists) are local to a function.  The only way
# a function can communicate values computed inside the function is
# to return values (except for lists).

### And now, for a function using a list
##############################
# addinterest3.py

def addInterest(balances, rate):
    for i in range(len(balances)):
        balances[i] = balances[i] * (1+rate)

def test():
    amounts = [1000, 2200, 800, 360]
    rate = 0.05
    addInterest(amounts, rate)
    print(amounts)

test()
#################################
# What's the story?  It looks like addinterest3.py, but
# in this case, addInterest(amounts, rate), when called from
# test(), does change amounts, even though addInterest(balances, rate)
# does not return anything.
# The difference is that list and its mutability
# Look at this:
x = 3
y = x
x = x+1
x
y
# x is changed, y is not changed
# ints are immutable.  Same would happen with floats......
f = 3.0
g = f
f = f + 1.0
f
g
# ..... and with strings:
s = 'sheep'
t = s
s = s + 's'
s
t
## also, look at this ex with a string:
s = 'pot'
s[1] = 'a' ## replace 'o' with 'a' in 'pot'
s
# But look what happens with a list:
L = [1,2,3]
M = L
L.append(4)
L
M
# Both L and M are modified.
# Also, unlike a string, a list can be modified in place:
W = [7,8,9]
W[1] = 8.5
W
# But tuples are immutable:
X = (1,2,3)
X[1] = 2.5 # change 2 to 2.5

# Write a function, distance(x1,y1,x2,y2),
# which takes the coordinates of 2 points on
# the xy plane as inputs and which returns
# the distance between the 2 points.

# Write a function, TrnglArea(x1,y1,x2,y2,x3,y3),which uses
# distance(x1,y1,x2,y2) to return the area of a triangle
# with vertices at the given coordinates.  Use the Hero's formula
# for the area of a triangle:
# A = sqrt(s(s-a)(s-b)(s-c)), where
# s = perimeter/2
# a,b,c = side lengths
# put  the def for distance(x1,y1,x2,y2) in the same file.

#  What is the area of the triangle with vertices at
# (0,0), (4,0), (0,3) ?

# What is the area of the triangle with vertices at
# (0,0), (3,6), (6,12)?

# Use TrnglArea(x1,y1,x2,y2,x3,y3) to show that the order of
# the points does not affect the area of the triangle.


# Write a function, midPtOfLine(x1,y1,x2,y2), that takes
# the coords of 2 pts as parameters and which returns the
# coords of the midpoint of the line segment connecting them.

# Write a function, areaOfInrTrngl(x1,y1,x2,y2,x3,y3), that uses
# midPtOfLine(x1,y1,x2,y2) and TrnglArea(x1,y1,x2,y2,x3,y3) to find
# the area of the triangle inside the triangle whose vertices are
# the initial 3 coord pairs;  the inside triangle has vertices on
# the midpoint of each side of the larger triangle.


# dictionaries
# Dictionaries are yet another kind of compound type.
# They are Python’s built-in mapping
# type. They map keys, which can be any immutable type,
# to values, which can be any type
# (heterogeneous), just like the elements of a list or tuple.
# In other languages, they are called
# associative arrays since they associate a key with a value.

# As an example, we will create a dictionary to translate English
# words into Spanish. For this
# dictionary, the keys are strings.
# One way to create a dictionary is to start with the empty
# dictionary and add key:value pairs.

# The empty dictionary is denoted {}:
    
eng2sp = {}
eng2sp["one"] = "uno"
eng2sp["two"] = "dos"

print(eng2sp)
{"two": "dos", "one": "uno"}
# Each pair contains a key and a value separated by a colon.
# Note: keys must be a non-mutable data type like a string,
# int, float or tuple. A list can't be used for a dictionary key.
# The key:value pairs of the dictionary are separated by commas.

fruitInventory = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}


# We can traverse a dictionary by traversing its keys:
for fruit in fruitInventory.keys():
    print(fruit)

# or
for fruit in fruitInventory:
    print(fruit)


# You can also traverse the dictionary using items
for stuff in fruitInventory.items():
    print(stuff)
   
# You can traverse the dictionary values:

for cost in fruitInventory.values():
    print(cost)

# or

for fruit in fruitInventory:
    print(fruitInventory[fruit])

# Notice how fruit is being like an index.  Think of a list, for example.
# Here is another dictionary that gives the cost per fruit for each
# fruit in the inventory

fruitCost = {"apples": 0.85, "bananas": 0.11, "oranges": 0.65, "pears": 0.70}

# write a function, totFruitInvVal(fruitInventory, fruitCost), that returns
# the total value of the fruit inventory.

# The in and not in operators can test if a key is in the dictionary:
>>> "one" in eng2sp
True
>>> "six" in eng2sp
False
>>> "tres" in eng2sp # Note that ’in’ tests keys, not values.
False
# This method can be very useful, since looking up a non-existent key in a dictionary causes a
# runtime error:
eng2esp["dog"]
# Traceback (most recent call last):
# ...
# KeyError: ’dog’

# Using a dictionary to count letter frequency in a word: histogram(word)
# def histogram(word):
    '''Returns a dictionary with keys =
letters in word, corresp value is
the number of times the letter occurs
in word.
Pseudo code:
   start with  empty dictionary accumulator
   traverse each letter of the word
   if letter not in dictionary
     put it in
     set count to 1
   if letter already in dictionary
     increase letter count of that letter by 1
   return the dictionary accumulator
        
'''
# histogram('parrot')   
# {'t': 1, 'a': 1, 'r': 2, 'p': 1, 'o': 1}
# write histogram(word)

# Write a funtion,rollOneDice(n), that rolls a fair dice
# n times & returns a dictionary whose keys are the ints
# 1,2,3,4,5,6 and whose corresponding values are the number
# of times that dice value was rolled. Use randint from the
# random module.  Start with a dictionary accumulator with all the
# values set to zero.

# Use rollOneDice(1000) and print out the result:

#   1 occurred   157 times.
#   2 occurred   175 times.
#   3 occurred   163 times.
#   4 occurred   163 times.
#   5 occurred   164 times.
#   6 occurred   178 times.

# Write a python script to sum all the values & confirm the total is 1000.

# Write a function, rollOneDiceFreq(n), that uses rollOneDice(n) to return
# a dictionary of the relative frequency as a decimal for each roll value.

# Write a boolean function, isFactor(f,n), which returns
# True if f is a factor of n, OTW returns False.
# f,n are ints.  Use your function to make this printout:
# >>> for f in range(2,13):
# ...     print('{0} is a factor of {1} is a {2} statement.'.format(f,12,isFactor(f,12)))
# ...
# 2 is a factor of 12 is a True statement.
# 3 is a factor of 12 is a True statement.
# 4 is a factor of 12 is a True statement.
# 5 is a factor of 12 is a False statement.
# 6 is a factor of 12 is a True statement.
# 7 is a factor of 12 is a False statement.
# 8 is a factor of 12 is a False statement.
# 9 is a factor of 12 is a False statement.
# 10 is a factor of 12 is a False statement.
# 11 is a factor of 12 is a False statement.
# 12 is a factor of 12 is a True statement.

# Write a function, isPrime(n), which uses
# isFactor(f,n), which returns True if
# n is prime, OTW returns False.
# Use isPrime(n) to print out all primes <= 1000.

# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103
# 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211
# 223 227 229 233 239 241 251 257 263 269 271 277 281 283 293 307 311 313 317 331
# 337 347 349 353 359 367 373 379 383 389 397 401 409 419 421 431 433 439 443 449
# 457 461 463 467 479 487 491 499 503 509 521 523 541 547 557 563 569 571 577 587
# 593 599 601 607 613 617 619 631 641 643 647 653 659 661 673 677 683 691 701 709
# 719 727 733 739 743 751 757 761 769 773 787 797 809 811 821 823 827 829 839 853
# 857 859 863 877 881 883 887 907 911 919 929 937 941 947 953 967 971 977 983 991
# 997



## dictionaries & coin tossing

# Write a function, CT(pH), that tosses a coin once & returns 1 its its
# a Head, which occurs with probability pH, and returns 0 if its a tail.
# If pH = 0.5, the coin is fair.  Use the random function from
# the random module.

# 1 0 0 0 1 0 0 1 0 1 0 1 0 0 1 1 0 1 0 1
# 1 0 1 0 1 0 0 1 0 1 1 0 1 1 0 1 1 1 1 1

# Write a function, CT_qToss(q,pH), which tosses a coin
# q times & which returns the number of Heads.
# Uses CT(pH).  pH is the probability of getting a Head.

# Use CT_qToss(q,pH), repeat a 5 toss 20 times, & print
# out the number of Heads for each 5 toss on one line.

# 1 3 2 2 3 2 1 2 2 3 2 2 2 2 2 1 2 3 3 4 

# Write a function, CT_qTosses_zTimes(q,z,pH), which
# Repeats a qToss z times.  Returns a dictionary
# with keys = nH for each qToss and values = # times that
# nH occurred.  Note that 0 <= nH <= q.

# Use CT_qTosses_zTimes(5,1000,0.5) to do a 5 toss 1000 times
# with a fair coin and then to print out the result:

##>>> 
##    0 Heads occurred    34 times. 
##    1 Heads occurred   163 times. 
##    2 Heads occurred   301 times. 
##    3 Heads occurred   298 times. 
##    4 Heads occurred   177 times. 
##    5 Heads occurred    27 times. 
##>>> 
