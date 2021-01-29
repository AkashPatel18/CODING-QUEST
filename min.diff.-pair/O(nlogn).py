#https://practice.geeksforgeeks.org/problems/minimum-difference-pair5444/1#

class Solution:
	def minimum_difference(self, nums):
		# Code here
		nums.sort()

		temp = 199999
		for i in range(len(nums)-1):
		    temp = min(nums[i+1]-nums[i], temp)

		return temp
