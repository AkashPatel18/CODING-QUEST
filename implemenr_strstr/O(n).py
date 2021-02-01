def strstr(s, p):
    #code here

    if p in s:
        print(s.index(p))
        return s.index(p[0])
    else:
        return -1
s = "Gekesforgeeks"

p ="for"

print(strstr(s,p))