def missingPanagram(s):

    key = list("abcdefghijklmnopqrstuvwxyz")
    value = [0]*26

    maindict = dict(zip(key, value))

    for i in s:
        x = i.lower()
        maindict[x] = 1

    ans = []

    for i in maindict:
        if maindict[i] == 0:
            ans.append(i)
    ans.sort()
    ans = "".join(ans)
    return ans
