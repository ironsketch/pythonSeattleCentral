person = ['I','You','He','She']
does = ['went','ran','said']

def nestedLoop(person,does):
    for per in person:
        for do in does:
            print(per,do,'.')

nestedLoop(person,does)

