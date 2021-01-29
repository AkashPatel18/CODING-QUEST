def smallestDiff(a,b):
    f = 0
    s = 0

    n = len(a)
    m = len(b)

    a.sort()
    b.sort()


    while f<n and s<m:
        firstnum = a[f]
        secondnum = b[s]

        if firstnum<secondnum:
            difference = secondnum - firstnum
            f += 1
        elif secondnum < firstnum:
            difference = firstnum - secondnum
            s -= 1
        else:
            return [firstnum,secondnum]
    return firstnum,secondnum      



a = [-1, 3 ,5 , 10,20,28]
b = [15 , 17 , 26, 134 , 135]

print(smallestDiff(a,b))