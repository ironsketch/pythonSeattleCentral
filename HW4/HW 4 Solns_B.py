# c06ex04.py

def sumN(n):
    '''
Sum of natural numbers from 1 to n.
'''
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    return sum

def sumNCube(n):
    '''
Sum of cubes of natural numbers from 1 to n.
'''
    sum = 0
    for i in range(1,n+1):
        sum = sum + i**3
    return sum

def main():
    print("This program computes the sum and sum of cubes of the first")
    print("N natural numbers.\n")

    n = eval(input("Please enter a value for N: "))
    print("The sum of the first %d natural numbers is %d" % (n,sumN(n)))
    print("The sum of the cubes of those numbers is %d" % (sumNCube(n)))

main()

##>>> 
##This program computes the sum and sum of cubes of the first
##N natural numbers.
##
##Please enter a value for N: 5
##The sum of the first 5 natural numbers is 15
##The sum of the cubes of those numbers is 225
##>>> 


# c06ex10.py
#   Acronym generator using functions


def acronym(phrase):
    '''
Given a phrase, outputs an acronym.
'''
    ans = ""
    for word in phrase.split():
        ans = ans + word[0]
    return ans.upper()

def main():
    print("Acronym Builder")
    words = input("Enter a phrase: ")
    print("Acronym:", acronym(words))

main()

>>> 
Acronym Builder
Enter a phrase: what is the world are you doing
Acronym: WITWAYD
>>> 


    
# c06ex11.py
#    Square each value in a list

def squareEach(nums):
    '''
Changes the numbers in a list
to squares.
'''
    for i in range(len(nums)):
        nums[i] = nums[i]**2


def test():
    nums = list(range(10))
    print('The original list:               ', nums)
    squareEach(nums)
    print('The list after squareEach(nums): ',nums)

test()

##>>> 
##The original list:                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
##The list after squareEach(nums):  [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
##>>> 


# c06ex13.py
#    function to convert list of strings to numbers

def toNumbers(strList):
    '''
Converts each string to a number in the list.
'''
    for i in range(len(strList)):
        strList[i] = eval(strList[i])


def test():
    x = ["12", "345", "15.34"]
    toNumbers(x)
    print(x)

test()

##>>> 
##[12, 345, 15.34]
##>>> 



# c06ex14.py
#    sum of squares from file

def toNumbers(strList):
    '''
Converts strings in string to numbers.
'''
    for i in range(len(strList)):
        strList[i] = eval(strList[i])

def sumList(nums):
    '''
Sums the numbers in list nums.
'''
    sum = 0
    for n in nums:
        sum = sum + n
    return sum

def squareEach(nums):
    '''
Squares each number in list nums.
'''
    for i in range(len(nums)):
        nums[i] = nums[i]**2

def main():
    print("Program to find sum of squares from numbers in a file")
    fname = input("Enter filename: ")
    data = open(fname,'r').readlines()
    print(data)  ## look at form of data
    toNumbers(data)
    squareEach(data)
    print("Sum of squares:", sumList(data))

##>>> main()
##Program to find sum of squares from numbers in a file
##Enter filename: nums.txt
##['2\n', '4\n', '6\n', '8\n', '10']
##Sum of squares: 220
##>>> 

def divOf(intNum):
    '''
Returns a list of divisors of intNum.
'''
    divOf = [1] ## init list accumulator
    for num in range(2,intNum+1):
        if intNum % num == 0:
            divOf.append(num)
    return divOf

def main():
    number = eval(input('Enter a number: '))
    print('Divisors of {0} are {1}.'.format(number,divOf(number)))

main()

##>>> main()
##Enter a number: 12
##Divisors of 12 are [1, 2, 3, 4, 6, 12].
##>>> main()
##Enter a number: 1000
##Divisors of 1000 are [1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 125, 200, 250, 500, 1000].
##>>> main()
##Enter a number: 1001
##Divisors of 1001 are [1, 7, 11, 13, 77, 91, 143, 1001].
##>>> main()
##Enter a number: 101
##Divisors of 101 are [1, 101].
##>>> 
    
def divOf(intNum):
    '''
Returns a list of divisors of intNum.
'''
    divOf = [1] ## init list accumulator
    for num in range(2,intNum+1):
        if intNum % num == 0:
            divOf.append(num)
    return divOf


def isPrime(intNum):
    '''
Returns True if intNum is Prime,
OTW returns False.
'''
    return len(divOf(intNum)) == 2

def main():
    number = eval(input('Enter a number: '))
    if isPrime(number):
        print('{0} is prime.'.format(number))
    else:
        print('{0} is not prime.'.format(number))


main()

##Enter a number: 12
##12 is not prime.
##>>> isPrime(12)
##False
##>>> main()
##Enter a number: 13
##13 is prime.
##>>> L = []
##>>> for num in range(2,1000):

##	if isPrime(num):
##		L.append(num)
##
##		
##
##>>> L
##[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
##>>> 
##
##
##    

            
    

