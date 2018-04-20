def diffOverSum(x,y):
    return (x+y)/(x-y)
def conv(cels):
    return 9.0 / 5.0 * cels + 32
def main():
    print('Celsius\tFahren.\tDiff over Sum')
    for n in range (0,101,10):
        a = conv(n)
        print (n, '\t', a, '\t', '%.2f' % diffOverSum(n,a))
main()
