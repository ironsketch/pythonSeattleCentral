def seq(n):
    L = []
    counter = 0
    while n != 1:
        if n % 2 == 0:
            n /= 2
            counter += 1
            L.append(n)
        else:
            n = (3 * n) + 1
    return L,counter,n

def addit(L):
    added = 0
    for i in L:
        added += i
    return added

def main():
    syrLength = {}
    syrAdded = {}
    for i in range (1,1001):
        L = seq(i)
        added = addit(L)
        ave = added / len(L)
        syr[len(L)] = i
    print('The longest sequence was for ')
