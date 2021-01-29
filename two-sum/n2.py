def twosum(arr,target):
    for i in range(n):
        for j in range(i,n):
            if arr[i] + arr[j] == target:
                return i,j


if __name__=="__main__":

    arr = [8,7,6,5]
    target = 13
    n = len(arr)

    print(twosum(arr,target))