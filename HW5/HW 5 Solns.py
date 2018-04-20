# c07ex1.py
#    overtime pay
def main():
    print("Weekly pay calculator\n")
    hours = eval(input("Enter hours worked: "))
    wage = eval(input("Enter hourly wage: "))
    if hours <= 40:
        pay = hours * wage
    else:
        pay = 40 * wage + (hours-40) * 1.5 * wage

    print("Your week's pay is ${0:0.2f}".format(pay))

if __name__ == '__main__':
    main()

##>>> 
##Weekly pay calculator
##
##Enter hours worked: 45
##Enter hourly wage: 30
##Your week's pay is $1425.00
##>>> 

##>>> 
##Weekly pay calculator
##
##Enter hours worked: 30
##Enter hourly wage: 30
##Your week's pay is $900.00
##>>> 


# c07ex03.0y
#   Exam grader using decisions

def main():
    print("Exam Grader\n")
    score = eval(input("Enter the score: "))
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >=70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    print("The grade is", grade)

if __name__ == '__main__':
    main()
##>>> 
##Exam Grader
##
##Enter the score: 92
##The grade is A
##>>> main()
##Exam Grader
##
##Enter the score: 87
##The grade is B
##>>> main()
##Exam Grader
##
##Enter the score: 59
##The grade is F
##>>> 


# c07ex04.py
#    College classification

def main():
    print("College Classification\n")
    credits = eval(input("Enter number of credits: "))
    if credits < 7:
        cls = "Freshman"
    elif credits < 16:
        cls = "Sophomore"
    elif credits < 26:
        cls = "Junior"
    else:
        cls = "Senior"
    print("The classification is", cls)

if __name__ == '__main__':
    main()
##>>> 
##College Classification
##
##Enter number of credits: 6
##The classification is Freshman
##>>> main()
##College Classification
##
##Enter number of credits: 7
##The classification is Sophomore
##>>> main()
##College Classification
##
##Enter number of credits: 17
##The classification is Junior
##>>> 

# c07ex06.py
#    Speeding tickets

def main():
    print("Speeding fine calculator\n")
    limit = eval(input("Enter the speed limit "))
    speed = eval(input("Enter the clocked speed "))

    if speed <= limit:
        print("Legal")
    else:
        fine = 50 + 5*(speed - limit)
        if speed > 90:
            fine = fine + 200
        print("Fine ${0:0.2f}".format(fine))

if __name__ == "__main__":
    main()

##>>> 
##Speeding fine calculator
##
##Enter the speed limit 35
##Enter the clocked speed 65
##Fine $200.00
##>>> main()
##Speeding fine calculator
##
##Enter the speed limit 35
##Enter the clocked speed 95
##Fine $550.00
##>>> 

# c07ex07.py
#    Babysitter pay
#    This is a subtle problem with many possible solutions


def main():
    '''There are 3 possibilities:
A.  Bedtime <= Start    <=   End      
B.  Start   <= Bedtime  <=   End
C.  Start   <= End      <=   Bedtime
It may be simpler to deal with each of these at a time
than to use Zelle's approach.
'''
    print("Babysitting Calculator\n")
    print("Enter times using 24 hour format (e.g. 8 pm is 20:00)")
    sHours, sMins = input("Starting time (hh:mm): ").split(":")
    eHours, eMins = input("Ending time (hh:mm): ").split(":")

    # convert to hours since midnight
    start = int(sHours) + float(sMins)/60.0
    end = int(eHours) + float(eMins)/60.0

    if start < 12: # correct for rollover at midnight - start is after midnight
        start += 24
    if end < start: # correct for rollover at midnight
        end   += 24
    

    bedtime = 21.0
    if bedtime <= start <= end:  ## Option A
        pay = (end - start)*1.75
    elif start <= bedtime <= end:  ## Option B
        pay = (bedtime - start)*2.50 + (end - bedtime)*1.75
    else:  ##Option C  start <= end <= bedtime
        pay = (end - start)*2.50
##    # calculate pre and post bedtime hours
##    if start < bedtime:
##        if end < bedtime:
##            primeHours = end - start
##            extraHours = 0.0
##        else:
##            primeHours = bedtime - start
##            extraHours = end - bedtime
##    else:
##        primeHours = 0.0
##        extraHours = end - start
##    pay = 2.50 * primeHours + 1.75 * extraHours
        
    print("Total payment due: ${0:0.2f}".format(pay))

if __name__ == '__main__':
    main()
##Babysitting Calculator
##
##Enter times using 24 hour format (e.g. 8 pm is 20:00)
##Starting time (hh:mm): 17:00
##Ending time (hh:mm): 2:00
##Total payment due: $18.75
##>>> main()
##Babysitting Calculator
##
##Enter times using 24 hour format (e.g. 8 pm is 20:00)
##Starting time (hh:mm): 2:00
##Ending time (hh:mm): 5:00
##Total payment due: $5.25
##>>> main()
##Babysitting Calculator
##
##Enter times using 24 hour format (e.g. 8 pm is 20:00)
##Starting time (hh:mm): 14:00
##Ending time (hh:mm): 19:00
##Total payment due: $12.50
##>>> 


# c07ex07.py  alt soln with functions
#    Babysitter pay
def main():
    sTimeStr = input('What is the start time (HH:MM, 24 hr clock)? ')
    eTimeStr = input('What is the end time (HH:MM, 24 hr clock)? ')
    sDecTime,eDecTime  = toDecTime(sTimeStr),2DecTime(eTimeStr)
    sScaledtime, eScaledtime = timeScale(sDecTime,eDecTime)
    HiPayHrs,LoPayHrs = LoHi(sScaledTime,eScaledTime)
    HiRate,LoRate = 2.50,1.75
    compensation = HiPayHrs*HiRate + LoPayHrs*LoRate
    print('The babysitter worked from {0} to {1}'.format(sTime,eTime))
    print('You owe the babysitter ${0:.2f}'.format(compensation))


def timeScale(time):
    '''
Time is in decimal format and uses 24 hr clock.
Bedtime is origin, with times before bedtimes -ve, times after bedtimes +ve.
'''
    bedtime = 21.00
    if AfterMidnight(time):
        time += 3
    else:
        time += -bedtime
    return time

##>>> timeScale(1)
##4
##>>> timeScale(21)
##0.0
##>>> timeScale(23)
##2.0
##>>> timeScale(12)
##-9.0
##>>> timeScale(7)
##10


def toDecTime(timeStr):
    '''
Converts from HH:MM string to decimal time in 24 hr format.
'''
    h,m = timeStr.split(':')
    return int(h) + float(m)/60.0

##>>> toDecTime('20:45')
##20.75
##>>> toDecTime('00:45')
##0.75

def AfterMidnight(decTime):
    '''
Boolean that returns True if scale time is after midnight
'''
    return 0 < decTime <= 8

##>>> AfterMidnight(8.25)
##False
##>>> AfterMidnight(4)
##True

def LoHi(sScaledTime,eScaledTime):
    '''
Returns # hrs Lo pay and Hi pay as a tuple.
'''
    if sScaledTime < 0 and eScaledTime < 0:  # start & end before bed
        Hi,Lo = abs(eScaledTime - sScaledTime),0
    elif sScaledTime <0 and eScaledTime > 0: # start before bed, end after bed
        Hi,Lo = abs(sScaledTime), eScaledTime
    else:  # start & end after bed
        Hi,Lo = 0, abs(eScaledTime - sScaledTime)
    return Hi,Lo

##>> LoHi(-2,2)
##(2, 2)
##>>> LoHi(-5,-1)
##(4, 0)
##>>> LoHi(1,5)
##(0, 4)
##>>> 


# c07ex08.py
#   Eligibility for Congress
#   Note: This solution does not use Boolean operators, since
#         they are introduced in Chapter 8.

def main():
    print("Congressional Eligibility\n")
    age = eval(input("Enter your age: "))
    residency = eval(input("Enter years of residency: "))
    if age >= 30:
        if residency >= 9:
            print("You are eligible for the Senate and the House.")
        elif residency >= 7:
            print("You are eligible only for the House.")
        else:
            print("You are not eligible for Congress.")
    elif age >= 25:
        if residency >= 7:
            print("You are eligible only for the House.")
        else:
            print("You are not eligible for Congress.")
    else:
        print("You are not eligible for Congress.")

if __name__ == '__main__':
    main# c07ex11.py
#     Leap year determination

def isLeap(year):
    if year % 4 != 0:
        return False
    elif year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    else:
        return True

def main():
    print("This program calculates whether a year is a leap year.\n")
    year = eval(input("Enter a year: "))
    if isLeap(year):
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")
        
if __name__ == '__main__':
    main()

##This program calculates whether a year is a leap year.
##
##Enter a year: 1600
##1600 is a leap year.
##
##>>> main()
##This program calculates whether a year is a leap year.
##
##Enter a year: 1700
##1700 is not a leap year.
##>>> main()
##This program calculates whether a year is a leap year.
##
##Enter a year: 1604
##1604 is a leap year.
##>>> main()
##This program calculates whether a year is a leap year.
##
##Enter a year: 1605
##1605 is not a leap year.
##>>>

# c07ex12.py
#    Date validator

from c07ex11 import isLeap

DAYS_IN_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isValidDate(month, day, year):
    if 1 <= month <=12:
        # month OK, check day
        
        # determine last day of month
        if month == 2:
            if isLeap(year):
                lastDay = 29
            else:
                lastDay = 28
        else:
            lastDay = DAYS_IN_MONTH[month]

        # if day is also good, return True
        if 1 <= day <= lastDay:
            return True
        
    # did not validate
    return False 
    

def main():
    print("Date Validator\n")
    month, day, year = input("Enter a date (mm/dd/yyyy): ").split("/")
    if isValidDate(int(month), int(day), int(year)):
        print("The date is valid.")
    else:
        print("The date is invalid.")

if __name__ == '__main__':
    main()
##>>> 
##Date Validator
##
##Enter a date (mm/dd/yyyy): 04/06/2014
##The date is valid.
##>>> main()
##Date Validator
##
##Enter a date (mm/dd/yyyy): 02/29/2000
##The date is valid.
##>>> main()
##Date Validator
##
##Enter a date (mm/dd/yyyy): 02/29/2001
##The date is invalid.
##>>> 


# c07ex13.py
#    Day number calculation

from c07ex11 import isLeap
from c07ex12 import isValidDate

def dayNumber(month, day, year):
    dayNum = 31*(month-1) + day
    
    if month > 2:
        dayNum = dayNum - (4 * month + 23) // 10
        
    if isLeap(year):
        if month > 2:
            dayNum = dayNum + 1

    return dayNum

def main():
    print("Day number calculation\n")
    
    month, day, year = input("Enter date (mm/dd/yyyy): ").split("/")
    day, month, year = int(day), int(month), int(year)

    if isValidDate(month, day, year):
        print("The day number is", dayNumber(month, day, year))
    else:
        print("That's an invalid date!")

if __name__ == '__main__':
    main()

##>>> 
##Day number calculation
##
##Enter date (mm/dd/yyyy): 04/05/2014
##The day number is 95
##>>> main()
##Day number calculation
##
##Enter date (mm/dd/yyyy): 04/05/2000
##The day number is 96
##>>>             



    
    
