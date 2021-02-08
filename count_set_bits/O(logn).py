def countSetBits(n):
    # code here
    # return the count

    binaryList = ""

    for i in range(1, n+1):
        b = bin(i).replace("0b", "")
        binaryList += (b)

    return binaryList.count("1")


n = int(input())

print(countSetBits(n))