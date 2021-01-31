#https://www.hackerrank.com/challenges/sparse-arrays/problem?h_r=next-challenge&h_v=ze
from collections import Counter
def matchingStrings(strings, queries):
    x = Counter(strings)
    print(x)
    print(queries)
    ans = []
    for i in range(len(queries)):
        if queries[i] in x:
            ans.append(x.get(queries[i]))
        else:
            ans.append('0')
    return ans
