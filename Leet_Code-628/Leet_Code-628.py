'''
Question 628
'''

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return 0
        nums.sort()
        return nums[-1]*nums[-2]*nums[-3] if nums[-1]*nums[-2]*nums[-3]>nums[0]*nums[1]*nums[-1] else nums[0]*nums[1]*nums[-1]