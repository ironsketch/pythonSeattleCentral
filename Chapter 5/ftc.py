

def table_Ex1():
    print('{0:^10}  {1:^10}'.format('column 1','column 2'))
    for i in range(200,301,10):
        print('{0:^10}  {1:^10}'.format(i,2*i))


def fToC(far):
    cel = (5 / 9) * (far - 32)
    return cel

def main():
    print('  {0:^10}  {1:^10}'.format('Fahren','cels'))
    for i in range (0,200,10):
        far = fToC(i)
        print('   {0:8.2f}    {1:8.2f}'.format(i,far))

main()
