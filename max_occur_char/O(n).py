#https://practice.geeksforgeeks.org/problems/maximum-occuring-character-1587115620/1/?track=dsa-workshop-1-strings&batchId=308#

from collections import Counter
#import collections

def getMaxOccurringChar(s):
    s = sorted(s)
    #print(s)

    dm = []

    for i in s:
        d = s.count(i)
        dm.append(d)
    x = set(dm)
    #print(dit)
    if len(x) == 1:
        return s[0]

    return s[max(x)]
    





s = input()
print(getMaxOccurringChar(s))
