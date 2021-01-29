#https: // practice.geeksforgeeks.org/problems/triplet-sum-in-array-1587115621/1

def find3Numbers(arr, N, X):
    # Your Code Here
    arr.sort()
    print(arr)

    for i in range(N):
        left = i+1
        right = N-1
        while(left < right):
            if arr[i] + arr[left]+arr[right] == X:
                print(i,left,right)
                return 1
            elif arr[i] + arr[left]+arr[right] > X:
                right -= 1
            else:
                left += 1

    return 0


if __name__=="__main__":

    n,sum = map(int,input().strip().split())
    a= list(map(int,input().strip().split()))
    print(find3Numbers(a,n,sum))
