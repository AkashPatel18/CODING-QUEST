#https://leetcode.com/problems/two-sum/submissions/
  
        
        

def twosum(arr,target):
    nums ={}

    for i in range(len(arr)):
        if target - arr[i] in nums:
            return [arr.index(target-arr[i]),i]
        else:
            nums[arr[i]] = True
            print(nums)
    return []   

if __name__=="__main__":

    arr = [8,7,6,5]
    target = 13
    n = len(arr)

    print(twosum(arr,target))