'''
Question 1 - Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
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
                