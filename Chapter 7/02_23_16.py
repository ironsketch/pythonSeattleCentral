def isIntEven(i):
    if (i % 5 == 0) and (i % 3 == 0):
        return True
    else:
        return False

def isIntEven_1(i):
    div3 = i % 5 == 0
    div5 = i % 3 == 0
    TV = div3 and div5
    return TV

for i in range(31):
    print(i, isIntEven_1(i))

