person = ['John','Jill','Jay']
does = ['runs','walks','rides']
what = ['to work.','from home.','all the time.']

def nestedLoop(person,does,what):
    for per in person:
        for do in does:
            for duh in what:
                print(per,do,duh)

nestedLoop(person,does,what)

