from random import randint


def ranColor():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return r,g,b

for i in range (4):
    print(ranColor())
