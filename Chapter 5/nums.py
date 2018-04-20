def opener():
    fin1 = open('nums.txt','r')
    for line in fin1:
        print(line[:-1])
    fin1.close()
L = ['meow','mew','MEOW','meeoeowowowowow']
def fileWrite():
    out = open('nums.txt','w')
    for i in L:
        print(i,file = out)
    out.close()

opener()
fileWrite()

