
#https://practice.geeksforgeeks.org/problems/reverse-words-in-a-given-string5459/1/?track=dsa-workshop-1-strings&batchId=308

def reverseWords(S):
    # code here

    s1 = S.split('.')
    x = len(s1)

    ans = s1[x-1]

    for i in range(x-2, -1, -1):
        ans += "."+s1[i]

    return ans
