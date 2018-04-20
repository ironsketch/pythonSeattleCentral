# Assume the days of the week are numbered 0,1,2,3,4,5,6 from Sunday to Saturday.
#  Writea function, dayNum2day(dayNum), which is given the day number, and
# which returns the day name (a string).  Use a for loop to cycle over all the
# numbers and print out the corresponding day name.  Use if elif.

daysOfTheWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def dayNum2Day(dayNum):
    return daysOfTheWeek[dayNum]
day = eval(input('Enter Number 0 - 6: '))
print (dayNum2Day(day))
