def recur(order):
    if order == 0:
        print('order 0')
        
    else:
        recur(order - 1)
        print ('first recursion')
        recur(order - 1)
        print ('second recursion')

recur(2)
