def sumDigits(n):
    string = str(n)
    added = 0
    for num in string:
        added += int(num)
    return added

print(sumDigits(19))
