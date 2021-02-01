from collections import Counter


def areIsomorphic(str1, str2):
    s3 = list(str1)
    s4 = list(str2)

    x = Counter(s3)
    y = Counter(s4)

    d = list(x.values())
    f = list(y.values())

    #print(d,f)

    if d == f:
        return 1
    else:
        return 0

s1 = "aab"
s2 = "xxy"

print(areIsomorphic(s1,s2))


