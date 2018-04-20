L = ['pooy','poop',1,2,3,4,5,7,8,9,12,14,15,17,19,'duhy','poo','pooooooooopppy']

def lengthAndY(item):
    length = len(item) % 4 == 0
    yesY = 'y' in item
    return length and yesY

def runThroughAll(L):
    for item in L:
        if type(item) == str:
            print(item, lengthAndY(item))
        else:
            div5 = item % 5 == 0
            not2 = not (item % 2 == 0)
            greaterThan7 = item > 7
            TV = (div5 and not2) or greaterThan7
            print(item, TV)
            

runThroughAll(L)
