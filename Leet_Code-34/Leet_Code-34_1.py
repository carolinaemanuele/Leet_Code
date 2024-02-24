'''
Question 34
'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if (target & target) in nums:
            x = min(i for i,num in enumerate(nums) if num==target)
            y = max(i for i,num in enumerate(nums) if num==target)
            return [x,y]
        return [-1,-1]