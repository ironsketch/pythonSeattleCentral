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

def textToNum(dayNum):
    if dayNum == 'sunday':
        day = 0
    elif dayNum == 'monday':
        day = 1
    elif dayNum == 'tuesday':
        day = 2
    elif dayNum == 'wednesday':
        day = 3
    elif dayNum == 'thursday':
        day = 4
    elif dayNum == 'friday':
        day = 5
    elif dayNum == 'saturday':
        day = 6
    else:
        print('Misspelling')
    return day

def dayBack():
    inputName = input('Enter day of the week you are leaving. Spell correctly: ')
    lowerName = inputName.lower()
    length = eval(input('How long are you on vaca?: '))
    convert = textToNum(lowerName)
    figured = (length % 7) + convert

    print (dayNum2Day(figured))

dayBack()
