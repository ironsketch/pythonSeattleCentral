stringText = '2.5, 8.5, 10.5'

def txt2nums(txt):
    theList = []
    txt = txt.split('\n')
    for row in txt:
        row = row.replace(',','')
        for item in row.split(' '):
            theList.append(float(item))
    return theList

def maxOf(L):
    L = sorted(L)
    Max = L[len(L) - 1]
    print('Max Num: ', Max)
    return Max

def minOf(L):
    L = sorted(L)
    Min = L[0]
    print('Min Num: ', Min)
    return Min

def avgOf(L):
    newList = []
    for item in L:
        newList.append(item)
    avg = 0
    for n in newList:
        avg += n
    avg /= len(newList)
    print('Average: ', avg)
    return avg

def max_min_Avg(fname):
    inFile = open(fname, 'r')
    docData = inFile.read()
    inFile.close()
    theList = (txt2nums(docData))
    return theList

def findMetricOf(fname):
    theList = max_min_Avg(fname)
    maxNum = maxOf(theList)
    minNum = minOf(theList)
    avgNum = avgOf(theList)
    metric = avgNum * (maxNum - minNum) / (maxNum + minNum)
    print('Metric: ', metric)

findMetricOf('quiz5Floats.txt')

