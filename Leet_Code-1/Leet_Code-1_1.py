'''
Question 1
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_without_x = nums.copy()
        for x in nums:
            i = nums.index(x)
            diference = target-x
            nums_without_x[i] = None
            if diference in nums_without_x:
                return [i, nums_without_x.index(diference)]
                