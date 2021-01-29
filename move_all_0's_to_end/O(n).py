#https://practice.geeksforgeeks.org/problems/move-all-zeroes-to-end-of-array0751/1#
# gfg sol.
"""
class Solution:
	def pushZerosToEnd(self, arr, n):
	    temp = 0

	    for i in range(n):
	        if arr[i] != 0:
	            arr[temp] = arr[i]
	            temp += 1

	    while (temp < n):
	        arr[temp] = 0
	        temp += 1

"""

#generalize sol (not maintaining 0's order)

def zero(arr, n):
    i = 0
    j = n-1

    while(i <= j):
        if arr[i] == 0 and arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
            print(arr)
        elif arr[i] == 0 and arr[j] == 0:
            j -= 1
            print("this is i",i)
        elif arr[i] != 0 and arr[j] != 0:
            i += 1
            print("this is i", i)
        else:
            j -= 1
            print("this is j", j)
    return arr


n = 20
arr = [15, 12, 0, 0, 0, 2, 2, 19, 6, 17, 16, 20, 0, 2, 16, 0, 10, 0, 14, 15, ]

print(zero(arr, n))
