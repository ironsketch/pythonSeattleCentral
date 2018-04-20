# Problems: #01,#02,#03,#04,#05,#06,#YouTube https://youtu.be/OJMoQumklwg

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

#02
################################################
##                  Zelle 8.2                 ##
################################################

from math import *

def wCI():

    # Setting up all the variables
    T = -20
    V = 0

    # Printing with nice formating what I have done
    print('{:<10} {:<10} {:<10}'.format('Degree ','Wind Speed ','Wind Chill'))

    # Setting up something to run through the numbers and using it for
    # Wind Speed
    for i in range(0,50,5):

        # Breaking apart the math
        V = i**.16
        wind1 = 0.6215 * T
        wind2 = 35.75 * V
        wind3 = .4275 * T * V
        windChillIndex = 35.74 + wind1 - wind2 + wind3
        print('{:<10.3f} {:<10.3f} {:<10.3f}'.format(T,V,windChillIndex))
        T += 10
wCI()

#03
################################################
##                  Zelle 8.3                 ##
################################################

def double(investment,r):
    a = 0
    t = 0

    # While the investment is less than twice its self
    while a < investment * 2:
        # Calculate the investment
        a = investment * (1 + r * t)

        # Calculating by year and adding one
        t += 1
    print (t,a)
        
inv =10000.00
double(inv,3.875)

#04
################################################
##                  Zelle 8.5                 ##
################################################

from math import *

def isPrime(n):
    L = []
    sqrtN = int(sqrt(n))
    a = 0
    for i in range(2,sqrtN):
        while a != 0:
            a = n % i
            L.append(a)

    total = 0
    for item in L:
        total += item

    TV = total == 0
    return TV
n = 8
print('It is,',isPrime(n),'that,',n,'is a prime number.')

#05
################################################
##                  Zelle 8.6                 ##
################################################
import math

def isPrime(n):
    if n % 2 == 0:
        return False
    factor = 3
    while factor <= math.sqrt(n):
        if n % factor == 0:
            return False
        factor = factor + 2
    return True

def main (n):
    for i in range (n):
        if isPrime(i):
            print(i, "is a prime.")
main(14)

#06
################################################
##                  Zelle 8.7                 ##
################################################

#YouTube https://youtu.be/OJMoQumklwg
################################################
##                  You Tube                  ##
################################################

def dec2letter(decGrade):

    # if else statment with booleans to decide grade
    if decGrade > 0.92:
        return 'A'
    elif decGrade > 0.85 and decGrade <= 0.92:
        return 'B'
    elif decGrade > 0.78 and decGrade <= 0.85:
        return 'C'
    elif decGrade > 0.65 and decGrade <= 0.78:
        return 'D'
    else:
        return 'E'

def testScores2Letter(fileName):
    L = []
    # Opening file to read it
    fileOpen = open(fileName, 'r')
    for grade in fileOpen:
        # Replacing unwanted characters
        grade = grade.replace('\n','')
        grade = grade.replace(' ','')
        #Splitting it
        grade = grade.split(',')
        # Appending it to list
        L.append(grade)
    # Closing the file
    fileOpen.close()

    #Returning list
    return L

def main():
    #List that was returned
    L = testScores2Letter('decGrades.txt')
    print('{:>10} {:>10} {:>10}'.format('Name','Grade','Average'))
    print('-'*40)
    for item in L:

        #Getting average
        average = float(item[1]) + float(item[2]) + float(item[3]) + float(item[4])
        average /= 4

        #Printing it out nicely
        print('{:>10} {:>10} {:>10.2f}'.format(item[0],dec2letter(average),average))
        
    
main()
