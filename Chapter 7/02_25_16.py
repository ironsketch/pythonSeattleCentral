def encodeCharCir(c,n):
    alfa = 'abcdefghijklmnopqrstuvwxyz'
    ndx = alfa.find(c)
    new_ndx = (ndx + n) % 26
    new_char = alfa[new_ndx]
    return new_char

def main():
    for c in 'abcdefghijklmnopqrstuvwxyz':
        print(c,encodeCharCir(c,3))


if __name__ == '__main__':
    main()
