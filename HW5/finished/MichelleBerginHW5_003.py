'''A certain college classifies students according to credits earned.
A student with less than 7 credits is a Freshman. At least 7 credits
are required to be a Sophomore, 16 to be a Junior and 26 to be classified
as a Senior. Write a program that calculates class standing from the
number of credits earned.'''

#03
################################################
##      Zelle 7.4 – find class standing       ##
################################################

hours = 120

def classStanding(credHours):

    # Setting up an if else option. Each uses a boolean to find out
    # If the data passed through == True then it will return the right
    # class standing
    if credHours < 7:
        return 'Freshman'
    elif credHours < 16:
        return 'Sophmore'
    elif credHours < 26:
        return 'Junior'
    else:
        return 'Senior'

print ('Your class standing is,',classStanding(hours),'with',hours,'credit hours.')
