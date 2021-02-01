#https: // practice.geeksforgeeks.org/problems/anagram-1587115620/1 /?track = dsa-workshop-1-strings & batchId = 308

from collections import Counter


def isAnagram(a, b):
    x = Counter(a)
    y = Counter(b)

    x1 = list(x.keys())
    x2 = list(x.values())

    y1 = list(y.keys())
    y2 = list(y.values())

    if x1 == y1 and x2 == y2:
        return True
    else:
        return False

a = "b"
b  ="d"

print(isAnagram(a,b))
