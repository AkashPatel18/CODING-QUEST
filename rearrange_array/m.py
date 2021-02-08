def re(arr,n):
    ans= []

    

    for i in range(0, n):
        arr[i] += (arr[arr[i]] % n) * n
        print(arr)

    # Second Step: Divide all values
    # by n
    for i in range(0, n):
        arr[i] = int(arr[i] / n)


arr = [3,2,0,1]
n=len(arr)
print(re(arr,n))
