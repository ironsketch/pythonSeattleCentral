L = ['one',2,'buckle',3,7,10,'book','python',16,17,'gold','myrh']

def cond(L):
    evenInt = []
    oddInt = []
    evenString = []
    oddString = []
    for item in L:
        if type(item) == str and len(item) % 2 == 0:
            evenString.append(item)
        elif type(item) == str:
            oddString.append(item)
        elif item % 2 == 0:
            evenInt.append(item)
        else:
            oddInt.append(item)
    return evenInt, oddInt, evenString, oddString

a,b,c,d = cond(L)

print(a,'\n',b,'\n',c,'\n',d)
