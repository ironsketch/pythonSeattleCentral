def toCm(inches):
    cm = inches * 2.54
    return cm

def wholeFeetFrom(inches):
    wholeFeet = inches // 12
    return wholeFeet

def leftOver(inches):
    leftOver = inches % 12
    return leftOver

def wholeMetersFrom(cm):
    cm = toCm(cm)
    meters = cm // 100
    return meters

def remaining(cm):
    cm = toCm(cm)
    remainingcm = cm % 100
    return remainingcm

def englishToMetric():
    print('feet\tinches\t     meters\tcent')
    print('------\t------\t     ------\t------')
    i = 0
    while i <= 60:
        print(format(wholeFeetFrom(i),'.0f'),'     ',format(leftOver(i),'.3f'),'         ',format(wholeMetersFrom(i),'.0f'),'\t',format(remaining(i),'.3f'))
        i +=2.50

englishToMetric()
        
