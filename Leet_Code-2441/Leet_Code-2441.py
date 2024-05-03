'''
Question 2441
'''

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        max = -1
        i = -1
        while (nums[i] > 0):
            if (-nums[i]) in nums:
                max = nums[i]
                break
            if i<-len(nums)+1:
                break
            else:
                i -= 1
        return max