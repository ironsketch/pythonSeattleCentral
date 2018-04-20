StartOdd, EndOdd = eval(input('Please enter in 2 odd numbers seperated by a comma: '))
if (StartOdd % 2 == 0):
    StartOdd += 1
def sumOdds(StartOdd,EndOdd):
    total = 0
    counter = 0
    for i in range(StartOdd,EndOdd + 1,2):
        counter += 1
        total += i
    print('The sum of odd ints from, ', StartOdd, ' to, ', EndOdd, ' is: ', total)
    print('We went through, ', counter,' odd numbers.')
    
sumOdds(StartOdd,EndOdd)
