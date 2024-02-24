'''
Question 34
'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if (target & target) in nums:
            x = [i for i,num in enumerate(nums) if num==target]
            return [min(x),max(x)]
        return [-1,-1]