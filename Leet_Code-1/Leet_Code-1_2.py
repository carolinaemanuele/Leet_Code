'''
Question 1
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(0,len(nums)):
            for y in range(0,len(nums)):
                if (x!=y) and (nums[x]+nums[y]==target):
                    return [x,y]
                    break