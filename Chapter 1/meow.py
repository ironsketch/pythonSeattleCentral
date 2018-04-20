print ("A chaotic function")

print('-------------------------------')
def cchaos (b):
    for i in range(10):
        linenum = 1
        b = 3.9 * b * (1 - b)
        linenum = linenum + 1
        print(linenum, '\t%.3f' % b)

for x in range (6):
    x = .25 + x * .01
    print ("Run Through")
    cchaos (x)


