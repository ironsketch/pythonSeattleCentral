# Problems: #01,#02,#03,#04,#05,#06,#07,#YouTube

#01
################################################
##     Zelle 7.1. – compute wages with OT     ##
################################################

# Definition to calculate wage and OT
def wages(OT,wage,hours):
    earned = 0

    # If the hours hit to Overtime pay, then
    if hours > 40:

        # Find how much was overtime
        remainder = hours - 40

        # Calculate how much you made before overtime
        earned = wage * 40

        # Calculate what rate is your overtime based on your hourly
        OT *= wage

        # Then add the rest all together to get total earned
        earned = (OT * remainder) + earned
        return earned
    else:
        # Or you made 40 or less and it returns what you  made
        earned = wage * hours
        return earned

print (wages(1.5,10,41))

#02
################################################
##          Zelle 7.3 – compute grade         ##
################################################

def score(grade):

    # If else statements. Each uses a boolean to
    # find if it is true or not
    # Python works from top to bottom for these
    # that I made. first it will check if it is an A
    # If I had put B before A it would always be true if
    # any grade is above 80. Thus never returning an A
    # That is why it is in this order
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'

for i in range(0,101,10):
    print(score(i),i)

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

#04
################################################
##     Zelle 7.6 – computes speeding fine     ##
################################################

sp = 91
limit = 50

# This def with 2 parameters is used to calculate total fee
def fee(speed,speedLimit):
    fee = 50
    diff = (speed - speedLimit) * 5
    fee += diff
    if speed > 90:
        fee += 200
        return fee
    else:
        return fee
    
#  This def is to find out if they even broke the limit or not
def illegal(speed,speedLimit):
    if speed > speedLimit:
        return True
    else:
        return False

# main def
def main():
    if illegal(sp,limit) == True:
        print('You are OVER the speed limit!')
        print('You have been fined for this unacceptable action!')
        print('You now owe, ${}'.format(fee(sp,limit)))
    else:
        print('You were at or under the speed limit at,',sp)

main()

#05
################################################
##       Zelle 7.8 – finds eligibility        ##
################################################

def senate(age,cit):

    # Using a boolean to find out if criteria is met and returning a print
    # string
    if (age >= 30) and cit >= 9:
        eligable = print('You are eligable to be a US senator!')
        return eligable
    else:
        eligable = print('You are NOT eligable to be a US senator...')
        return eligable

def house(age,cit):
    # Using a boolean to find out if criteria is met and returning a print
    # string
    if (age >= 25) and cit >= 7:
        eligable = print('You are eligable to be a US rep')
        return eligable
    else:
        eligable = print('You are NOT eligable to be a US rep')
        return eligable

def main(age,cit):
    senate(age,cit)
    house(age,cit)
    
    
main(25,9)

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

#YouTube
################################################
##                   YouTube                  ##
################################################

def factorsOf(n):
    factors = []
    for i in range(1,n):
        if n % i == 0:
            factors.append(i)
    return factors

def isPerfect(n):
    factors = factorsOf(n)
    added = 0
    for i in factors:
        added += i
    if added == n:
        return factors,True,added
    else:
        factors = 'Not a Perfect'
        return factors,False,added

def ListOfPerfectNums():
    print('{:^7}:  {:^7}  :{:^7}:  {:^7}'.format('Numb','Factors','Perfect?','Equals too'))
    print("-"*50)
    for i in range(1,10001):
          fact,yes,total = isPerfect(i)
          if yes == True:
              print('{:^7}:  {:^60}  :{:^7}:  {:^7}'.format(str(i),str(fact),str(yes),str(total)))

ListOfPerfectNums()
