# change.py
#   A program to calculate the value of some change in dollars

def main():
    print("Change Counter")
    print()
    print("Please enter the count of each coin type.")
    quarters = eval(input("Quarters: "))
    dimes = eval(input("Dimes: "))
    nickels = eval(input("Nickels: "))
    pennies = eval(input("Pennies: "))
    total = quarters * .25 + dimes * .10 + nickels * .05 + pennies * .01
    print()
    print("The total value of your change is", total)

main()

type(3)
type(3.14)
type(3.0)
myInt = -32
type(myInt)
myFloat = 32.0
type(myFloat)

a = 3+4
print(a,type(a))
b = 3.0 + 4.0
print(b,type(b))
c = 3*4
print(c,type(c))
d = 3.0*4.0
print(d,type(d))
e = 4**3
print(e,type(e))
f,g = 5,-3.5
print(f,abs(f),g,abs(g))
h = 10/3
print(h,type(h))
i = 10.0,3.0
print(i,type(i))
j = 10/5
print(j,type(j))
k = 10//3
print(k,type(k))
l = 10.0 // 3.0
print(l,type(l))
m = 10 % 3
print(m,type(m))
n = 10.0 % 3.0
print(n,type(n))

x = 3 +  4.0
print(x,type(x))

## USING MATH LIBRARY

# quadratic.py
#    A program that computes the real roots of a quadratic equation.
#    Illustrates use of the math library.
#    Note: this program crashes if the equation has no real roots.

import math  # Makes the math library available.

def main():
    print("This program finds the real solutions to a quadratic")
    print()

    a, b, c = eval(input("Please enter the coefficients (a, b, c): "))

    discRoot = math.sqrt(b * b - 4 * a * c)
    root1 = (-b + discRoot) / (2 * a)
    root2 = (-b - discRoot) / (2 * a)

    print()
    print("The solutions are:", root1, root2 )

main()

## INTRODUCE BOOLEANS, IF ELIF ELSE
## MUTUALLY EXCLUSIVE POSSIBILITIES
## ALSO INTRODUCE RETURN STATEMENT

b1 = (3 > 2)
print(b1,type(b1))

b2 = (7 == 5)
print(b2,type(b2))

b3 = (4 >= 2)
print(b3,type(b3))

b4 = (7 % 2 == 1)
print(b4,type(b4))

b5 = (2 <= 7 <= 10)
print(b5,type(b5))

for i in range(5):
    if i < 3:
        print(i)

# Write a function printIfEx_1(), which uses a for loop and a range
# statement to cycle through all ints between 15 & 20 inclusive
# and uses an if statement and a boolean toprint out only the ints
# between 17 and 19 inclusive.

# COMPARING PRINT AND RETURN

# Compare these two functions:

def addNums_1(x,y):
    print(x+y)

def addNums_2(x,y):
    return x+y


##>>> addNums_1(2,4)
##6
##>>> addNums_2(2,4)
##6
##>>>
# But:
##>>> addNums_1(2,4) + 1
##6
##Traceback (most recent call last):
##  File "<pyshell#26>", line 1, in <module>
##    addNums_1(2,4) + 1
##TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
# And:
##>>> addNums_2(2,4) + 1
##7
##>>>

# addNums_1(2,4) sends its output to the terminal with the print statement.
# Its output is not useable for further computation.
# addNums_2(2,4)returns its numberical output, which can then be used
# for further computation.
# Moral:  If you want to use the output of a function for further computation,
#       use      return     not     print.
# This is particularly useful for function composition, ie, functions of functions.

def square(x):
    return x**2

>>> square(addNums_2(2,3))
25
>>> 

# but
##>>> square(addNums_1(2,3))
##5
##Traceback (most recent call last):
##  File "<pyshell#32>", line 1, in <module>
##    square(addNums_1(2,3))
##  File "<pyshell#30>", line 2, in square
##    return x**2
##TypeError: unsupported operand type(s) for ** or pow(): 'NoneType' and 'int'

# Notice that:
# 1. Variable x in addNums_2(x,y) and x in square(x) are different variables.
#     and do not conflict with each other.  More on this later.
# 2. square(addNums_1(2,3)) triggered a syntax error and printed 5.
# 3.square(addNums_2(2,3)) did the right thing.  addNums(2,3) returns 5 to the 
#   square function, which then squares its input and returns 25.

# Also, note that, once return is executed, Python leaves the function, returning whatever
# it was asked to return.

# Write a function, diffOverSum(x,y), which returns (x-y)/(x+y).

# Use diffOverSum(x,y) to write a function, C2F_2(), which prints out a table whose
# 1st column is C degrees from 0 to 100 in steps of 10,
# whose 2nd column is equivalent F degrees,
# and whose 3rd column is(F-C)/(F+C).
# Make sure you put the definition of  diffOverSum(x,y) in the same file with C2F_2().
# Then you can use diffOverSum(x,y) inside the definition of C2F_2().

# quadraticWConditionals.py
#    A program that computes the real roots of a quadratic equation.
#    Illustrates use of the math library and if elif else
#    Note: this program does not crashes if the equation has no real roots.
#    There is a bug in this program.  Can you find it?

import math  # Makes the math library available.

def main():
    print("This program finds the real solutions to a quadratic")
    print()

    a, b, c = eval(input("Please enter the coefficients (a, b, c): "))

    disc= (b * b - 4 * a * c)
    if disc < 0:
        print('This equations has no real roots.  Sayonara.')
    elif disc > 0:
        root1 = (-b + math.sqrt(disc)) / (2 * a)
        root2 = (-b - math.sqrt(disc)) / (2 * a)
        print("The solutions are:", root1, root2 )
    else: # 2 equal real roots
        print("The 2 equal roots are:", -b/2*a )    

main()

##This program finds the real solutions to a quadratic
## (x+2)(x+3) = x^2 + 5x + 6
##Please enter the coefficients (a, b, c): 1,5,6
##The solutions are: -2.0 -3.0
##>>> main()
##This program finds the real solutions to a quadratic
## 
##Please enter the coefficients (a, b, c): 1,5,10
##This equations has no real roots.  Sayonara.
##>>> main()
##This program finds the real solutions to a quadratic
## x^2 + 4x + 4 = (x+2)^2
##Please enter the coefficients (a, b, c): 1,4,4
##The 2 equal roots are: -2.0
##>>> main()
##This program finds the real solutions to a quadratic
## (3x+2)^2 = 9x^2 + 12x + 4
##Please enter the coefficients (a, b, c): 9,12,4
##The 2 equal roots are: -54.0
##>>> 

# An int is even if it is divisible by 2,
# otherwise it is odd. Look at remainder when an int n
# is divided by 2. There are only 2 cases:
#   If remainder is 0, n is even.
#   If remainder is 1, n is odd.

e = 8 % 2
print(e)
o = 9 % 2
print(o)

# boolean functions return True or False.  Examples are isEven(n) and isOdd(n):
# isEvenisOdd.py

def isEven(n):
    '''Returns True if n is even. OTW return False.
n is an int.'''
    Tval = (n % 2 == 0)
    return Tval

def isOdd(n):
    '''Returns True if n is odd. OTW return False.
n is an int.  Uses isEven(n).'''
    return not isEven(n)

# Write a function,IDasEvenOrOdd(L), that traverses a list L of ints with 
# a for loop & which prints out each number, identifying each int as
# even or as odd. Make sure isEven(n) is in the same file.  Do you need
# isOdd(n)?

# Assume the days of the week are numbered 0,1,2,3,4,5,6 from Sunday to Saturday.
#  Writea function, dayNum2day(dayNum), which is given the day number, and
# which returns the day name (a string).  Use a for loop to cycle over all the
# numbers and print out the corresponding day name.  Use if elif.


## You go on a wonderful holiday (perhaps to jail, if you don’t like happy exercises)
## leaving on day number 3 (a Wednesday). You return home after 137 sleeps. Write 
## a general function, dayBackFromVacation(),  which asks for the starting day number, 
## and the length of your stay, and it will return the name of day of the week you 
## will return on.  Plan on using dayNum2day(dayNum) in the definition of
## dayBackFromVacation().

# We have discussed a sum accumulator.  Here is a  function  that uses a product acum
# and returns the product of the 1st 5 natural numbers.

# There is a bug in this function.  Can you find it?
def productAcum(L):
    ''' Returns the product of the numbers in list L.  There is a bug in
this program.  Can you find it & fix it?
'''
    p = 1
    for n in L:
        p = p*n
        return n
    



