def isFactor(n):
    for i in range(2,n + 1):
        if n % i == 0:
            return True
        else:
            return False
        
    
print(isFactor(12))
