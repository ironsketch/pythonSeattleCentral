
def numToMonth(num):
    months = ['January',
              'Febuary',
              'March',
              'April',
              'May',
              'June',
              'July',
              'August',
              'September',
              'October',
              'November',
              'December']
    return months[num - 1]

num = [2,3,5,6,10]

def main(num):
    for i in num:
        month = numToMonth(i)
        print(month)

main(num)

print('+++++++++++++++++++++++++')

def reverse():
    for i in range(12):
        print(12 - i, numToMonth(12 - i))

reverse()

print('+++++++++++++++++++++++++')

def even():
    for i in range(1,13):
        if i % 2 == 0:
            print(numToMonth(i).upper())

        else:
            print(numToMonth(i).lower())

even()
