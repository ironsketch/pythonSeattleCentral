def even_1(n):
    if n%2 == 0:
        return True
    else:
        return False
    print()
print ('MEOW+')
print (5,even_1(5))
print (6,even_1(6))
def even_2(n):
    poop = (n%2 == 0)
    return poop
print()
print ('MEOW+')
print (5,even_2(5))
print (6,even_2(6))

def odd(n):
    poop = (n%2 == 1)
    return poop
print()
print ('MEOW-')
print (5,odd(5))
print (6,odd(6))

def odd_2(n):
    poop = (n%2 != 0)
    return poop
print()
print ('MEOW-')
print (5,odd_2(5))
print (6,odd_2(6))

def toggle(n):
    poop = not even_1(n)
    return poop
print()
print ('MEOW-')
print (5,toggle(5))
print (6,toggle(6))
