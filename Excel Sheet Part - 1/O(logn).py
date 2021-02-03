
def ExcelColumn(N):
    #return required string
    #code here
    ans = ""

    while(N > 0):
        rem = N % 26
        if rem == 0:
            ans += "Z"
            N = (N//26)-1

        else:
            ans += chr(rem+64)
            N = N//26

    return ans[::-1]
