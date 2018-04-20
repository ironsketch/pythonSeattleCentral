'''A year is a leap year if it is divisible by 4, unless it is a century
year that is not divisible by 400. (1800 and 1900 are not leap years while
1600 and 2000 are.) Write a program that calculates whether a year is a
leap year.'''

#06
################################################
##          Zelle 7.11 – determines           ##
################################################

def isLeapYear(year):

    # Weed out all the not divisable by fours first
    if year % 4 != 0:
        return False

    # Then weed out all the centuries
    elif year % 100 == 0:

        # Make sure they are divisable by 400
        if year % 400 == 0:
            return True
        else:
            return False
        
    # Or return the divisable by 4
    else:
        return True

def main():
    for i in range (1600,2101):
        if isLeapYear(i) == True:
            print(i,'is a leap year.')
        else:
            print(i,'is not a leap year.')
main()
