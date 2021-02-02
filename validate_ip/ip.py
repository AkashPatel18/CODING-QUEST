def isValid(s):
    #code here
    x = s.count('.')

    if x != 3:
        return 0

    sn = s.split('.')

    ct = 0
    for i in sn:
        i.replace(" ", "")

        if i.isdigit() == True and len(i) <= 3 and int(i) < 256:

            if i[0] == '0' and len(i) > 1:

                return 0
            ct += 1

    if ct == 4:
        return 1

    else:
        return 0
    



s = "222. 111.111.111"

print(isValid(s))
