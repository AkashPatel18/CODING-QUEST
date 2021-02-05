def checkKthBit(n, k):
    #Your code here
    x = bin(n).replace("0b", "")

    #(x)

    y = str(x)

    m = len(y)

    if y[m-1-k] == "1":
        return True
    else:
        return False




if __name__ == "__main__":
    t = int(input())

    while(t>0):
        n = int(input())
        k = int(input())

        print(checkKthBit(n,k))

        t -= 1
