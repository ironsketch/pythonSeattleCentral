def dayNum2Day(dayNum):
    if dayNum == 0:
        day = 'Sunday'
    elif dayNum == 1:
        day = 'Monday'
    elif dayNum == 2:
        day = 'Tuesday'
    elif dayNum == 3:
        day = 'Wednesday'
    elif dayNum == 4:
        day = 'Thursday'
    elif dayNum == 5:
        day = 'Friday'
    else:
        day = 'Saturday'
    return day

def dayBack():
    start = eval(input('enter day number 0 - 6: '))
    length = eval(input('How long are you on vaca?: '))
    figured = (length % 7) + start

    print (dayNum2Day(figured))

dayBack()
