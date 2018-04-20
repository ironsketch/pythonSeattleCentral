'''Write a program that accepts a date in the form month/day/year and
outputs whether or not the date is valid. For example 5/24/1962 is
valid, but 9/31/2000 is not. (September has only 30 days.)'''

#07
################################################
##       Zelle 7.11 – determines valid        ##
################################################

# Setting dict to make this easier
monthDays = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,
             8:31,9:30,10:31,11:30,12:31}

# User input
def userInput():
    date = input('Please enter a date like M/D/YEAR 1/2/1999: ')
    date = date.split('/')
    return date

# Is it a leap year (because of Feb)
def isLeapYear(year):
    year = int(year)
    if year % 4 != 0:
        return False
    elif year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    else:
        return True

# Check date validity
def validDate():

    # User input
    date = userInput()

    # Is it a leap year?
    if isLeapYear(int(date[2])) == True:

        # Yes, is it February and the day of month <= 29?
        if (int(date[0]) == 2) and (int(date[1]) <= 29):

            # Yes, is the months not exceeding 12?
            if int(date[0]) <= 12:

                # Yes return
                return date
            else:

                # No return false
                return False

        # Yes, leap year, no not Feb, is month !> 12 and month not larger
        # than the stored value for the dict?
        elif (int(date[0]) <= 12) and (int(date[1]) <= monthDays[int(date[0])]):

            # Yes return date
            return date
        else:

            # Return false otherwise
            return False

    # No not a leap year, is the month !> 12 and month not larger than the
    # stored value for the dict?
    elif (int(date[0]) <= 12) and (int(date[1]) <= monthDays[int(date[0])]):

        # Yes return date
        return date
    else:

        # No return False
        return False

def main():
    valid = validDate()

    # If valid is False:
    if valid == False:

        # You're a shitbag... apparently
        print('INVALID DATE SHITBAG!')
    else:

        # Put the string back
        s = '/'
        valid = s.join( valid )

        # Print out your congradulations
        print('Your date,',valid,'is valid.')
main()
    
